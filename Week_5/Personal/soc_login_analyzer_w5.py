
import json
from collections import Counter
from datetime import datetime
from pathlib import Path


def classify_severity(failed):
    if type(failed) is not int or failed < 0:
        raise ValueError("Invalid failed-login count")

    if failed >= 10:
        return "HIGH"
    elif failed >= 5:
        return "MEDIUM"
    else:
        return "LOW"


def analyze_events(events):
    severity_counts = Counter()
    ip_counts = Counter()
    invalid_events = 0

    for event in events:
        try:
            user = event["user"]
            ip = event["ip"]
            failed = event["failed"]
            timestamp = event["timestamp"]

            if not isinstance(user, str) or not user.strip():
                raise ValueError

            if not isinstance(ip, str) or not ip.strip():
                raise ValueError

            datetime.fromisoformat(timestamp)
            severity = classify_severity(failed)

            severity_counts[severity] += 1
            ip_counts[ip] += 1

        except (KeyError, TypeError, ValueError):
            invalid_events += 1

    return {
        "total": len(events),
        "valid": len(events) - invalid_events,
        "invalid": invalid_events,
        "severity": severity_counts,
        "ips": ip_counts,
    }


def main():
    file_path = Path(__file__).with_name("login_events.json")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            events = json.load(file)
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"Unable to load events: {error}")

    if not isinstance(events, list):
        raise SystemExit("Invalid JSON: expected a list of events")

    report = analyze_events(events)

    print("===== SOC SUMMARY =====")
    print(f"Total Events: {report['total']}")
    print(f"Valid Events: {report['valid']}")
    print(f"Invalid Events: {report['invalid']}")

    for severity in ["HIGH", "MEDIUM", "LOW"]:
        print(f"{severity} Severity: {report['severity'][severity]}")

    print("===== REPEATED IP ADDRESSES =====")
    for ip, count in report["ips"].items():
        if count > 1:
            print(f"Repeated IP: {ip} ({count} events)")


if __name__ == "__main__":
    main()
