# Number Guessing Game

A simple command-line number guessing game written in Python. The computer picks a random number, you try to guess it, and the terminal shows the result in color.

## Table of Contents

- [Features](#features)
- [Preview](#preview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Limitations](#limitations)
- [License](#license)

## Features

- Randomly generated number for each round
- Simple, repeated guessing loop that keeps running until manually stopped
- Colored terminal output: green for a correct guess, red for an incorrect one
- Shows both the player's guess and the actual number after every round
- Built entirely on Python's standard library, no external dependencies required

## Preview

```
Enter a Number Between 1 to 10: 7
Please Try Again...
Your Choice: 7 And The Answer: 3

Enter a Number Between 1 to 10: 3
YOU WON!
Your Choice: 3 And The Answer: 3
```

In an actual terminal, "YOU WON!" is shown in green and "Please Try Again..." in red.

## Requirements

- Python 3.7 or newer
- A terminal that supports ANSI color codes (most modern terminals on Windows, macOS, and Linux do)
- No third-party packages are required; the script relies only on the `random` module from the standard library

## Installation

Clone the repository:

```bash
git clone https://github.com/HoneySpider/guess_the_number.git
cd guess_the_number
```

No further installation steps are needed since the script has no external dependencies.

## Usage

Run the script from the terminal:

```bash
python main.py
```

You will be prompted to enter a number between 1 and 10. After each guess, the result is shown along with the correct number, and a new round starts automatically.

To stop the game, close the terminal or press `Ctrl+C`.

## How It Works

1. **Random number generation** — On every round, `random.randrange(1, 10)` generates a new number for the player to guess against.
2. **Getting the guess** — The player's input is read with `input()` and converted to an integer with `int()`.
3. **Comparing results** — The guess is compared to the randomly generated number. If they match, a win message is printed; otherwise, a "try again" message is shown.
4. **Colored output** — ANSI escape codes (`\033[32m` for green, `\033[31m` for red, `\033[0m` to reset) are used to color the win and loss messages directly in the terminal.
5. **Looping** — The entire process is wrapped in a `while True` loop, so a new round begins immediately after each guess without needing to restart the script.

## Limitations

- The game currently has no way to exit gracefully from within the loop; it must be stopped externally with `Ctrl+C` or by closing the terminal.
- Entering a non-numeric value will cause the script to crash, since the input is converted directly with `int()` without validation.
- `random.randrange(1, 10)` generates numbers from 1 up to and including 9, so a guess of exactly 10 can never actually match the generated number, despite the prompt suggesting a range of 1 to 10.
- ANSI color codes may not render correctly in terminals that lack ANSI support, such as older Windows Command Prompt versions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
