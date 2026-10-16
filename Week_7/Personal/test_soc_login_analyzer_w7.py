
import pytest
import csv

from soc_login_analyzer_w7 import (
    classify_severity,
    analyze_events,
    export_csv,
    export_report,
    validate_ip,
    detect_sensitive_account
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
    assert "SENSITIVE ACCOUNT FINDINGS" in content
    assert report["valid_events"][0]["sensitive_account"] is True
    assert "===== SENSITIVE ACCOUNT FINDINGS =====" in content
    assert "Account: admin" in content
    assert "IP: 192.0.2.10" in content
    assert "Failed: 12" in content

# The report should explain when the watchlist has no matches.
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


# Test cases for the validate_ip function
def test_valid_ip_addresses():
    assert validate_ip("192.168.1.1") is True
    assert validate_ip("10.0.0.15") is True
    assert validate_ip("255.255.255.255") is True

# Test cases for the validate_ip function
def test_invalid_ip_addresses():
    # Check invalid ranges, incomplete addresses, and leading zeros.
    assert validate_ip("275.3.6.28") is False
    assert validate_ip("192.168.1") is False
    assert validate_ip("192.168.001.1") is False
    assert validate_ip("192.168.1.999") is False
    assert validate_ip("not-an-ip") is False
    assert validate_ip(None) is False


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


# Test cases for the detection summary counts in the report
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
