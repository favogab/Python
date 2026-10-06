# -------------------- CS50P Week 3 Personal SOC Practice --------------------

# This script applies CS50P Week 3 concepts to a basic SOC login analysis.
# It analyzes multiple login events, assigns severity levels, summarizes
# the results, and identifies IP addresses that appear more than once.
# Error handling is included to manage invalid event data.

events = [
    {"user": "admin", "ip": "185.220.101.45", "failed": 12},
    {"user": "favour", "ip": "10.0.0.15", "failed": 2},
    {"user": "james", "ip": "91.210.15.8", "failed": 7},
    {"user": "admin", "ip": "185.220.101.45", "failed": 18},
    {"user": "sarah", "ip": "10.0.0.21", "failed": 1},

    # Invalid test events
    {"user": "peter", "ip": "192.168.1.50", "failed": "unknown"},
    {"user": "mary", "ip": "10.0.0.20"}
]

invalid_events = 0

for event in events:
    try:
        if event["failed"] >= 10:
            severity = "HIGH"
        elif event["failed"] >= 5:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        print(
            f"User: {event['user']}",
            f"IP: {event['ip']}",
            f"Failed Logins: {event['failed']}",
            f"Severity: {severity}",
            sep="\n"
        )
        print()

    except (TypeError, KeyError):
        invalid_events += 1
        print("Invalid event data - skipped")
        print()

valid_events = len(events) - invalid_events


# Count the total number of events only.

print(f"Total Events Received: {len(events)}")
print(f"Valid Events: {valid_events}")
print(f"Invalid Events: {invalid_events}")
print()

# Count how many events have a severity of HIGH, MEDIUM, and LOW.

total_high = 0
total_medium = 0
total_low = 0

for event in events:
    try:
        if event["failed"] >= 10:
            total_high += 1
        elif event["failed"] >= 5:
            total_medium += 1
        else:
            total_low += 1
    except (TypeError, KeyError):
        pass

print(f"Total HIGH Severity Events: {total_high}")
print(f"Total MEDIUM Severity Events: {total_medium}")
print(f"Total LOW Severity Events: {total_low}")
print()

## Detect IP addresses that appear in more than one event ##
ip_counts = {}

for event in events:
    ip = event["ip"]

    if ip in ip_counts:
        ip_counts[ip] += 1
    else:
        ip_counts[ip] = 1

for ip, count in ip_counts.items():
    if count > 1:
        print(f"Repeated IP: {ip}")
print()        