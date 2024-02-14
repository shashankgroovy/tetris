# Tetris

A simple cli based Tetris game implemented in python that reads pieces from
STDIN and writes the final height of a board to STDOUT.

## Technical docs:

- [Installation](./docs/project-setup.md#installation)
- [Running the application](./docs/project-setup.md#running-the-application)
- [Running tests](./docs/project-setup.md#running-tests)
- [Problem Statement](./docs/problem.md)

## Quickstart

The entire game code is inside the `src` folder which makes it fairly easy to work with. Use the
following script to spin up the application.

To build a binary use the make command
```bash
make
```

To run, invoke the resulting binary file generated from the above make command
```bash
./tetris < tests/input.txt > output.txt
```

or, run using python
```bash
python -m src < tests/input.txt > output.txt
```

For more, read the [project setup guide](./docs/project-setup.md).

## Style Guide

Follows [Python style guide - PEP 8](https://www.python.org/dev/peps/pep-0008/)
and uses [Black](https://pypi.org/project/black/) as the code formatter.
