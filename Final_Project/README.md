# SOC Login Analyzer

A Python-based security log analysis tool developed as my Harvard CS50P final learning project.

The application processes simulated authentication events, validates login records, identifies potentially suspicious activity, and generates structured reports for security investigation.

## Features

- **Login Event Validation:** Validates usernames, IPv4 addresses, failed-login counts, and timestamps.
- **Severity Classification:** Categorizes login events as LOW, MEDIUM, or HIGH based on failed-login attempts.
- **Sensitive Account Detection:** Identifies authentication activity involving privileged accounts such as `admin`, `administrator`, and `root`.
- **Repeated IP Analysis:** Tracks how frequently source IP addresses appear across valid login events.
- **Invalid Event Tracking:** Records the position and rejection reason for malformed login records.
- **CSV Export:** Exports validated events into a structured CSV file.
- **SOC Report Generation:** Creates a readable text report containing security findings and event statistics.
- **Command-Line Interface:** Supports custom input files and output directories.
- **Automated Testing:** Includes pytest tests for validation, analysis, reporting, and CLI behavior.

## Technologies

- Python 3
- Python standard library (`json`, `csv`, `argparse`, `collections`, `pathlib`, and others)
- pytest
- mypy

## Project Structure

```text
Final_Project/
├── project.py
├── test_project.py
├── login_events.json
├── requirements.txt
├── README.md
├── .gitignore
└── reports/                 # Generated locally
    ├── cleaned_login_events.csv
    └── soc_report.txt
```

## Installation

Clone the repository or download the project files.

Install the development dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the analyzer using the included sample dataset:

```bash
python project.py
```

Specify a custom JSON input file and output directory:

```bash
python project.py --input login_events.json --output reports
```

Display command-line help:

```bash
python project.py --help
```

## Input Format

The application accepts a JSON array of login event objects.

Example:

```json
[
  {
    "user": "admin",
    "ip": "192.0.2.10",
    "failed": 12,
    "timestamp": "2026-10-17T09:00:00"
  },
  {
    "user": "james",
    "ip": "192.0.2.20",
    "failed": 2,
    "timestamp": "2026-10-17T09:05:00"
  }
]
```

## Severity Classification

| Failed Login Attempts | Severity |
|---|---|
| 0–4 | LOW |
| 5–9 | MEDIUM |
| 10 or more | HIGH |

These thresholds are demonstration rules for this project, not universal SOC detection standards.

## Output

The analyzer generates two files:

**`cleaned_login_events.csv`**

Contains validated login events and their calculated severity and sensitive-account status.

**`soc_report.txt`**

Summarizes event counts, severity distribution, repeated IP addresses, sensitive-account activity, and invalid records with their rejection reasons.

## Testing

Run the automated test suite:

```bash
python -m pytest test_project.py -v
```

Check type annotations:

```bash
python -m mypy project.py
```

At the final documented development checkpoint, all 37 automated tests passed, with no mypy issues reported.

## Design and Limitations

The project uses object-oriented programming, helper functions, type annotations, comprehensions, generators, and exception handling.

It is designed for learning and analysis of simulated login records. It does not connect to a production SIEM, ingest live authentication streams, or independently confirm malicious activity.

Severity ratings are based on defined failed-login thresholds and should not be treated as definitive evidence of compromise.

## Future Improvements

- Support larger datasets through streaming processing.
- Introduce configurable detection thresholds.
- Add time-window correlation for repeated login failures.
- Support additional log formats.
- Integrate with SIEM or security monitoring platforms.

## Author

**Favour Gabriel (FavoGab)**

- GitHub: https://github.com/favogab
- Portfolio: https://favogab.com/
- LinkedIn: https://www.linkedin.com/in/favogab/

Developed as part of my practical Python learning journey through Harvard CS50P.