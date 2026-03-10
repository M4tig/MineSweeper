# Minesweeper

My first university project — a Python implementation of the classic **Minesweeper** game.

This project was developed for the **Fundamentos da Programação** course and was one of my first bigger programming assignments, so the goal here is not to present some super polished production-ready code, but rather a project that helped me learn how to structure a non-trivial program and work with abstract data types in Python.

---

## About the Project

This is a command-line version of Minesweeper built in Python.

The game follows the classic rules:
- the board starts fully covered
- the player can **clear** or **mark** cells
- clearing a mine ends the game
- clearing safe cells reveals clues about neighboring mines
- if a cell has no neighboring mines, nearby cells are revealed automatically

Like many modern Minesweeper implementations, the **first move is always safe**, and mines are only placed after the player's first chosen coordinate. The project also uses a **pseudo-random generator** to place mines. fileciteturn3file0

---

## What I Implemented

The project was built around several **abstract data types (TADs)** required by the assignment:

- **Generator** — pseudo-random number generator based on `xorshift`
- **Coordinate** — board coordinates
- **Cell** (`parcela`) — board cell state and mine information
- **Field** (`campo`) — the full Minesweeper board

On top of these, the project includes:
- mine placement
- board clearing logic
- flag toggling
- neighboring mine counting
- turn handling
- full game execution

The assignment also required respecting **abstraction barriers**, so a big part of the challenge was not just making the game work, but organizing the logic cleanly around the required TADs. fileciteturn3file0

---

## Main Features

- Command-line Minesweeper game
- Safe first move
- Automatic mine placement after the first action
- Recursive/iterative reveal of empty neighboring cells
- Flagging and unflagging cells
- Pseudo-random mine generation
- Board display in text mode
- Win / loss detection

---

## Game Rules

The objective is to clear every non-mined cell without detonating a mine.

During the game:
- **L** clears a cell
- **M** marks or unmarks a cell with a flag

The board shows:
- covered cells
- flagged cells
- revealed cells
- clue numbers indicating how many neighboring cells contain mines

The game is won when all non-mined cells have been revealed. fileciteturn3file0

---

## Technical Context

This project was developed under some interesting constraints:

- everything had to be submitted in a **single `.py` file**
- no external modules were allowed, except for `reduce` from `functools`
- the project required careful separation between data abstraction and higher-level logic
- output formatting had to exactly match the specification for automatic grading fileciteturn3file0

Because of that, this project was a good exercise in:
- functional decomposition
- input/output handling
- game logic
- abstraction
- careful testing

---

## Running the Project

If your file is called `proj2.py`, you can run it with:

```bash
python3 proj2.py
```

Depending on how your version is structured, you may need to call the main function directly from an interactive Python session.

For example, the project statement defines a main function with the following signature:

```python
minas(c, l, n, d, s)
```

where:
- `c` is the last column
- `l` is the last row
- `n` is the number of mines
- `d` is the generator dimension
- `s` is the generator seed fileciteturn3file0

Example:

```python
minas('Z', 5, 6, 32, 2)
```

---

## What I Learned

Since this was one of my first projects, it was a very important step for me.

It helped me get more comfortable with:
- breaking a problem into smaller functions
- representing data cleanly
- thinking in terms of abstract data types
- writing game rules in code
- dealing with edge cases and validation

Looking back, it is definitely a beginner project, but it was also one of the projects that helped me build a stronger programming foundation.

---

## Notes

- This project was developed for the **2022/2023** edition of **Fundamentos da Programação**. fileciteturn3file0
- The original assignment was written in Portuguese.
- The implementation is text-based and focused on correctness according to the course specification.
- As an early academic project, the code may reflect the learning stage I was in at the time.

---

## Credits

This project was developed by [Martim Afonso](https://github.com/M4tig).
