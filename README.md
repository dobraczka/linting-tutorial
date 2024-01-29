# Writing good python code can be ruff

Linting tools can help you prevent bugs and programming or stylistic errors.
There is a variety of tools like [pylint](https://www.pylint.org/), [flake8](https://flake8.pycqa.org/en/latest/) or [pylama](https://github.com/klen/pylama).

In this tutorial we will use [ruff](https://docs.astral.sh/ruff/tutorial/)

## Prerequisites

You will only need your favorite way to edit python code, a command line and [ruff](https://docs.astral.sh/ruff/installation/).
My recommended way to install ruff is via [pipx](https://packaging.python.org/en/latest/guides/installing-stand-alone-command-line-tools/), because it is a stand-alone command line tool:

```
pipx install ruff
```

Pipx creates a virtual environment for each package to avoid dependency issues among your python standalone applications.

## Usage

The tutorial is split into several levels (inside the `ltut` folder), which introduce you to ruff and a family of linting rules.
Each level folder contains an `example.py` file. This file contains some issues, which you need to address.
The example stays the same throughout the tutorial and in each subsequent level the previous issues are fixed (i.e. `ltut/level_2/example.py` is the solution to `ltut/level_1/example.py` and so on).
In each level folder you will find a `README.md` with directions.

You should start by cloning this repository (or downloading it as .zip and unpacking it) and navigating to the respective directory:

```
git clone https://github.com/dobraczka/linting-tutorial.git
```

When you have done this head to [`ltut/level_1/README.md`](https://github.com/dobraczka/linting-tutorial/blob/main/ltut/level_1/README.md).

## Now what?

If you are finished you can either to some `mypy` example (e.g. [`ltut/mypy_1`](https://github.com/dobraczka/linting-tutorial/blob/main/ltut/mypy_1/README.md)) or head over to [What's next](https://github.com/dobraczka/linting-tutorial/blob/main/ltut/WhatsNext.md)
