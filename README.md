# CS50P – Python Learning & Security Projects

This repository documents my Python learning journey through Harvard's
CS50's Introduction to Programming with Python (CS50P).

Alongside the official course exercises and problem sets, I build small
personal projects that apply the Python concepts I learn to cybersecurity,
SOC analysis, and security automation.

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
- Course exercises
- Problem sets
- Coding practice

**Personal Projects**
- Small programs built independently
- Cybersecurity-focused exercises
- SOC and security automation experiments
- Projects that reinforce concepts learned during that week

Example structure:

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
└── ...
```

## Personal Security Projects

### Week 1 – SOC Alert Triage

One of my first personal Python exercises applies basic Python concepts to
a simple SOC alert-triage scenario.

The script collects:

- Username
- Source IP address
- Number of failed login attempts
- Whether a successful login followed the failures

It then uses conditional logic to classify the activity as:

- LOW
- MEDIUM
- HIGH
- CRITICAL

This project was built to reinforce:

- `input()`
- Variables
- Functions
- Integer conversion
- `if / elif / else`
- Boolean conditions
- Return values
- f-strings

### Week 2 – SOC Login Event Analyzer

The Week 2 personal project expands from analyzing a single user-provided
alert to processing multiple login events stored as structured data.

Each event contains:

- Username
- Source IP address
- Number of failed login attempts

The script:

- Iterates through multiple login events
- Classifies each event as LOW, MEDIUM, or HIGH severity
- Counts the total number of events
- Summarizes events by severity
- Identifies IP addresses that appear in more than one event

This project was built to reinforce:

- `for` loops
- Lists
- Dictionaries
- Lists of dictionaries
- `len()`
- Iteration
- Counters
- Conditional logic
- Dictionary membership
- Working with structured data

### Week 3 – Resilient SOC Login Event Analyzer

The Week 3 version introduces exception handling to make the login event
analyzer more resilient when processing malformed or incomplete event data.

The dataset intentionally includes invalid events, such as:

- A failed-login value containing text instead of a number
- An event missing the `failed` field entirely

Rather than allowing one malformed event to terminate the entire analysis,
the script catches the relevant exceptions, skips invalid events, and
continues processing the remaining data.

The analyzer also reports:

- Total events received
- Valid events
- Invalid events
- HIGH, MEDIUM, and LOW severity totals
- Repeated source IP addresses

This project was built to reinforce:

- `try`
- `except`
- `TypeError`
- `KeyError`
- Handling malformed data
- Skipping invalid records safely
- Combining exception handling with loops and dictionaries
- Keeping analysis running when individual records fail

The project intentionally uses concepts introduced up to the current CS50P
week rather than jumping ahead to more advanced Python techniques. This
allows the security scripts to develop alongside my progress through the
course.

## Running the Programs

Python 3 is required.

Clone the repository or open it locally, navigate to the appropriate
directory, and run a script with:

```bash
python filename.py
```

For example:

```bash
python soc_login_analyzer.py
```

## Goal

My goal is not only to complete CS50P, but to develop a strong Python
foundation that I can eventually apply to security operations, log analysis,
automation, APIs, data processing, and other cybersecurity workflows.

Rather than jumping directly into advanced security-specific Python scripts,
this repository tracks the fundamentals first and shows how those skills
develop over time.

## Status

🚧 **In Progress**

Completed coursework and personal practice through **CS50P Week 3**.

Current progression:

**Week 1:** Single-alert triage and classification  
**Week 2:** Multi-event analysis using loops and structured data  
**Week 3:** Exception handling and resilience against malformed event data

The personal security projects will continue to develop as new Python
concepts are introduced.