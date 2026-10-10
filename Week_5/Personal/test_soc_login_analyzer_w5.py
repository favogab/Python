
import pytest

from soc_login_analyzer_w5 import classify_severity, analyze_events


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
