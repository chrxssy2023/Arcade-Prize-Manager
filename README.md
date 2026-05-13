# WGC Arcade Prize Manager
> Phase 1 / 3 — Author: Christina C

## Overview
`wgc_arcade_prize_manager.py` for phase 1, I am working on a "Prize Cabinet" database that allows staff for this instant the user to be able to view the stock, cost and name of the arcade prizes

## Project Structure
```text
Arcade-Prize-Manager/
├── README.md
└── wgc_arcade_prize_manager.py
```

## Requirements
- Create a system that stores the arcade’s inventory and allows a staff member to view it.

## How to Run
From the project root, run:

```bash
python3 wgc_arcade_prize_manager.py
```

## Usage Example

After the program starts, the menu looks like this:

```text
--- WGC Arcade Prize Manager ---

1. Prizes
2. Exit
Pick 1 or 2:
```

- Enter `1` and press Enter — displays the current prize table
- Enter `2` and press Enter — prints `Goodbye` and exits the program
- Enter anything else — prints an "invalid choice" message and waits for input again

Selecting `1` produces output similar to the following:

```text
PRIZES:
Name         | Cost   | Stock
--------------------------------
Teddy Bear   | 160    | 40
Fidget Toy   | 40     | 50
Bouncy Ball  | 5      | 100
Chocolate    | 45     | 75
Keychain     | 20     | 60
```

## About `ljust()`

`ljust()` is a built-in string method that left-justifies a string within a given width by padding spaces on the right. This helps keep my inventory table neat

```python
"apple".ljust(10) + "is my favorite fruit."
# -> "apple     is my favorite fruit."
```

Notes:
- ljust() only works on str() as the numbers must be wrapped with str() (e.g. `str(prize["Ticket Cost"]).ljust(6)`).
- If the string is already longer than `width`, it is returned unchanged.
- The last column in the table doesn't need `ljust()` since nothing follows it.
