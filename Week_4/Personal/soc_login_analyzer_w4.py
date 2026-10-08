
import json
from collections import Counter
from datetime import datetime
from pathlib import Path

# Load simulated login events
file_path = Path(__file__).with_name("login_events.json")

try:
    with open(file_path, "r", encoding="utf-8") as file:
        events = json.load(file)
except (OSError, json.JSONDecodeError) as error:
    raise SystemExit(f"Unable to load events: {error}")

if not isinstance(events, list):
    raise SystemExit("Invalid JSON: expected a list of events")

# Counters
invalid_events = 0
severity_counts = Counter()
ip_counts = Counter()
valid_events = 0

print("===== SOC LOGIN ANALYSIS =====")
print()

for event in events:
    try:
        user = event["user"]
        ip = event["ip"]
        failed = event["failed"]
        timestamp = event["timestamp"]

        # Validate event fields
        if not isinstance(user, str) or not user.strip():
            raise ValueError

        if not isinstance(ip, str) or not ip.strip():
            raise ValueError

        if type(failed) is not int or failed < 0:
            raise ValueError

        event_time = datetime.fromisoformat(timestamp)

        # Classify severity
        if failed >= 10:
            severity = "HIGH"
        elif failed >= 5:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        # Count only validated events
        valid_events += 1
        severity_counts[severity] += 1
        ip_counts[ip] += 1

        print(f"User: {user}")
        print(f"IP: {ip}")
        print(f"Failed Logins: {failed}")
        print(f"Time: {event_time}")
        print(f"Severity: {severity}")
        print()

    except (KeyError, TypeError, ValueError):
        invalid_events += 1
        print("Invalid event data - skipped")
        print()

# Summary
print("===== SOC SUMMARY =====")
print(f"Total Events: {len(events)}")
print(f"Valid Events: {valid_events}")
print(f"Invalid Events: {invalid_events}")
print()

print(f"HIGH Severity: {severity_counts['HIGH']}")
print(f"MEDIUM Severity: {severity_counts['MEDIUM']}")
print(f"LOW Severity: {severity_counts['LOW']}")
print()

print("===== REPEATED IP ADDRESSES =====")

for ip, count in ip_counts.items():
    if count > 1:
        print(f"Repeated IP: {ip} ({count} events)")
