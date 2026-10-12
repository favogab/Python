
import pytest
import csv

from soc_login_analyzer_w6 import (
    classify_severity,
    analyze_events,
    export_csv,
    export_report,
)


def test_low_severity():
    assert classify_severity(0) == "LOW"
    assert classify_severity(4) == "LOW"


def test_medium_severity():
    assert classify_severity(5) == "MEDIUM"
    assert classify_severity(9) == "MEDIUM"


def test_high_severity():
    assert classify_severity(10) == "HIGH"
    assert classify_severity(20) == "HIGH"


def test_invalid_failed_count():
    with pytest.raises(ValueError):
        classify_severity(-1)

    with pytest.raises(ValueError):
        classify_severity("unknown")

    with pytest.raises(ValueError):
        classify_severity(None)


def test_export_csv(tmp_path):
    events = [
        {
            "timestamp": "2026-10-08T09:00:00",
            "user": "admin",
            "ip": "192.0.2.10",
            "failed": 12,
            "severity": "HIGH"
        }
    ]

    output_path = tmp_path / "cleaned_events.csv"

    export_csv(events, output_path)

    with open(output_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    assert len(rows) == 1
    assert rows[0]["user"] == "admin"
    assert rows[0]["severity"] == "HIGH"
    assert rows[0]["failed"] == "12"


def test_export_report(tmp_path):
    events = [
        {
            "user": "admin",
            "ip": "192.0.2.10",
            "failed": 12,
            "timestamp": "2026-10-08T09:00:00"
        },
        {
            "user": "james",
            "ip": "192.0.2.10",
            "failed": 6,
            "timestamp": "2026-10-08T09:05:00"
        }
    ]

    report = analyze_events(events)
    output_path = tmp_path / "soc_report.txt"

    export_report(report, output_path)

    content = output_path.read_text(encoding="utf-8")

    assert "Total Events: 2" in content
    assert "Valid Events: 2" in content
    assert "Invalid Events: 0" in content
    assert "HIGH Severity: 1" in content
    assert "MEDIUM Severity: 1" in content
    assert "Repeated IP: 192.0.2.10 (2 events)" in content


def test_analyze_events():
    events = [
        {
            "user": "admin",
            "ip": "192.0.2.10",
            "failed": 12,
            "timestamp": "2026-10-08T09:00:00",
        },
        {
            "user": "james",
            "ip": "192.0.2.10",
            "failed": 6,
            "timestamp": "2026-10-08T09:05:00",
        },
        {
            "user": "mary",
            "ip": "192.0.2.20",
            "failed": "unknown",
            "timestamp": "2026-10-08T09:10:00",
        },
    ]

    report = analyze_events(events)

    assert report["total"] == 3
    assert report["valid"] == 2
    assert report["invalid"] == 1
    assert report["severity"]["HIGH"] == 1
    assert report["severity"]["MEDIUM"] == 1
    assert report["ips"]["192.0.2.10"] == 2
    assert "192.0.2.20" not in report["ips"]

    assert len(report["valid_events"]) == 2
    assert report["valid_events"][0]["severity"] == "HIGH"
    assert report["valid_events"][1]["severity"] == "MEDIUM"
