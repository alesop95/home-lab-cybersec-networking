"""Prove del modello di spazio, tempi e contratto CLI; nessun dato personale."""

import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest
import uuid


ROOT = Path(__file__).resolve().parents[1]
TOOL_PATH = ROOT / "tools/dimensiona-backup.py"
EXAMPLE_PATH = ROOT / "docs/03-spunti-di-sviluppo/05-strategia-di-backup/esempi/budget-nas-iniziale.json"
spec = importlib.util.spec_from_file_location("dimensiona_backup", TOOL_PATH)
PLANNER = importlib.util.module_from_spec(spec)
spec.loader.exec_module(PLANNER)


def scenario():
    # Piccole grandezze per avere un risultato atteso verificabile a mano:
    # occupato 520 B, nuovo full 100 B, incremento 10 B, lavoro 45 B -> 675 B.
    return {
        "schema_version": 1,
        "input_status": "illustrative",
        "capacity": {
            "layout": "mirror",
            "devices": ["1000 B", "1200 B"],
            "filesystem_reserve": "0 B",
            "max_fraction": "1",
            "planning_limit": "1000 B",
        },
        "fixed_allocations": [{"label": "originali", "size": "100 B"}],
        "snapshot_hold": "20 B",
        "workspace": "30 B",
        "full_archives": [{"label": "vm", "size": "100 B", "keep": 2, "protected": 1}],
        "incremental_repositories": [{
            "label": "file", "base": "80 B", "unique_change_per_point": "10 B",
            "points": 3, "maintenance_workspace": "15 B",
        }],
        "run_time": {"throughput": "30 B/s", "overhead_minutes": 1, "window_minutes": 2},
        "uncertainties": ["dati costruiti, nessun ripristino eseguito"],
    }


class UnitsTests(unittest.TestCase):
    def test_gb_and_gib_have_different_byte_counts(self):
        self.assertEqual(PLANNER.size_bytes("1 GB"), 1_000_000_000)
        self.assertEqual(PLANNER.size_bytes("1 GiB"), 1_073_741_824)
        self.assertEqual(PLANNER.size_bytes("1.5 GB"), 1_500_000_000)

    def test_ambiguous_or_invalid_sizes_are_rejected(self):
        for value in [1, True, None, "1", "1G", "1 gb", "1 Gbit", "-1 GB", "NaN GB", "1e3 GB", "0.1 B"]:
            with self.subTest(value=value), self.assertRaises(PLANNER.ScenarioError):
                PLANNER.size_bytes(value)

    def test_zero_is_allowed_only_where_requested(self):
        self.assertEqual(PLANNER.size_bytes("0 B"), 0)
        with self.assertRaises(PLANNER.ScenarioError):
            PLANNER.size_bytes("0 B", positive=True)


class BudgetTests(unittest.TestCase):
    def test_mirror_uses_the_smallest_device_not_the_sum(self):
        result = PLANNER.dimensiona(scenario())
        self.assertEqual(result["capacity"]["mirror_nominal_bytes"], 1000)

    def test_all_retained_and_temporary_consumers_count_toward_peak(self):
        result = PLANNER.dimensiona(scenario())
        used = result["occupancy"]
        self.assertEqual(used["retained_full_bytes"], 300)
        self.assertEqual(used["retained_incremental_bytes"], 100)
        self.assertEqual(used["steady_bytes"], 520)
        self.assertEqual(used["new_full_bytes"], 100)
        self.assertEqual(used["new_incremental_bytes"], 10)
        self.assertEqual(used["workspace_bytes"], 45)
        self.assertEqual(used["peak_bytes"], 675)
        self.assertEqual(used["headroom_bytes"], 325)

    def test_retention_may_fit_while_a_new_full_does_not(self):
        data = scenario()
        data["capacity"]["planning_limit"] = "600 B"
        result = PLANNER.dimensiona(data)
        self.assertLess(result["occupancy"]["steady_bytes"], 600)
        self.assertFalse(result["fits_capacity"])
        self.assertEqual(result["decision"], "exceeds_planned_bounds")

    def test_one_byte_over_the_limit_changes_admission(self):
        data = scenario()
        data["capacity"]["planning_limit"] = "675 B"
        self.assertTrue(PLANNER.dimensiona(data)["fits_capacity"])
        data["snapshot_hold"] = "21 B"
        self.assertFalse(PLANNER.dimensiona(data)["fits_capacity"])

    def test_fraction_and_explicit_limit_both_apply_after_filesystem_reserve(self):
        data = scenario()
        data["capacity"]["filesystem_reserve"] = "100 B"
        data["capacity"]["max_fraction"] = "0.8"
        result = PLANNER.dimensiona(data)
        self.assertEqual(result["capacity"]["fraction_limit_bytes"], 720)
        data["capacity"]["planning_limit"] = "700 B"
        self.assertEqual(PLANNER.dimensiona(data)["capacity"]["planning_limit_bytes"], 700)

    def test_sequential_archives_reserve_a_whole_new_generation_before_pruning(self):
        data = scenario()
        data["full_archives"].append({"label": "vm-piccola", "size": "40 B", "keep": 1, "protected": 0})
        result = PLANNER.dimensiona(data)
        self.assertEqual(result["occupancy"]["new_full_bytes"], 140)
        self.assertEqual(result["occupancy"]["retained_full_bytes"], 340)
        self.assertEqual(result["occupancy"]["peak_bytes"], 755)

    def test_protected_copies_and_snapshot_hold_cannot_disappear_from_budget(self):
        data = scenario()
        baseline = PLANNER.dimensiona(data)["occupancy"]["peak_bytes"]
        data["full_archives"][0]["protected"] += 1
        data["snapshot_hold"] = "90 B"
        self.assertEqual(PLANNER.dimensiona(data)["occupancy"]["peak_bytes"] - baseline, 170)

    def test_more_versions_never_reduce_the_peak(self):
        data = scenario()
        before = PLANNER.dimensiona(data)["occupancy"]["peak_bytes"]
        for keep in range(3, 9):
            data["full_archives"][0]["keep"] = keep
            now = PLANNER.dimensiona(data)["occupancy"]["peak_bytes"]
            self.assertGreater(now, before)
            before = now

    def test_no_vm_archives_is_a_valid_file_only_plan(self):
        data = scenario()
        data["full_archives"] = []
        result = PLANNER.dimensiona(data)
        self.assertEqual(result["occupancy"]["new_full_bytes"], 0)
        self.assertEqual(result["occupancy"]["retained_full_bytes"], 0)

    def test_example_is_an_estimate_and_all_its_allocations_fit(self):
        result = PLANNER.dimensiona(PLANNER.load_scenario(EXAMPLE_PATH))
        self.assertEqual(result["input_status"], "illustrative")
        self.assertFalse(result["operationally_validated"])
        self.assertEqual(result["occupancy"]["peak_bytes"], 150_500_000_000)
        self.assertEqual(result["occupancy"]["headroom_bytes"], 29_500_000_000)


class TimingTests(unittest.TestCase):
    def test_initial_base_copy_and_recurring_changes_have_separate_durations(self):
        result = PLANNER.dimensiona(scenario())["timing"]
        self.assertEqual(result["initial_write_bytes"], 180)
        self.assertEqual(result["recurring_write_bytes"], 110)
        self.assertEqual(result["initial_seconds"], 66)
        self.assertEqual(result["recurring_seconds"], 64)

    def test_exact_window_boundary_fits_but_one_extra_byte_does_not(self):
        data = scenario()
        data["run_time"] = {"throughput": "3 B/s", "overhead_minutes": 0, "window_minutes": 1}
        first = PLANNER.dimensiona(data)
        self.assertTrue(first["timing"]["fits_initial_window"])
        data["incremental_repositories"][0]["base"] = "81 B"
        second = PLANNER.dimensiona(data)
        self.assertFalse(second["timing"]["fits_initial_window"])
        self.assertTrue(second["timing"]["fits_recurring_window"])
        self.assertEqual(second["decision"], "exceeds_planned_bounds")

    def test_bit_rate_or_unspecified_rate_is_rejected(self):
        for rate in ["1 Gbit/s", "100 Mbps", "100 MB", "0 B/s"]:
            data = scenario()
            data["run_time"]["throughput"] = rate
            with self.subTest(rate=rate), self.assertRaises(PLANNER.ScenarioError):
                PLANNER.dimensiona(data)


class ContractTests(unittest.TestCase):
    def test_typo_in_a_required_budget_field_fails_instead_of_dropping_consumer(self):
        data = scenario()
        data["snapshot_holds"] = data.pop("snapshot_hold")
        with self.assertRaises(PLANNER.ScenarioError):
            PLANNER.dimensiona(data)

    def test_boolean_counts_and_version_are_not_integers_for_this_contract(self):
        data = scenario()
        data["schema_version"] = True
        with self.assertRaises(PLANNER.ScenarioError):
            PLANNER.dimensiona(data)
        data = scenario()
        data["full_archives"][0]["keep"] = True
        with self.assertRaises(PLANNER.ScenarioError):
            PLANNER.dimensiona(data)

    def test_missing_consumers_and_unknown_fields_are_rejected(self):
        for key in ["workspace", "incremental_repositories", "uncertainties"]:
            data = scenario()
            del data[key]
            with self.subTest(key=key), self.assertRaises(PLANNER.ScenarioError):
                PLANNER.dimensiona(data)
        data = scenario()
        data["extra_consumer"] = "500 GB"
        with self.assertRaises(PLANNER.ScenarioError):
            PLANNER.dimensiona(data)

    def test_duplicate_labels_are_rejected(self):
        data = scenario()
        data["full_archives"][0]["label"] = "originali"
        with self.assertRaises(PLANNER.ScenarioError):
            PLANNER.dimensiona(data)

    def test_unsupported_layout_and_impossible_reserve_are_rejected(self):
        for layout in ["raidz", "stripe"]:
            data = scenario()
            data["capacity"]["layout"] = layout
            with self.subTest(layout=layout), self.assertRaises(PLANNER.ScenarioError):
                PLANNER.dimensiona(data)
        data = scenario()
        data["capacity"]["filesystem_reserve"] = "1000 B"
        with self.assertRaises(PLANNER.ScenarioError):
            PLANNER.dimensiona(data)

    def test_measured_input_label_still_does_not_certify_a_real_backup(self):
        data = scenario()
        data["input_status"] = "measured"
        result = PLANNER.dimensiona(data)
        self.assertFalse(result["operationally_validated"])

    def test_function_does_not_change_its_input(self):
        data = scenario()
        before = copy.deepcopy(data)
        PLANNER.dimensiona(data)
        self.assertEqual(data, before)


class CliTests(unittest.TestCase):
    def setUp(self):
        scratch = (ROOT / "_notes/backup-restore/test-tmp").resolve()
        self.assertTrue(scratch.is_relative_to(ROOT.resolve()))
        scratch.mkdir(parents=True, exist_ok=True)
        # Su Windows mkdtemp crea directory 0700 che il token ristretto puo'
        # non riaprire. Un file unico nella cartella del progetto non richiede
        # ACL speciali o privilegi e non cambia il perimetro della prova.
        self.folder = scratch
        self.fixture_path = scratch / ("scenario-" + uuid.uuid4().hex + ".json")
        self.assertTrue(self.fixture_path.resolve().is_relative_to(scratch))
        self.addCleanup(lambda: self.fixture_path.unlink(missing_ok=True))

    def run_cli(self, text):
        path = self.fixture_path
        path.write_text(text, encoding="utf-8")
        return subprocess.run(
            [sys.executable, str(TOOL_PATH), str(path), "--json"],
            capture_output=True, text=True, encoding="utf-8",
        )

    def test_cli_fitting_plan_returns_zero_and_machine_readable_evidence(self):
        result = self.run_cli(json.dumps(scenario()))
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["occupancy"]["peak_bytes"], 675)
        self.assertFalse(report["operationally_validated"])

    def test_cli_excess_capacity_is_one_not_a_schema_error(self):
        data = scenario()
        data["capacity"]["planning_limit"] = "600 B"
        result = self.run_cli(json.dumps(data))
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertEqual(json.loads(result.stdout)["decision"], "exceeds_planned_bounds")

    def test_cli_rejects_duplicate_json_keys_and_nonfinite_numbers(self):
        for text in ['{"schema_version":1,"schema_version":1}', '{"size":NaN}', '{"size":Infinity}']:
            with self.subTest(text=text):
                result = self.run_cli(text)
                self.assertEqual(result.returncode, 2)
                self.assertIn("Scenario non valido", result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_cli_missing_input_is_a_clean_error(self):
        result = subprocess.run(
            [sys.executable, str(TOOL_PATH), str(self.fixture_path.with_suffix(".assente.json"))],
            capture_output=True, text=True, encoding="utf-8",
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("Scenario non valido", result.stderr)


if __name__ == "__main__":
    unittest.main()
