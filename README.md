# CS50P – Python Learning & Security Projects

This repository documents my Python learning journey through Harvard's **CS50's Introduction to Programming with Python (CS50P)**.

Alongside the official course exercises and problem sets, I build small personal projects that apply the Python concepts I learn to cybersecurity, Security Operations Center (SOC) analysis, and security automation.

My approach is to learn Python fundamentals progressively and apply each week's concepts to practical security scenarios.

## What I'm Learning

The course covers Python fundamentals including:

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

## Repository Structure

The repository is organized by course week.

Each week contains two types of work:

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
└── Week_5/
    ├── Exercise/
    │   ├── test_bank/
    │   ├── test_fuel/
    │   ├── test_plates/
    │   └── test_twttr/
    └── Personal/
        ├── login_events.json
        ├── soc_login_analyzer_w5.py
        └── test_soc_login_analyzer_w5.py
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

🚧 **In Progress**

Completed coursework and personal practice through **CS50P Week 5 – Unit Tests**.

**Current progression:**

- **Week 1:** Single-alert triage using functions and conditional logic
- **Week 2:** Multi-event analysis using loops, lists, and dictionaries
- **Week 3:** Exception handling and resilience against malformed event data
- **Week 4:** Library-enhanced SOC analysis using JSON, Counter, datetime, and structured event validation
- **Week 5:** Refactored SOC analyzer with automated `pytest` tests, boundary checks, and invalid-data validation

**Next:** CS50P Week 6 – File I/O.

The personal security projects will continue to evolve as new Python concepts are introduced, with an emphasis on learning the fundamentals, understanding the code, and applying programming skills to realistic cybersecurity scenarios.