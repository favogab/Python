
import json
import csv
from collections import Counter
from datetime import datetime
from pathlib import Path

# Classify the severity of failed login attempts based on the number of failures
def classify_severity(failed):
    if type(failed) is not int or failed < 0:
        raise ValueError("Invalid failed-login count")

    if failed >= 10:
        return "HIGH"
    elif failed >= 5:
        return "MEDIUM"
    else:
        return "LOW"

# Analyze a list of login events and return a summary report
def analyze_events(events):
    severity_counts = Counter()
    ip_counts = Counter()
    invalid_events = 0
    valid_events = []

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
            valid_events.append({
                "timestamp": timestamp,
                "user": user,
                "ip": ip,
                "failed": failed,
                "severity": severity
           })

            severity_counts[severity] += 1
            ip_counts[ip] += 1

        except (KeyError, TypeError, ValueError):
            invalid_events += 1

    return{
    "total": len(events),
    "valid": len(events) - invalid_events,
    "invalid": invalid_events,
    "severity": severity_counts,
    "ips": ip_counts,
    "valid_events": valid_events,
}


# Export valid events to a CSV file
def export_csv(valid_events, output_path):
    fieldnames = ["timestamp", "user", "ip", "failed", "severity"]

    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(valid_events)


# Main function to load events, analyze them, and print the report
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

    # Export valid events to a CSV file
    csv_path = Path(__file__).with_name("cleaned_events.csv")
    try:
        export_csv(report["valid_events"], csv_path)
    except OSError as error:
        raise SystemExit(f"Unable to export CSV: {error}")
    print(f"Cleaned CSV exported to: {csv_path.name}")

    # Export the summary report to a text file
    report_path = Path(__file__).with_name("soc_report.txt")
    try:
        export_report(report, report_path)
    except OSError as error:
        raise SystemExit(f"Unable to export SOC report: {error}")

    print(f"SOC report exported to: {report_path.name}")


# Print the summary report to the console
def export_report(report, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write("===== SOC SUMMARY =====\n")
        file.write(f"Total Events: {report['total']}\n")
        file.write(f"Valid Events: {report['valid']}\n")
        file.write(f"Invalid Events: {report['invalid']}\n")

        for severity in ["HIGH", "MEDIUM", "LOW"]:
            count = report["severity"].get(severity, 0)
            file.write(f"{severity} Severity: {count}\n")

        file.write("===== REPEATED IP ADDRESSES =====\n")

        repeated_found = False

        for ip, count in report["ips"].items():
            if count > 1:
                file.write(f"Repeated IP: {ip} ({count} events)\n")
                repeated_found = True

        if not repeated_found:
            file.write("No repeated IP addresses detected.\n")


if __name__ == "__main__":
    main()
