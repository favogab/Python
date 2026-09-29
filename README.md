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

CS50P/
├── Week_0/
│   ├── indoor.py
│   ├── playback.py
│   ├── faces.py
│   ├── einstein.py
│   ├── tip.py
│   └── personal/
│       └── soc_triage.py
│
├── Week_1/
│   ├── Exercise/
│   │   ├── bank.py
│   │   ├── deep.py
│   │   ├── extensions.py
│   │   ├── interpreter.py
│   │   └── meal.py
│   └── personal/
│       └── ...
│
└── ...

## Personal Security Projects

### SOC Alert Triage

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

As I learn more Python, I plan to gradually improve these security-focused
scripts using concepts introduced later in the course.

## Running the Programs

Python 3 is required.

Clone the repository or open it locally, navigate to the appropriate
directory, and run a script with:

```bash
python filename.py
```

For example:

```bash
python soc_triage.py
```

## Goal

My goal is not only to complete CS50P, but to develop a strong Python
foundation that I can eventually apply to security operations, log analysis,
automation, APIs, data processing, and other cybersecurity workflows.

Rather than jumping directly into security-specific Python scripts, this
repository tracks the fundamentals first and shows how those skills develop
over time.

## Status

🚧 **In Progress**

Currently working through CS50P and expanding the personal security projects
as new Python concepts are introduced.
