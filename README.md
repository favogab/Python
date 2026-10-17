# CS50P – Python Learning & Security Projects

This repository documents my completed learning journey through Harvard's **CS50's Introduction to Programming with Python (CS50P)**. It is a personal learning record, not a claim of a formal CS50P certificate.

Alongside the official course exercises and problem sets, I built small personal projects that apply the Python concepts I learn to cybersecurity, Security Operations Center (SOC) analysis, and security automation.

My approach was to learn Python fundamentals progressively and apply each week's concepts to practical security scenarios, culminating in a tested SOC Login Analyzer.

## What I Learned

Topics studied include:

- Variables and data types
- Functions and arguments
- String manipulation
- Conditionals and Boolean logic
- Loops
- Lists and dictionaries
- Exceptions
- Libraries
- Unit testing
- File I/O
- Regular expressions
- Object-oriented programming
- Constants, sets, comprehensions, unpacking, and generators
- Type annotations, docstrings, and static checking with mypy
- Command-line argument parsing with argparse

## Repository Structure

The repository is organized by course week, followed by a final project.

Course weeks include two types of work:

**CS50P Exercises**
- Official course exercises and problem sets
- Coding practice and problem-solving activities

**Personal Projects**
- Small programs developed alongside the course
- Cybersecurity-focused programming exercises
- SOC analysis and security automation experiments
- Projects that reinforce and extend concepts learned during each week

### Directory Structure

```text
CS50P/
├── Week_0/
│   ├── indoor.py
│   ├── playback.py
│   ├── faces.py
│   ├── einstein.py
│   └── tip.py
│
├── Week_1/
│   ├── Exercise/
│   │   ├── bank.py
│   │   ├── deep.py
│   │   ├── extensions.py
│   │   ├── interpreter.py
│   │   └── meal.py
│   └── Personal/
│       └── soc_triage.py
│
├── Week_2/
│   ├── Exercise/
│   │   ├── camel.py
│   │   ├── coke.py
│   │   ├── nutrition.py
│   │   ├── plates.py
│   │   └── twttr.py
│   └── Personal/
│       └── soc_login_analyzer.py
│
├── Week_3/
│   ├── Exercise/
│   │   ├── fuel.py
│   │   ├── grocery.py
│   │   ├── outdated.py
│   │   └── taqueria.py
│   └── Personal/
│       └── soc_login_analyzer.py
│
├── Week_4/
│   ├── Exercise/
│   │   ├── adieu.py
│   │   ├── bitcoin.py
│   │   ├── emojize.py
│   │   ├── figlet.py
│   │   ├── game.py
│   │   └── professor.py
│   └── Personal/
│       ├── login_events.json
│       └── soc_login_analyzer_w4.py
│
├── Week_5/
│   ├── Exercise/
│   │   ├── test_bank/
│   │   ├── test_fuel/
│   │   ├── test_plates/
│   │   └── test_twttr/
│   └── Personal/
│       ├── login_events.json
│       ├── soc_login_analyzer_w5.py
│       └── test_soc_login_analyzer_w5.py
│
├── Week_6/
│   ├── Exercise/
│   │   ├── lines.py
│   │   ├── pizza.py
│   │   ├── scourgify.py
│   │   └── shirt.py
│   └── Personal/
│       ├── login_events.json
│       ├── soc_login_analyzer_w6.py
│       ├── test_soc_login_analyzer_w6.py
│       ├── cleaned_events.csv
│       └── soc_report.txt
│
├── Week_7/
│   ├── Exercise/
│   │   ├── numb3rs.py
│   │   ├── test_numb3rs.py
│   │   ├── watch.py
│   │   ├── working.py
│   │   ├── test_working.py
│   │   ├── um.py
│   │   ├── test_um.py
│   │   └── response.py
│   └── Personal/
│       ├── login_events.json
│       ├── soc_login_analyzer_w7.py
│       ├── test_soc_login_analyzer_w7.py
│       ├── cleaned_events.csv
│       └── soc_report.txt
│
├── Week_8/
    ├── Exercise/
    │   ├── seasons.py
    │   ├── test_seasons.py
    │   ├── jar.py
    │   ├── test_jar.py
    │   ├── shirtificate.py
    │   └── shirtificate.png
    └── Personal/
        ├── login_events.json
        ├── soc_login_analyzer_w8.py
        ├── test_soc_login_analyzer_w8.py
        ├── cleaned_events.csv
        ├── Screenshot
        └── soc_report.txt
│
├── Week_9/                  # Et Cetera learning exercises
│
├── Final_Project/
│   ├── project.py
│   ├── test_project.py
│   ├── login_events.json
│   ├── requirements.txt
│   ├── README.md
│   └── reports/              # Generated locally; ignored by Git
│       ├── cleaned_login_events.csv
│       └── soc_report.txt
│
├── .gitignore
└── README.md
```

## Personal Security Projects

### Week 1 – SOC Alert Triage

My first personal Python security project applies basic programming concepts to a simple SOC alert-triage scenario.

The script collects:

- Username
- Source IP address
- Number of failed login attempts
- Whether a successful login followed the failures

It uses conditional logic to classify the activity into four severity levels:

- LOW
- MEDIUM
- HIGH
- CRITICAL

**Python concepts reinforced:**

- `input()`
- Variables and data types
- Functions and arguments
- Integer conversion
- `if / elif / else`
- Boolean conditions
- Return values
- f-strings

This project introduces the idea of translating simple security detection rules into Python logic.

### Week 2 – SOC Login Event Analyzer

The Week 2 project expands from analyzing a single alert to processing multiple login events stored as structured data.

Each event contains a username, source IP address, and number of failed login attempts.

**Features:**

- Iterates through multiple login events
- Classifies events as LOW, MEDIUM, or HIGH severity
- Counts the total number of events
- Summarizes events by severity
- Identifies IP addresses appearing in multiple events

**Python concepts reinforced:**

- `for` loops
- Lists and dictionaries
- Lists of dictionaries
- `len()`
- Iteration and manual counters
- Conditional logic
- Dictionary membership
- Working with structured data

This project demonstrates how loops and data structures can support basic security event analysis.

### Week 3 – Resilient SOC Login Event Analyzer

The Week 3 project improves the analyzer's resilience by introducing exception handling.

The dataset intentionally includes malformed or incomplete login events, including:

- Failed-login counts containing text instead of integers
- Events missing the required `failed` field

Rather than allowing one invalid event to terminate the entire analysis, the program catches relevant exceptions, skips malformed records, and continues processing.

**Features:**

- Classifies valid login events by severity
- Handles invalid event data using exception handling
- Counts total, valid, and invalid events
- Summarizes HIGH, MEDIUM, and LOW severity events
- Identifies repeated source IP addresses

**Python concepts reinforced:**

- `try` and `except`
- `TypeError`
- `KeyError`
- Handling malformed data
- Skipping invalid records
- Combining exceptions with loops and dictionaries
- Maintaining program execution when individual records fail

This project reinforces the importance of handling unexpected input in security analysis workflows.

### Week 4 – Library-Enhanced SOC Login Event Analyzer

The Week 4 project extends the previous analyzer by introducing Python libraries to simplify data processing, strengthen event validation, and incorporate timestamp information.

Instead of storing login events directly inside the Python script, the analyzer reads simulated security events from an external JSON file.

**Features:**

- Loads structured login events from `login_events.json`
- Checks required fields, nonempty usernames and IP strings, nonnegative integer failed-login counts, and parseable timestamps
- Classifies events into HIGH, MEDIUM, and LOW severity levels
- Skips malformed or incomplete events without terminating the analysis
- Uses `collections.Counter` to summarize severity levels and count source IP occurrences
- Uses `datetime` to parse event timestamps
- Identifies IP addresses appearing in multiple valid events
- Generates a summary of total, valid, and invalid events

**Python concepts reinforced:**

- Importing and using standard-library modules
- `json` for structured data
- `collections.Counter` for counting occurrences
- `datetime.fromisoformat()` for timestamp parsing
- `pathlib.Path` for file paths
- Combining libraries with loops, dictionaries, conditions, and exception handling

**Sample analysis results:**

| Metric | Result |
|---|---|
| Total events | 7 |
| Valid events | 5 |
| Invalid events | 2 |
| HIGH severity | 2 |
| MEDIUM severity | 1 |
| LOW severity | 2 |
| Repeated source IP | `185.220.101.45` (2 events) |

The project uses **simulated login data for educational purposes**. Severity classifications are based on failed-login thresholds and do not independently establish malicious activity.

The analyzer checks that an IP field contains a nonempty string; it does not yet perform full IPv4 or IPv6 address validation.

**Learning scope:**

The primary focus is CS50P Week 4 (Libraries). Reading JSON files also introduces a concept covered more thoroughly in Week 6 (File I/O).

The personal projects primarily reinforce concepts introduced up to the current CS50P week. Occasionally, a small concept from a later week is introduced when needed for a practical security workflow, with the intention of studying it more deeply when the course reaches that topic.

**Project files:**

- `Week_4/Personal/soc_login_analyzer_w4.py`
- `Week_4/Personal/login_events.json`

### Week 5 – Unit-Tested SOC Login Event Analyzer

The Week 5 project refactors the Week 4 analyzer into smaller, independently testable functions and introduces automated unit testing with `pytest`.

Instead of relying only on manual inspection of the analyzer's output, the project verifies expected behavior using repeatable tests.

**Features:**

- Uses `classify_severity(failed)` to assign LOW, MEDIUM, or HIGH severity based on failed-login counts
- Uses `analyze_events(events)` to validate simulated events, summarize severity levels, and count source IP occurrences
- Rejects invalid failed-login counts, including negative values and non-integer inputs
- Tests severity boundaries at 4/5 and 9/10 failed logins
- Tests event totals, valid and invalid records, severity counts, and repeated IP addresses
- Keeps the JSON dataset alongside the Week 5 script so the project runs independently of Week 4
- Uses `if __name__ == "__main__":` so importing the analyzer for tests does not execute its command-line workflow

**Python concepts reinforced:**

- Writing unit tests with `pytest`
- Using `assert` to verify expected results
- Using `pytest.raises()` to verify expected exceptions
- Testing boundary values and invalid inputs
- Refactoring code into functions with clear responsibilities
- Separating test data from external file dependencies

**Verified results:**

- `pytest`: **5 tests passed**
- Analyzer: **7 total events, 5 valid, 2 invalid**
- Severity: **2 HIGH, 1 MEDIUM, 2 LOW**
- Repeated source IP: `185.220.101.45` (**2 events**)

These results use simulated events and simple educational thresholds; they do not independently establish malicious activity.

**Project files:**

- `Week_5/Personal/soc_login_analyzer_w5.py`
- `Week_5/Personal/test_soc_login_analyzer_w5.py`
- `Week_5/Personal/login_events.json`

### Week 6 – SOC Log Cleaner & Report Exporter

The Week 6 project extends the unit-tested SOC login event analyzer with file-output capabilities. Instead of only displaying findings in the terminal, the analyzer now retains validated events, exports them as structured CSV data, and saves a human-readable investigation summary to a text file.

**Official CS50P File I/O exercises:**

- `lines.py` — counts executable lines in Python source files, excluding blank lines and full-line comments
- `pizza.py` — reads CSV menus and displays them as ASCII tables with `tabulate`
- `scourgify.py` — transforms and writes cleaned CSV records using `csv.DictReader` and `csv.DictWriter`
- `shirt.py` — processes image files using Pillow to resize, crop, overlay, and save images

All four official exercises passed `check50`.

**Personal project features:**

- Loads simulated login records from `login_events.json` without modifying the original dataset
- Validates required event fields, nonempty usernames and IP strings, nonnegative integer failed-login counts, and parseable timestamps
- Skips invalid events while continuing analysis of valid records
- Classifies valid events into LOW, MEDIUM, and HIGH severity using educational failed-login thresholds
- Counts event totals, severity distribution, and repeated source IP addresses
- Retains validated events with an additional `severity` field
- Exports validated records to `cleaned_events.csv` with the columns `timestamp`, `user`, `ip`, `failed`, and `severity`
- Saves event totals, severity counts, and repeated IP findings to `soc_report.txt`
- Handles input-loading and export errors, and uses script-relative paths for the project files
- Extends automated tests to cover both CSV and text-report exports

**Python concepts reinforced:**

- Reading and writing files with `with open(...)`
- `csv.DictWriter`, `writeheader()`, and `writerows()`
- Text-file output with `write()` and newline characters
- `pathlib.Path` for predictable input and output locations
- `try / except` for file-operation errors
- Reusing validated data across multiple output formats
- Testing generated files with `pytest` and its `tmp_path` fixture
- Understanding that CSV values are read back as strings

**Verified results:**

| Metric | Result |
|---|---|
| Total login events | 7 |
| Valid events exported | 5 |
| Invalid events skipped | 2 |
| HIGH severity | 2 |
| MEDIUM severity | 1 |
| LOW severity | 2 |
| Repeated source IP | `185.220.101.45` (2 events) |
| Automated tests | **7 passed** |

**Project files:**

- `Week_6/Personal/soc_login_analyzer_w6.py` — event validation, analysis, and report exports
- `Week_6/Personal/test_soc_login_analyzer_w6.py` — seven automated tests
- `Week_6/Personal/login_events.json` — simulated input events
- `Week_6/Personal/cleaned_events.csv` — generated validated event records
- `Week_6/Personal/soc_report.txt` — generated SOC summary report

The dataset is simulated, and the severity thresholds are educational heuristics. Repeated IPs and failed-login counts are investigation signals, not proof of malicious activity. The analyzer does not yet perform comprehensive IP address validation or full threat detection.

### Week 7 – SOC Log Pattern Detector

Week 7 introduces regular expressions for recognizing structured text and adds pattern-based checks to the existing SOC login analyzer. The project continues to use simulated login events and preserves the JSON input, severity classification, CSV export, and text reporting workflow.

**Official CS50P Regular Expressions exercises:**

- `numb3rs.py` and `test_numb3rs.py` — validate IPv4 address structure, octet ranges, and leading-zero rules, with unit tests
- `watch.py` — extract a YouTube video ID from an HTML iframe embed URL and construct a short shareable link
- `working.py` and `test_working.py` — validate and convert 12-hour time ranges into 24-hour notation, with unit tests
- `um.py` and `test_um.py` — count standalone occurrences of “um” using word boundaries and case-insensitive matching
- `response.py` — validate email syntax with a third-party validation library instead of writing a custom regex

All five official exercises were completed, as reported during the learning session.

**Personal project features:**

- Validates IPv4 addresses using `re.fullmatch()` and checks each octet is between 0 and 255 without leading zeros
- Rejects login events with malformed IPv4 addresses while continuing to process valid records
- Uses a case-insensitive regex watchlist to identify the exact usernames `admin`, `administrator`, and `root`
- Adds a `sensitive_account` Boolean to each validated event and exports it in the cleaned CSV
- Counts watchlist-matching events and the subset classified as HIGH severity
- Includes a detection summary and individual sensitive-account findings in the saved text report
- Retains severity counts, repeated IP reporting, and the original event-processing behavior

**Python concepts reinforced:**

- Raw-string regular expressions and `re.fullmatch()`
- Capturing groups and match results
- Alternation (`|`) and `re.IGNORECASE`
- Separating format validation, watchlist matching, and severity classification
- Extending existing functions and CSV schemas without breaking prior behavior
- Regression testing with `pytest`, including valid, invalid, and edge-case inputs

**Verified results (simulated dataset):**

| Metric | Result |
|---|---|
| Total login events | 7 |
| Valid events | 5 |
| Invalid events | 2 |
| HIGH / MEDIUM / LOW | 2 / 1 / 2 |
| Repeated source IP | `185.220.101.45` (2 events) |
| Sensitive-account events | 2 |
| HIGH-severity sensitive-account events | 2 |
| Automated tests | **16 passed** |

**Project files:**

- `Week_7/Personal/soc_login_analyzer_w7.py` — event validation, regex watchlist detection, and exports
- `Week_7/Personal/test_soc_login_analyzer_w7.py` — sixteen automated tests
- `Week_7/Personal/login_events.json` — simulated input data
- `Week_7/Personal/cleaned_events.csv` — validated records and sensitive-account flags
- `Week_7/Personal/soc_report.txt` — summary, repeated IPs, detection counts, and findings

**Detection limitations:** The username watchlist is deliberately small and educational. A watchlist match or repeated source IP is an investigation lead, not proof of compromise. Counts represent events, not unique accounts or confirmed incidents. The IP validator checks IPv4 syntax only; it does not assess IP reputation or validate IPv6 addresses.

### Week 8 – Object-Oriented SOC Login Analyzer

Week 8 focuses on object-oriented programming (OOP). The personal project refactors the existing SOC login analyzer into cooperating classes, preserving the previous validation, detection, CSV export, and text-report functionality. This is primarily an architectural improvement rather than a new detection feature.

**Official CS50P Object-Oriented Programming exercises:**

- `seasons.py` and `test_seasons.py` — use `datetime.date` objects and date subtraction to calculate age in minutes, converting the result into English words with `inflect`
- `jar.py` and `test_jar.py` — implement a `Jar` class with initialization, string representation, deposit/withdraw methods, capacity and size properties, and validation
- `shirtificate.py` — use the `FPDF` class from `fpdf2` to generate a personalized A4 PDF with the CS50 shirt image and a name overlay

All three official exercises were completed during the learning session.

**Personal project architecture:**

| Component | Responsibility |
|---|---|
| `LoginEvent` | Validates a single event's username, IPv4 address, failed-login count, and timestamp; exposes severity and sensitive-account properties |
| `SOCAnalyzer` | Processes event records, skips invalid entries, counts severities and repeated IPs, and summarizes sensitive-account findings |
| `SOCReport` | Exports validated records to CSV and writes a readable text investigation report |

The original `analyze_events()`, `export_csv()`, and `export_report()` functions remain as compatibility wrappers, while `main()` uses the classes directly. The text report now includes blank lines between sections for easier reading.

**Python concepts reinforced:**

- Classes, instances, `__init__`, instance attributes, and methods
- `@property` for computed attributes
- Encapsulation through validation at object creation
- Composition: `SOCAnalyzer` uses `LoginEvent` objects
- Separation of concerns across analysis and reporting
- Refactoring with regression tests and backwards-compatible interfaces
- Testing object behavior, independent instances, invalid input, empty datasets, and generated files

**Reported results (simulated dataset):**

| Metric | Result |
|---|---|
| Total login events | 7 |
| Valid / invalid events | 5 / 2 |
| HIGH / MEDIUM / LOW | 2 / 1 / 2 |
| Repeated source IP | `185.220.101.45` (2 events) |
| Sensitive-account events | 2 |
| HIGH-severity sensitive-account events | 2 |
| Automated tests | **30 passed** |

**Project files:**

- `Week_8/Personal/soc_login_analyzer_w8.py` — OOP analyzer, reporting, and command-line workflow
- `Week_8/Personal/test_soc_login_analyzer_w8.py` — 30 automated tests
- `Week_8/Personal/login_events.json` — simulated input records
- `Week_8/Personal/cleaned_events.csv` — generated validated events
- `Week_8/Personal/soc_report.txt` — generated human-readable findings

**Limitations:** This is an educational analyzer using simulated records and simple failed-login thresholds. Its username watchlist is limited to `admin`, `administrator`, and `root`. Findings are investigation leads, not confirmed incidents. IPv4 validation does not provide reputation assessment or IPv6 support. `LoginEvent` validates values during initialization, but its attributes are not immutable afterward.

### Week 9 – Python Et Cetera and Analyzer Refinements

Week 9 consolidates advanced Python language features and developer tooling. I applied these concepts to the evolving SOC analyzer rather than introducing unrelated features purely for demonstration.

**Concepts practiced:**

- Named constants and sets for detection thresholds and sensitive-account usernames
- Type hints for functions and methods, checked with `mypy`
- Docstrings to document the purpose of classes, functions, and methods
- `argparse` for `--input` and `--output` command-line options
- Unpacking, list/dictionary/set comprehensions, and `enumerate()`
- Generator functions using `yield` and iterator annotations
- Additional pytest coverage for CLI behavior, summaries, invalid records, and generator filtering

The final project incorporates the Week 9 refinements. These improvements retain the earlier validation and detection workflow while making the analyzer easier to run, inspect, and test.

### Final Project – SOC Login Analyzer

The final learning project brings together the Python skills developed throughout CS50P into a command-line tool for examining **simulated authentication records**.

**Architecture:**

| Component | Responsibility |
|---|---|
| `LoginEvent` | Validates individual records and exposes computed severity and sensitive-account status |
| `SOCAnalyzer` | Processes valid and invalid events; summarizes severity, IP occurrences, and sensitive-account activity |
| `SOCReport` | Exports cleaned CSV records and a readable SOC investigation report |
| `main()` | Parses CLI options, loads JSON, runs analysis, and writes output files |

**Capabilities:**

- Validate usernames, IPv4 addresses, failed-login counts, and ISO-format timestamps
- Classify login events as LOW (0–4 failures), MEDIUM (5–9), or HIGH (10+)
- Identify events involving `admin`, `administrator`, and `root`
- Summarize repeated source IPs, sensitive-account events, and unique sensitive usernames
- Preserve invalid-event numbers and error reasons without stopping processing
- Export `cleaned_login_events.csv` and `soc_report.txt` to an output directory
- Accept custom JSON inputs and report destinations through `argparse`
- Provide a high-severity iterator using `yield`

**Final verified development checkpoint:** **37 pytest tests passed; mypy reported zero issues**. The expanded simulated dataset contains 62 records, including eight intentionally invalid events. These checks demonstrate the tested behavior of the project, not production SOC detection accuracy.

**Project files:** `Final_Project/project.py`, `Final_Project/test_project.py`, `Final_Project/login_events.json`, `Final_Project/requirements.txt`, and `Final_Project/README.md`.

**Scope and limitations:** This is a learning project using synthetic data and educational severity thresholds. IP repetition and privileged-account activity are leads for review, not proof of compromise. The analyzer is not connected to a live SIEM and does not assess IP reputation or support IPv6.

## Running the Programs

Python 3 is required.

Clone the repository or open it locally, navigate to the appropriate directory, and run a Python script using:

```bash
python filename.py
```

For example, to run the Week 4 SOC Login Event Analyzer from the repository root:

```bash
cd Week_4/Personal
python soc_login_analyzer_w4.py
```

The analyzer reads simulated login events from `login_events.json`, which is included in the same directory.

To run the Week 5 analyzer and its unit tests from the repository root:

```bash
cd Week_5/Personal
python soc_login_analyzer_w5.py
python -m pytest test_soc_login_analyzer_w5.py -v
```

The Week 5 unit tests require `pytest` (`python -m pip install pytest`).

To run the Week 6 SOC Log Cleaner & Report Exporter from the repository root:

```bash
cd Week_6/Personal
python soc_login_analyzer_w6.py
python -m pytest test_soc_login_analyzer_w6.py -v
```

The script reads `login_events.json` and writes `cleaned_events.csv` and `soc_report.txt` to the same project directory. The seven automated tests require `pytest` (`python -m pip install pytest`). The output files are regenerated when the analyzer runs.

To run the Week 7 SOC Log Pattern Detector and its tests from the repository root:

```bash
cd Week_7/Personal
python soc_login_analyzer_w7.py
python -m pytest test_soc_login_analyzer_w7.py -v
```

The script reads `login_events.json` and regenerates `cleaned_events.csv` and `soc_report.txt`. The 16 automated tests require `pytest`. The official Week 7 `response.py` exercise additionally uses a third-party email validation package such as `validator-collection`.

To run the Week 8 object-oriented analyzer and its tests from the repository root:

```bash
cd Week_8/Personal
python soc_login_analyzer_w8.py
python -m pytest test_soc_login_analyzer_w8.py -v
```

The script reads `login_events.json` and regenerates `cleaned_events.csv` and `soc_report.txt`. The Week 8 test suite contains 30 tests. The official Week 8 exercises use `inflect` (`seasons.py`) and `fpdf2` (`shirtificate.py`), in addition to Python's standard library.

### Run the Final Project

From the repository root:

```bash
cd Final_Project
python -m pip install -r requirements.txt
python project.py
```

Use a specific input and output folder:

```bash
python project.py --input login_events.json --output reports
```

See available options, run the automated tests, and check types:

```bash
python project.py --help
python -m pytest test_project.py -v
python -m mypy project.py
```

The application creates its output directory and generates `cleaned_login_events.csv` and `soc_report.txt`. The generated `reports/` directory and Python/test caches are excluded from version control through `.gitignore`. For detailed usage and architecture, see [`Final_Project/README.md`](Final_Project/README.md).

### Dependencies and API Security

Most personal projects use Python's standard library.

Some official CS50P exercises require additional third-party packages, including `requests`, `emoji`, `pyfiglet`, and `inflect`.

The Week 4 Bitcoin exercise uses the CoinCap API to retrieve Bitcoin prices.

For security reasons:

- API keys are not hardcoded into the Python source code.
- The CoinCap API key is read from the `COINCAP_API_KEY` environment variable.
- Actual API credentials are not included in the repository.
- Sensitive credentials and local environment configuration files should not be committed to version control.

The Bitcoin exercise can be run after installing `requests`, configuring the API key, and supplying a Bitcoin quantity:

```bash
python bitcoin.py 2.5
```

This exercise introduces API requests, JSON responses, command-line arguments, and currency formatting.

## Goal

My goal is not only to complete CS50P, but to develop a strong Python foundation that I can eventually apply to:

- Security operations and SOC workflows
- Security log analysis
- Threat detection and event triage
- Security automation
- API integration
- Structured data processing
- Building reliable and maintainable Python tools

Rather than jumping directly into advanced security-specific Python scripts, this repository tracks my progress through the fundamentals and demonstrates how those skills develop over time.

Each personal project builds on earlier work, gradually introducing new programming concepts and practical security use cases.

## Status

✅ **CS50P learning journey completed — Weeks 0–9 and personal final project.**

This repository documents self-directed completion of the lessons, exercises, and accompanying security-focused projects. It does **not** represent a formal CS50P certificate or a claim that the final project was submitted for certification.

**Learning progression:**

- **Week 0:** Functions, variables, and foundational Python exercises
- **Week 1:** Single-alert triage using functions and conditional logic
- **Week 2:** Multi-event analysis using loops, lists, and dictionaries
- **Week 3:** Exception handling and resilience against malformed event data
- **Week 4:** Library-enhanced SOC analysis using JSON, Counter, datetime, and event validation
- **Week 5:** Refactored analyzer with pytest tests and boundary checks
- **Week 6:** File-based event cleaning, CSV export, and saved investigation reports
- **Week 7:** Regex-based IPv4 validation and sensitive-account detection
- **Week 8:** Object-oriented design using `LoginEvent`, `SOCAnalyzer`, and `SOCReport`; 30 tests passed
- **Week 9:** Constants, typing, docstrings, CLI arguments, comprehensions, enumeration, and generators
- **Final Project:** Integrated SOC Login Analyzer with **37 passing tests** and **zero mypy issues** at the final verified checkpoint

**Next chapter:** Apply this Python foundation to independent projects, security tooling, and practical automation beyond the CS50P course.
