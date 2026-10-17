
import json
import csv
from collections import Counter
from datetime import datetime
from pathlib import Path
import re
from typing import Any
import argparse
from collections.abc import Iterator





def iter_high_severity(
    events: list[dict[str, Any]]
) -> Iterator[dict[str, Any]]:
    """Yield validated login events classified as HIGH severity."""
    for event in events:
        if event["severity"] == "HIGH":
            yield event


# Detection thresholds
HIGH_SEVERITY_THRESHOLD = 10
MEDIUM_SEVERITY_THRESHOLD = 5

# Accounts monitored for privileged login activity
SENSITIVE_ACCOUNTS = {"admin", "administrator", "root"}

# Report severity order
SEVERITY_LEVELS = ("HIGH", "MEDIUM", "LOW")


# Represent and validate a single login event
class LoginEvent:
    def __init__(self, user: str, ip: str, failed: int, timestamp: str) -> None:
        """Represent and validate an individual login event."""
        if not isinstance(user, str) or not user.strip():
            raise ValueError("Invalid username")

        # Reject malformed IPv4 addresses.
        if not validate_ip(ip):
            raise ValueError("Invalid IPv4 address")

        # Reuse our existing failed-login validation.
        classify_severity(failed)

        # Confirm that the timestamp can be parsed.
        try:
            datetime.fromisoformat(timestamp)
        except (TypeError, ValueError):
            raise ValueError("Invalid timestamp")

        self.user = user
        self.ip = ip
        self.failed = failed
        self.timestamp = timestamp

    @property
    def severity(self) -> str:
        return classify_severity(self.failed)

    @property
    def sensitive_account(self) -> bool:
        return detect_sensitive_account(self.user)

# Analyzer for processing login events and generating reports
class SOCAnalyzer:
    def __init__(self, events: list[dict[str, Any]]) -> None:
        """Analyze login events and summarize security findings."""
        self.events = events

    
    def analyze(self) -> dict[str, Any]:
        """Analyze login events and return a summary report."""
        severity_counts: Counter[str] = Counter()
        ip_counts: Counter[str] = Counter()
        invalid_events = 0
        invalid_event_details: list[dict[str, Any]] = []
        valid_events: list[dict[str, Any]] = []
        sensitive_count = 0
        sensitive_high_count = 0

        for event_number, event in enumerate(self.events, start=1):
            try:
                login = LoginEvent(
                    event["user"],
                    event["ip"],
                    event["failed"],
                    event["timestamp"]
                )

                severity = login.severity
                sensitive_account = login.sensitive_account

                if sensitive_account:
                    sensitive_count += 1

                    if severity == "HIGH":
                        sensitive_high_count += 1

                # Preserve the structure expected by our reports.
                valid_events.append({
                    "timestamp": login.timestamp,
                    "user": login.user,
                    "ip": login.ip,
                    "failed": login.failed,
                    "severity": severity,
                    "sensitive_account": sensitive_account,
                })

                severity_counts[severity] += 1
                ip_counts[login.ip] += 1

            except (KeyError, TypeError, ValueError) as error:
                invalid_events += 1

                invalid_event_details.append({
                    "event_number": event_number,
                    "reason": str(error),
                })

        
        sensitive_users = [ 
            event["user"] 
            for event in valid_events 
            if event["sensitive_account"]
        ]

        severity_summary = {
            level: severity_counts.get(level, 0)
            for level in SEVERITY_LEVELS
        }

        unique_sensitive_users = {
            user.lower()
            for user in sensitive_users
     }
    
        return {
            "total": len(self.events),
            "valid": len(valid_events),
            "invalid": invalid_events,
            "severity": severity_counts,
            "ips": ip_counts,
            "valid_events": valid_events,
            "sensitive_count": sensitive_count,
            "sensitive_high_count": sensitive_high_count,
            "sensitive_users": sensitive_users,
            "severity_summary": severity_summary,
            "unique_sensitive_users": sorted(unique_sensitive_users),
            "invalid_event_details": invalid_event_details,
        }

# Class for generating and exporting SOC reports in different formats
class SOCReport:
    
    def __init__(self, report: dict[str, Any]) -> None:
        """Export SOC analysis results to CSV and text files."""
        self.report = report

    
    def export_csv(self, output_path: Path) -> None:
        """Write validated login events to a CSV file."""
        fieldnames = [
            "timestamp",
            "user",
            "ip",
            "failed",
            "severity",
            "sensitive_account",
        ]

        with open(output_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.report["valid_events"])

    
    def export_text(self, output_path: Path) -> None:
        """Write a human-readable SOC investigation report."""
        report = self.report

        with open(output_path, "w", encoding="utf-8") as file:
            file.write("===== SOC SUMMARY =====\n")
            file.write(f"Total Events: {report['total']}\n")
            file.write(f"Valid Events: {report['valid']}\n")
            file.write(f"Invalid Events: {report['invalid']}\n")

            for severity in SEVERITY_LEVELS:
                count = report["severity"].get(severity, 0)
                file.write(f"{severity} Severity: {count}\n")

            file.write("\n===== REPEATED IP ADDRESSES =====\n")

            repeated_found = False

            for ip, count in report["ips"].items():
                if count > 1:
                    file.write(f"Repeated IP: {ip} ({count} events)\n")
                    repeated_found = True

            if not repeated_found:
                file.write("No repeated IP addresses detected.\n")

            file.write("\n===== SENSITIVE ACCOUNT FINDINGS =====\n")

            sensitive_found = False

            for event in report["valid_events"]:
                if event["sensitive_account"]:
                    file.write(
                        f"Account: {event['user']} | "
                        f"IP: {event['ip']} | "
                        f"Failed: {event['failed']} | "
                        f"Severity: {event['severity']}\n"
                    )
                    sensitive_found = True

            if not sensitive_found:
                file.write("No sensitive account activity detected.\n")

            # Write detection summary
            file.write("\n===== DETECTION SUMMARY =====\n")
            file.write(
                f"Sensitive Account Events: {report['sensitive_count']}\n"
            )
            file.write(
                f"HIGH Severity Sensitive Events: {report['sensitive_high_count']}\n"
            )
            file.write(
                f"Unique Sensitive Users: {len(report['unique_sensitive_users'])}\n"
            )
            if report['unique_sensitive_users']:
                file.write(
                    f"Sensitive Account Name: {', '.join(report['unique_sensitive_users'])}\n")
            else:
                file.write("Sensitive Account Name: None\n")    

            # Write invalid event details
            file.write("\n===== INVALID EVENT DETAILS =====\n")

            if report["invalid_event_details"]:
               for detail in report["invalid_event_details"]:
                   file.write(
                       f"Event #{detail['event_number']}: "
                       f"{detail['reason']}\n"
              )
            else:
                file.write("No invalid events detected.\n")
    




# Classify the severity of failed login attempts
def classify_severity(failed: int) -> str:
    """Classify a failed-login count as LOW, MEDIUM, or HIGH."""
    if type(failed) is not int or failed < 0:
        raise ValueError("Invalid failed-login count")

    if failed >= HIGH_SEVERITY_THRESHOLD:
        return "HIGH"
    elif failed >= MEDIUM_SEVERITY_THRESHOLD:
        return "MEDIUM"
    else:
        return "LOW"


# Validate an IPv4 address format
def validate_ip(ip: str) -> bool:
    """Return whether a value is a valid IPv4 address."""
    if not isinstance(ip, str):
        return False

    match = re.fullmatch(
        r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})",
        ip,
    )

    if not match:
        return False

    # Each octet must be within range and have no leading zeros.
    for octet in match.groups():
        if not 0 <= int(octet) <= 255:
            return False

        if len(octet) > 1 and octet.startswith("0"):
            return False

    return True

# Detect if a username is considered sensitive
def detect_sensitive_account(user: str) -> bool:
    """Check whether a username belongs to the privileged-account watchlist."""
    if not isinstance(user, str):
        return False

    return user.lower() in SENSITIVE_ACCOUNTS


# Analyze a list of login events and return a summary report
def analyze_events(events: list[dict[str, Any]]) -> dict[str, Any]:
    """Analyze login records using the SOCAnalyzer class."""
    analyzer = SOCAnalyzer(events)
    return analyzer.analyze()

# Export valid events to a CSV file
def export_csv(valid_events: list[dict[str, Any]], output_path: Path) -> None:
    """Export validated login events to a CSV file."""
    report = {"valid_events": valid_events}
    SOCReport(report).export_csv(output_path)

# Load events and coordinate analysis and exports

def main(argv: list[str] | None = None) -> None:
    """Load login events, analyze them, and export the results."""

    parser = argparse.ArgumentParser(
        description="Analyze login events and generate SOC reports."
    )

    parser.add_argument(
        "--input",
        type=Path,
        default=Path(__file__).with_name("login_events.json"),
        help="Path to the JSON file containing login events."
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).parent / "reports",
        help="Directory where reports will be saved."
    )

    args = parser.parse_args(argv)

    file_path = args.input
    output_dir = args.output
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
    except OSError as error:
        raise SystemExit(f"Unable to create output directory: {error}")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            events = json.load(file)
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"Unable to load events: {error}")

    if not isinstance(events, list):
        raise SystemExit("Invalid JSON: expected a list of events")

    # Analyze events once, then use the results for both exports.
    report = SOCAnalyzer(events).analyze()
    reporter = SOCReport(report)

    # Export valid events to a CSV file
    csv_path = output_dir / "cleaned_login_events.csv"
    try:
        reporter.export_csv(csv_path)
    except OSError as error:
        raise SystemExit(f"Unable to export CSV: {error}")
    print(f"Cleaned CSV exported to: {csv_path}")

    # Export the summary report to a text file
    report_path = output_dir / "soc_report.txt"
    try:
        reporter.export_text(report_path)
    except OSError as error:
        raise SystemExit(f"Unable to export SOC report: {error}")

    print(f"SOC report exported to: {report_path}")

# Export the SOC report to a text file
def export_report(report: dict[str, Any], output_path: Path) -> None:
    """Export analysis findings to a text report."""
    SOCReport(report).export_text(output_path)

if __name__ == "__main__":
    main()
