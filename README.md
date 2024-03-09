# Tetris

A simple cli based Tetris game engine implemented in python that reads pieces
from STDIN and writes the final height of a board to STDOUT.

## Technical docs:

- [Installation](./docs/project-setup.md#installation)
- [Running the application](./docs/project-setup.md#running-the-application)
- [Running tests](./docs/project-setup.md#running-tests)

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
## Problem statement

The engine should model a grid that pieces enter from top and come to rest at
the bottom, as if pulled down by gravity. Each piece is made up of four unit
squares.
No two unit squares can occupy the same space in the grid at the same time.

The pieces are rigid, and come to rest as soon as any part of a piece contacts
the bottom of the grid or any resting block. As in Tetris, whenever an entire
row of the grid is filled, it disappears, and any higher rows drop into the
vacated space without any change to the internal pattern of blocks in any row.

Your program must process a text file of lines each representing a sequence of
pieces entering the grid. For each line of the input file, your program should
output the resulting height of the remaining blocks within the grid.
The file denotes the different possible shapes by letter. The letters used are
Q, Z, S, T, I, L, and J. The shapes of the pieces they represent are shown in
the table below:

</td>
</tr>
</table>
<table>
  <tr>
    <td>Letter</td>
    <td>Q</td>
    <td>Z</td>
    <td>S</td>
    <td>T</td>
    <td>I</td>
    <td>L</td>
    <td>J</td>
  </tr>
  <tr>
    <td>Shape</td>
    <td>
      <pre>
##
##
      </pre>
    </td>
    <td>
      <pre>
##
 ##
      </pre>
    </td>
    <td>
      <pre>
 ##
##
      </pre>
    </td>
    <td>
      <pre>
###
 #
      </pre>
    </td>
    <td>
      <pre>
####
      </pre>
    </td>
    <td>
      <pre>
#
#
##
      </pre>
    </td>
    <td>
      <pre>
 #
 #
##
      </pre>
    </td>
  </tr>
</table>

Your program does not need to validate its input and can assume that there will
be no illegal characters
You do not have to account for shape rotation in your model. The pieces will
always have the orientations shown above.
Each line of the input file is a comma-separated list.
Each entry in the list is a single letter (from the set above) and a
single-digit integer. The integer represents the left-most column of the grid
that the shape occupies, starting from zero.
The grid of the game space is 10 units wide. For each line of the file, the
grid’s initial state is empty.

For example, if the input file consisted of the line “Q0” the corresponding
line in the output file would be “2”, since the block will drop to the bottom
of the initially empty grid and has height two.

## Examples

### Example 1

A line in the input file contains `I0,I4,Q8` resulting in the following
configuration:

```
  I0 │          │ I4  │          │ Q8  │          │
     │          │ ──► │          │ ──► │        ##│
     │####      │     │########  │     │##########│
     └──────────┘     └──────────┘     └──────────┘
      0123456789       0123456789       0123456789

```

The filled bottom row then disappears:

```
│          │
│          │
│        ##│
└──────────┘
 0123456789
```

Therefore, the output row for this sequence is “1”.

### Example 2

A line in the input file contains `T1,Z3,I4`.

```

     │          │       │          │       │    ####  │
  T1 │          │  Z3   │   ##     │  I4   │   ##     │
     │ ###      │  ──►  │ #####    │  ──►  │ #####    │
     │  #       │       │  #       │       │  #       │
     └──────────┘       └──────────┘       └──────────┘
      0123456789         0123456789         0123456789

```

No rows are filled, so the output for this sequence is “4”.

## Style Guide

Follows [Python style guide - PEP 8](https://www.python.org/dev/peps/pep-0008/)
and uses [Black](https://pypi.org/project/black/) as the code formatter.
