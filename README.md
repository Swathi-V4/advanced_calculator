# Advanced Calculator

## Overview

The Advanced Calculator is a modular command-line calculator application written in Python. It demonstrates professional software engineering practices by combining object-oriented programming, multiple design patterns, automated testing, persistent data storage, logging, and continuous integration.

The application allows users to perform mathematical calculations, maintain calculation history, undo and redo previous results, automatically save calculations, and configure application settings through environment variables.

---

## Features

### Basic Operations

- Addition
- Subtraction
- Multiplication
- Division

### Advanced Operations

- Power
- Root
- Modulus
- Integer Division
- Percentage
- Absolute Difference

### Command Line Interface

Available commands:

- help
- history
- clear
- undo
- redo
- save
- load
- exit

---

## Design Patterns

### Factory Pattern

The Factory pattern creates the appropriate operation object based on the user's selected operation.

### Strategy Pattern

Each mathematical operation is implemented as its own strategy class, making it easy to extend the calculator with additional operations.

### Facade Pattern

The Calculator class serves as a simplified interface that coordinates calculations, history management, observers, and other internal components.

### Observer Pattern

Observers automatically respond whenever a calculation is completed.

Current observers include:

- LoggingObserver
- AutoSaveObserver

### Memento Pattern

The Memento pattern stores previous calculation results and enables Undo and Redo functionality.

---

## Configuration

Application settings are stored in a `.env` file.

Example configuration:

```
CALCULATOR_LOG_DIR=.
CALCULATOR_HISTORY_DIR=.
CALCULATOR_LOG_FILE=calculator.log
CALCULATOR_HISTORY_FILE=calculator_history.csv
CALCULATOR_MAX_HISTORY_SIZE=100
CALCULATOR_AUTO_SAVE=true
CALCULATOR_PRECISION=2
CALCULATOR_MAX_INPUT_VALUE=1000000
CALCULATOR_DEFAULT_ENCODING=utf-8
```

---

## Logging

Every calculation is automatically written to:

```
calculator.log
```

The log records:

- operation
- input values
- result
- timestamp

---

## History

The calculator supports:

- automatic history tracking
- saving history to CSV
- loading history from CSV
- clearing history

---

## Running the Calculator

Start the application with:

```bash
python -m app.calculator_repl
```

---

## Running Tests

Execute all unit tests:

```bash
pytest
```

Generate coverage:

```bash
pytest --cov=app
```

---

## Technologies Used

- Python 3
- pandas
- pytest
- pytest-cov
- python-dotenv
- colorama
- Git
- GitHub Actions

---

## Project Structure

```
app/
    calculation.py
    calculator_config.py
    calculator_memento.py
    calculator_repl.py
    exceptions.py
    history.py
    input_validators.py
    logger.py
    operations.py

tests/
```

---

## Continuous Integration

GitHub Actions automatically:

- installs dependencies
- runs all unit tests
- checks code coverage

Every push to the repository is automatically tested.

---

## Author

Swathi Veerapalli

NJIT – IS 601