# PyO3 Demo

This project demonstrates how to create a Python module using Rust and PyO3.

## Setup

1. Install Rust (if not already installed):
   ```bash
   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
   ```

2. Install maturin (the build tool for PyO3):
   ```bash
   pip install maturin
   ```

## Build and Run

### Quick start (recommended):
```bash
./run.sh
```

### Manual build:
```bash
source venv/bin/activate
PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 maturin develop
python main.py
```

### Build a wheel:
```bash
source venv/bin/activate
PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 maturin build --release
```

> **Note**: The `PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1` flag is needed for Python 3.14 compatibility.

## What's Inside

- **Functions**: `add()` and `multiply()` - simple Rust functions callable from Python
- **Class**: `Calculator` - a Rust struct exposed as a Python class with methods

## Project Structure

- `Cargo.toml` - Rust package configuration with PyO3 dependency
- `src/lib.rs` - Rust code defining the Python module
- `main.py` - Python script demonstrating usage
- `pyproject.toml` - Python project configuration for maturin
