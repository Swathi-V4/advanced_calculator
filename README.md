# Advanced Calculator

## Overview

Advanced Calculator is a modular Python command-line calculator application that demonstrates object-oriented programming, design patterns, persistent data management with pandas, automated testing with pytest, and continuous integration using GitHub Actions.

The calculator supports advanced arithmetic operations, calculation history management, undo/redo functionality, configuration management using environment variables, and automated history persistence.

---

## Features

### Arithmetic Operations

* Addition
* Subtraction
* Multiplication
* Division
* Power
* Root

### Design Patterns

* Strategy Pattern
* Factory Pattern
* Observer Pattern
* Memento Pattern
* Facade Pattern

### History Management

* Stores calculation history using pandas DataFrames
* Save history to CSV files
* Load history from CSV files
* Clear history
* Auto-save support through observers

### User Commands

* help
* history
* clear
* undo
* redo
* save
* load
* exit

### Configuration Management

* Uses python-dotenv
* Loads settings from environment variables
* Validates configuration values

### Error Handling

* Division by zero protection
* Invalid operation handling
* Custom exceptions
* LBYL and EAFP programming techniques

---

## Project Structure

```text
advanced_calculator/
│
├── app/
│   ├── calculator_repl.py
│   ├── calculation.py
│   ├── calculator_config.py
│   ├── calculator_memento.py
│   ├── exceptions.py
│   ├── history.py
│   ├── input_validators.py
│   └── operations.py
│
├── tests/
│   ├── test_calculations.py
│   ├── test_calculator_repl.py
│   ├── test_calculator_config.py
│   ├── test_calculator_memento.py
│   ├── test_exceptions.py
│   ├── test_history.py
│   ├── test_input_validators.py
│   └── test_operations.py
│
├── .github/workflows/
├── README.md
└── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd advanced_calculator
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### macOS/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Calculator

Run the application:

```bash
python app/calculator_repl.py
```

---

## Running Tests

Execute all tests:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=app
```

---

## Continuous Integration

GitHub Actions automatically:

* Installs project dependencies
* Executes pytest test suites
* Measures test coverage
* Verifies code quality on every push and pull request

---

## Technologies Used

* Python
* pandas
* pytest
* pytest-cov
* python-dotenv
* Git
* GitHub Actions

---

## Learning Outcomes

This project demonstrates:

* Object-Oriented Programming (OOP)
* Design Pattern implementation
* Automated software testing
* Continuous Integration (CI)
* CSV data management using pandas
* Professional software development practices
