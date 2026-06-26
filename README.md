# Simple Python Calculator

A simple Python program demonstrating basic arithmetic operations (addition, subtraction, and logarithms) and unit testing.

## Files

- [calculator.py](file:///Users/byungwoolee/mytestprogram/calculator.py): Contains the core logic and functions (`add`, `subtract`, `log`).
- [test_calculator.py](file:///Users/byungwoolee/mytestprogram/test_calculator.py): Contains unit tests for the functions in `calculator.py`.

## Features

- **Addition (`add`):** Adds two numbers.
- **Subtraction (`subtract`):** Subtracts one number from another.
- **Logarithm (`log`):** Calculates the logarithm of a number with an optional custom base (defaults to $e$, natural log). Raises a `ValueError` for non-positive values.

## Getting Started

### Prerequisites

Make sure you have Python 3 installed. You can check your Python version by running:

```bash
python3 --version
```

### Running the Program

To run the main program:

```bash
python3 calculator.py
```

### Running the Unit Tests

To run the unit tests:

```bash
python3 -m unittest test_calculator.py
```

