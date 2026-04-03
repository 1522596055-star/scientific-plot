#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PROFILER = REPO_ROOT / "skills" / "scientific-plotter" / "scripts" / "profile_tabular_data.py"
FINDER = REPO_ROOT / "skills" / "scientific-plotter" / "scripts" / "find_samples.py"


def run_json(command: list[str]) -> dict:
    completed = subprocess.run(command, cwd=REPO_ROOT, capture_output=True, text=True, check=True)
    return json.loads(completed.stdout)


def assert_equal(actual: object, expected: object, message: str) -> None:
    if actual != expected:
        raise AssertionError(f"{message}: expected {expected!r}, got {actual!r}")


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validate_profiler() -> None:
    cases = [
        {
            "path": "test-data/catalyst_activity_summary.csv",
            "chart_family": "bar",
        },
        {
            "path": "test-data/engine_dual_metric_scan.csv",
            "chart_family": "multi_panel",
        },
        {
            "path": "test-data/method_similarity_matrix.tsv",
            "chart_family": "heatmap",
        },
        {
            "path": "test-data/long_form_similarity_matrix.csv",
            "chart_family": "heatmap",
        },
        {
            "path": "test-data/treatment_conversion_repeats.csv",
            "chart_family": "distribution",
            "layout": "boxplot",
        },
    ]

    for case in cases:
        summary = run_json([sys.executable, str(PROFILER), case["path"]])
        top = summary["recommended_patterns"][0]
        assert_equal(top["chart_family"], case["chart_family"], f"wrong top chart family for {case['path']}")
        if "layout" in case:
            assert_equal(top["layout"], case["layout"], f"wrong layout for {case['path']}")

    ignition = run_json([sys.executable, str(PROFILER), "test-data/ignition_delay_scan.csv"])
    ignition_top = ignition["recommended_patterns"][0]
    assert_equal(ignition_top["chart_family"], "scatter", "ignition-delay top chart should favor scatter")
    assert_equal(ignition_top["mapping_hints"]["x"], "temperature_K", "ignition-delay x mapping")
    assert_equal(ignition_top["mapping_hints"]["y"], "ignition_delay_ms", "ignition-delay y mapping")
    assert_equal(ignition_top["mapping_hints"]["y_scale"], "log", "ignition-delay y-scale hint")

    bubble = run_json([sys.executable, str(PROFILER), "test-data/cluster_embedding_points.csv"])
    bubble_top = bubble["recommended_patterns"][0]
    assert_equal(bubble_top["chart_family"], "scatter", "bubble dataset should favor scatter")
    assert_equal(bubble_top["layout"], "bubble_scatter", "bubble dataset should prefer bubble layout")
    assert_equal(bubble_top["mapping_hints"]["x"], "x", "bubble x mapping")
    assert_equal(bubble_top["mapping_hints"]["y"], "y", "bubble y mapping")
    assert_equal(bubble_top["mapping_hints"]["size"], "bubble_size", "bubble size mapping")

    validation = run_json([sys.executable, str(PROFILER), "test-data/validation_profile_with_errors.csv"])
    validation_top = validation["recommended_patterns"][0]
    assert_equal(validation_top["chart_family"], "line", "validation table should stay on a line-oriented path")
    assert_equal(validation_top["layout"], "single_panel_with_uncertainty", "validation table should prefer line-with-uncertainty")
    assert_equal(validation_top["mapping_hints"]["x"], "x_value", "validation table x mapping")
    assert_equal(validation_top["mapping_hints"]["y"], "y_value", "validation table y mapping")
    assert_true(
        "error_low" in validation_top["mapping_hints"]["uncertainty_columns"] and "error_high" in validation_top["mapping_hints"]["uncertainty_columns"],
        "validation table should expose uncertainty columns",
    )


def validate_finder() -> None:
    shared_x_result = run_json(
        [
            sys.executable,
            str(FINDER),
            "--query",
            "two-panel figure with shared x-axis and multiple line series",
            "--top",
            "5",
        ]
    )
    shared_x_top = shared_x_result["results"][0]
    assert_equal(shared_x_top["sample_id"], "sample_0014", "shared-x multi-panel query should prefer sample_0014")

    single_panel_result = run_json(
        [
            sys.executable,
            str(FINDER),
            "--query",
            "plain single-panel multi-line scientific trend over a continuous x-axis",
            "--top",
            "5",
        ]
    )
    single_panel_top = single_panel_result["results"][0]
    assert_equal(single_panel_top["sample_id"], "sample_0013", "single-panel multi-line query should prefer sample_0013")


if __name__ == "__main__":
    validate_profiler()
    validate_finder()
    print("scientific-plotter validation passed")
