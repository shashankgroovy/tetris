# Project setup guide

## Requirements

- Python 3.11+

## Installation

#### Using make
The game doesn't need any requirements to run as such and can be directly
invoked using the `src/tetris.py` file but to generate a binary we need
`pyinstaller`. To install it, simply run:

```bash
make install
```

#### Via Pip
Make sure you are in a virtual environment and install all the required
dependencies in a virtual environment which are present in the
`requirements.txt` file.

```bash
pip install -r requirements.txt
```

Dev requirements for running tests can be installed using the
`dev-requirements.txt` file.

```bash
make install-dev
```
or,
```bash
pip install -r dev-requirements.txt
```

## Running the application

There are 2 ways to run the application which are listed below.

1. ### Using executable

   The `Makefile` generates a `tetris` executable file which can be directly
   invoked from command-line and is the recommended way to spin things up.

   Simply run:

   ```bash
   make
   ```

   Then use the `input.txt` file in the `tests/` folder to run a sample test.
   ```bash
   ./tetris < tests/input.txt > output.txt
   ```

   or, directly input (tetromino,position) data which can be read from STDIN as
   follows:

   ```bash
   ./tetris
   Q4
   2
   T1,I4,Z3
   3
   ```

2. ### Pythonic way

   Sometimes it's just easier and faster to run things using python
   interpreter. Simply run,

   ```bash
   python -m src
   ```

   or, provide an input file

   ```bash
   python -m src < tests/input.txt > output.txt
   ```


## Running Tests

Pytest is being used for testing making it easier to test.

Simply run:
```bash
make test
```
OR
```bash
python -m pytest
```
NOTE: Be sure to install the dependencies in `dev-requirements.txt`
