"""Regression tests for the Week 8 object-oriented SOC analyzer."""

import csv
import pytest
import json

from project import (
    LoginEvent,
    SOCAnalyzer,
    SOCReport,
    analyze_events,
    classify_severity,
    detect_sensitive_account,
    export_csv,
    iter_high_severity,
    main,
    export_report,
    validate_ip,
)


# LoginEvent


def test_login_event_attributes():
    event = LoginEvent(
        "admin",
        "192.0.2.10",
        12,
        "2026-10-08T09:00:00"
    )

    assert event.user == "admin"
    assert event.ip == "192.0.2.10"
    assert event.failed == 12
    assert event.timestamp == "2026-10-08T09:00:00"


def test_login_event_properties():
    admin_event = LoginEvent(
        "ADMIN",
        "192.0.2.10",
        12,
        "2026-10-08T09:00:00"
    )

    normal_event = LoginEvent(
        "james",
        "192.0.2.20",
        3,
        "2026-10-08T09:05:00"
    )

    assert admin_event.severity == "HIGH"
    assert admin_event.sensitive_account is True

    assert normal_event.severity == "LOW"
    assert normal_event.sensitive_account is False


def test_login_event_invalid_username():
    with pytest.raises(ValueError):
        LoginEvent("", "192.0.2.10", 5, "2026-10-08T09:00:00")

    with pytest.raises(ValueError):
        LoginEvent("   ", "192.0.2.10", 5, "2026-10-08T09:00:00")


def test_login_event_invalid_ip_and_failed_count():
    with pytest.raises(ValueError):
        LoginEvent("admin", "999.10.10.10", 12, "2026-10-08T09:00:00")

    with pytest.raises(ValueError):
        LoginEvent("admin", "192.0.2.10", -5, "2026-10-08T09:00:00")

    with pytest.raises(ValueError):
        LoginEvent("admin", "192.0.2.10", "unknown", "2026-10-08T09:00:00")


def test_login_event_invalid_timestamp():
    with pytest.raises(ValueError):
        LoginEvent("admin", "192.0.2.10", 5, "yesterday")

    with pytest.raises(ValueError):
        LoginEvent("admin", "192.0.2.10", 5, "2026-13-40")

    with pytest.raises(ValueError):
        LoginEvent("admin", "192.0.2.10", 5, None)


# Validation helpers


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


def test_valid_ip_addresses():
    assert validate_ip("192.168.1.1") is True
    assert validate_ip("10.0.0.15") is True
    assert validate_ip("255.255.255.255") is True


def test_invalid_ip_addresses():
    # Check invalid ranges, incomplete addresses, and leading zeros.
    assert validate_ip("275.3.6.28") is False
    assert validate_ip("192.168.1") is False
    assert validate_ip("192.168.001.1") is False
    assert validate_ip("192.168.1.999") is False
    assert validate_ip("not-an-ip") is False
    assert validate_ip(None) is False


def test_sensitive_accounts():
    # These account names should trigger our watchlist.
    assert detect_sensitive_account("admin") is True
    assert detect_sensitive_account("administrator") is True
    assert detect_sensitive_account("root") is True


def test_sensitive_accounts_case_insensitive():
    # Account names should match regardless of capitalization.
    assert detect_sensitive_account("ADMIN") is True
    assert detect_sensitive_account("Root") is True
    assert detect_sensitive_account("AdMiN") is True


def test_normal_accounts():
    # Partial matches and ordinary usernames should not trigger.
    assert detect_sensitive_account("favour") is False
    assert detect_sensitive_account("james") is False
    assert detect_sensitive_account("admin123") is False
    assert detect_sensitive_account("superadmin") is False


# SOCAnalyzer


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


def test_reject_event_with_invalid_ip():
    events = [
        {
            "user": "admin",
            "ip": "999.10.10.10",
            "failed": 12,
            "timestamp": "2026-10-08T09:00:00",
        }
    ]

    report = analyze_events(events)

    assert report["total"] == 1
    assert report["valid"] == 0
    assert report["invalid"] == 1
    assert report["valid_events"] == []


def test_analyzer_with_login_event_objects():
    events = [
        {
            "user": "admin",
            "ip": "192.0.2.10",
            "failed": 12,
            "timestamp": "2026-10-08T09:00:00",
        },
        {
            "user": "favour",
            "ip": "192.0.2.20",
            "failed": 2,
            "timestamp": "2026-10-08T09:05:00",
        },
    ]

    report = analyze_events(events)

    assert report["valid"] == 2
    assert report["invalid"] == 0
    assert report["sensitive_count"] == 1
    assert report["sensitive_high_count"] == 1
    assert report["valid_events"][0]["severity"] == "HIGH"
    assert report["valid_events"][1]["severity"] == "LOW"


def test_analyzer_skips_invalid_login_objects():
    events = [
        {
            "user": "admin",
            "ip": "999.999.999.999",
            "failed": 12,
            "timestamp": "2026-10-08T09:00:00",
        },
        {
            "user": "root",
            "ip": "192.0.2.30",
            "failed": 11,
            "timestamp": "2026-10-08T09:05:00",
        },
    ]

    report = analyze_events(events)

    assert report["total"] == 2
    assert report["valid"] == 1
    assert report["invalid"] == 1
    assert report["sensitive_count"] == 1
    assert report["sensitive_high_count"] == 1
    assert report["ips"]["192.0.2.30"] == 1
    assert "999.999.999.999" not in report["ips"]


def test_detection_summary():
    # Only watchlist matches should contribute to these counts.
    events = [
        {
            "user": "admin",
            "ip": "192.0.2.10",
            "failed": 12,
            "timestamp": "2026-10-08T09:00:00",
        },
        {
            "user": "root",
            "ip": "192.0.2.11",
            "failed": 6,
            "timestamp": "2026-10-08T09:05:00",
        },
        {
            "user": "james",
            "ip": "192.0.2.12",
            "failed": 15,
            "timestamp": "2026-10-08T09:10:00",
        },
    ]

    report = analyze_events(events)

    assert report["sensitive_count"] == 2
    assert report["sensitive_high_count"] == 1


def test_soc_analyzer_class():
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
    ]

    analyzer = SOCAnalyzer(events)
    report = analyzer.analyze()

    assert report["total"] == 2
    assert report["valid"] == 2
    assert report["severity"]["HIGH"] == 1
    assert report["severity"]["MEDIUM"] == 1
    assert report["ips"]["192.0.2.10"] == 2
    assert report["sensitive_count"] == 1


def test_soc_analyzer_independent_instances():
    # Each analyzer should work with its own dataset.
    first_events = [
        {
            "user": "admin",
            "ip": "192.0.2.10",
            "failed": 15,
            "timestamp": "2026-10-08T09:00:00",
        }
    ]

    second_events = [
        {
            "user": "favour",
            "ip": "192.0.2.20",
            "failed": 2,
            "timestamp": "2026-10-08T09:05:00",
        }
    ]

    first_analyzer = SOCAnalyzer(first_events)
    second_analyzer = SOCAnalyzer(second_events)

    first_report = first_analyzer.analyze()
    second_report = second_analyzer.analyze()

    assert first_report["sensitive_count"] == 1
    assert first_report["severity"]["HIGH"] == 1

    assert second_report["sensitive_count"] == 0
    assert second_report["severity"]["LOW"] == 1


def test_empty_dataset():
    report = SOCAnalyzer([]).analyze()

    assert report["total"] == 0
    assert report["valid"] == 0
    assert report["invalid"] == 0
    assert report["valid_events"] == []
    assert report["sensitive_count"] == 0
    assert report["sensitive_high_count"] == 0


def test_invalid_event_types():
    events = [
        None,
        "not a dictionary",
        {},
        {
            "user": "admin",
            "ip": "192.0.2.10",
            "failed": 12,
            "timestamp": "2026-10-08T09:00:00",
        },
    ]

    report = SOCAnalyzer(events).analyze()

    assert report["total"] == 4
    assert report["valid"] == 1
    assert report["invalid"] == 3
    assert report["severity"]["HIGH"] == 1


# SOCReport and compatibility exports


def test_export_csv(tmp_path):
    events = [
        {
            "timestamp": "2026-10-08T09:00:00",
            "user": "admin",
            "ip": "192.0.2.10",
            "failed": 12,
            "severity": "HIGH",
            "sensitive_account": True
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
    assert report["valid_events"][0]["sensitive_account"] is True
    assert "===== SENSITIVE ACCOUNT FINDINGS =====" in content
    assert "Account: admin" in content
    assert "IP: 192.0.2.10" in content
    assert "Failed: 12" in content


def test_report_without_sensitive_accounts(tmp_path):

    events = [
        {
            "user": "favour",
            "ip": "192.0.2.20",
            "failed": 2,
            "timestamp": "2026-10-08T09:00:00",
        }
    ]

    report = analyze_events(events)
    output_path = tmp_path / "soc_report.txt"

    export_report(report, output_path)

    content = output_path.read_text(encoding="utf-8")

    assert "===== SENSITIVE ACCOUNT FINDINGS =====" in content
    assert "No sensitive account activity detected." in content


def test_detection_summary_in_report(tmp_path):
    # Confirm the detection counts are written to the text report.
    events = [
        {
            "user": "ADMIN",
            "ip": "192.0.2.10",
            "failed": 11,
            "timestamp": "2026-10-08T09:00:00",
        }
    ]

    report = analyze_events(events)
    output_path = tmp_path / "soc_report.txt"

    export_report(report, output_path)

    content = output_path.read_text(encoding="utf-8")

    assert "===== DETECTION SUMMARY =====" in content
    assert "Sensitive Account Events: 1" in content
    assert "HIGH Severity Sensitive Events: 1" in content

# Test that the report sections are separated by a single blank line.
def test_report_section_spacing(tmp_path):
    events = [
        {
            "user": "admin",
            "ip": "192.0.2.10",
            "failed": 12,
            "timestamp": "2026-10-08T09:00:00",
        }
    ]

    report = analyze_events(events)
    output_path = tmp_path / "soc_report.txt"

    export_report(report, output_path)

    content = output_path.read_text(encoding="utf-8")

    # Each section should be separated by one blank line.
    assert "LOW Severity: 0\n\n===== REPEATED IP ADDRESSES =====" in content
    assert "No repeated IP addresses detected.\n\n===== SENSITIVE ACCOUNT FINDINGS =====" in content
    assert "Severity: HIGH\n\n===== DETECTION SUMMARY =====" in content

# Test that the SOCReport class can generate a text report with the expected content.
def test_soc_report_class_csv(tmp_path):
    events = [
        {
            "user": "admin",
            "ip": "192.0.2.10",
            "failed": 12,
            "timestamp": "2026-10-08T09:00:00",
        }
    ]

    report = SOCAnalyzer(events).analyze()
    output_path = tmp_path / "cleaned_events.csv"

    SOCReport(report).export_csv(output_path)

    with open(output_path, "r", newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    assert len(rows) == 1
    assert rows[0]["user"] == "admin"
    assert rows[0]["severity"] == "HIGH"
    assert rows[0]["sensitive_account"] == "True"

# Command-line interface (CLI) tests
def test_soc_report_class_text(tmp_path):
    events = [
        {
            "user": "root",
            "ip": "192.0.2.20",
            "failed": 11,
            "timestamp": "2026-10-08T09:00:00",
        }
    ]

    report = SOCAnalyzer(events).analyze()
    output_path = tmp_path / "soc_report.txt"

    SOCReport(report).export_text(output_path)

    content = output_path.read_text(encoding="utf-8")

    assert "Total Events: 1" in content
    assert "HIGH Severity: 1" in content
    assert "Account: root" in content
    assert "Sensitive Account Events: 1" in content
    assert "HIGH Severity Sensitive Events: 1" in content

# Command-line interface (CLI) tests
def test_cli_custom_output_directory(tmp_path):
    input_path = tmp_path / "events.json"
    output_dir = tmp_path / "reports"

    events = [
        {
            "user": "admin",
            "ip": "192.0.2.10",
            "failed": 12,
            "timestamp": "2026-10-17T09:00:00",
        }
    ]

    input_path.write_text(
        json.dumps(events),
        encoding="utf-8"
    )

    main([
        "--input", str(input_path),
        "--output", str(output_dir),
    ])

    assert (output_dir / "cleaned_login_events.csv").exists()
    assert (output_dir / "soc_report.txt").exists()

    content = (output_dir / "soc_report.txt").read_text(
        encoding="utf-8"
    )

    assert "Total Events: 1" in content
    assert "HIGH Severity: 1" in content

# Test that the CLI handles missing input files gracefully.
def test_cli_missing_input_file(tmp_path):
    missing_file = tmp_path / "missing.json"
    output_dir = tmp_path / "reports"

    with pytest.raises(SystemExit) as error:
        main([
            "--input", str(missing_file),
            "--output", str(output_dir),
        ])

    assert "Unable to load events" in str(error.value)

# Test that the CLI handles invalid JSON input gracefully.
def test_cli_invalid_json(tmp_path):
    input_path = tmp_path / "invalid.json"
    output_dir = tmp_path / "reports"

    input_path.write_text(
        "{this is not valid JSON}",
        encoding="utf-8"
    )

    with pytest.raises(SystemExit) as error:
        main([
            "--input", str(input_path),
            "--output", str(output_dir),
        ])

    assert "Unable to load events" in str(error.value)

# Test that the sensitive_users list is correctly populated and 
# case-insensitive.
def test_sensitive_users_list():
    events = [
        {
            "user": "admin",
            "ip": "192.0.2.10",
            "failed": 12,
            "timestamp": "2026-10-17T09:00:00",
        },
        {
            "user": "james",
            "ip": "192.0.2.20",
            "failed": 2,
            "timestamp": "2026-10-17T09:05:00",
        },
        {
            "user": "root",
            "ip": "192.0.2.30",
            "failed": 11,
            "timestamp": "2026-10-17T09:10:00",
        },
    ]

    report = SOCAnalyzer(events).analyze()

    assert report["sensitive_users"] == ["admin", "root"]
    assert report["sensitive_count"] == 2

# Test that the unique_sensitive_users set is correctly populated 
# and case-insensitive.
def test_comprehension_summaries():
    events = [
        {
            "user": "admin",
            "ip": "192.0.2.10",
            "failed": 12,
            "timestamp": "2026-10-17T09:00:00",
        },
        {
            "user": "ADMIN",
            "ip": "192.0.2.20",
            "failed": 6,
            "timestamp": "2026-10-17T09:05:00",
        },
        {
            "user": "root",
            "ip": "192.0.2.30",
            "failed": 2,
            "timestamp": "2026-10-17T09:10:00",
        },
    ]

    report = SOCAnalyzer(events).analyze()

    assert report["severity_summary"] == {
        "HIGH": 1,
        "MEDIUM": 1,
        "LOW": 1,
    }

    assert report["unique_sensitive_users"] == ["admin", "root"]
    assert report["sensitive_count"] == 3

# Test that the analyzer correctly identifies and reports invalid events
def test_invalid_event_details():
    events = [
        {
            "user": "admin",
            "ip": "192.0.2.10",
            "failed": 12,
            "timestamp": "2026-10-17T09:00:00",
        },
        {
            "user": "root",
            "failed": 15,
            "timestamp": "2026-10-17T09:05:00",
        },
        {
            "user": "james",
            "ip": "192.0.2.20",
            "failed": 2,
            "timestamp": "2026-10-17T09:10:00",
        },
    ]

    report = SOCAnalyzer(events).analyze()

    assert report["total"] == 3
    assert report["valid"] == 2
    assert report["invalid"] == 1

    assert report["invalid_event_details"] == [
        {
            "event_number": 2,
            "reason": "'ip'",
        }
    ]

# Test that the iter_high_severity function correctly filters events with HIGH severity.
def test_iter_high_severity():
    events = [
        {"user": "admin", "severity": "HIGH"},
        {"user": "james", "severity": "LOW"},
        {"user": "root", "severity": "HIGH"},
    ]

    result = list(iter_high_severity(events))

    assert [event["user"] for event in result] == [
        "admin",
        "root",
    ]

