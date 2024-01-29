# Intro to static typing

Here you will learn some basics on static typing and type checking with mypy.

In order to check the examples I have set up a [nox](https://nox.thea.codes/en/stable/) session.

You can install nox via:

```
pipx install nox
```

Run the checks with (from the base directory i.e. where the `noxfile.py` resides):

```
nox -rs check_mypy -- mypy_1
```

You can run subsequent checks with:

```
nox --no-install -rs check_mypy -- mypy_1
```

to avoid trying to reinstall. The `-r` flag re-uses the virtual environment, the `-s` flag tells nox to run run the `check_mypy` session.

This command will install the necessary dependencies and run:

```
ruff check --select ANN ltut/mypy_1/example.py
mypy ltut/mypy_1/solution.py
```

The ruff rule checks, whether there are type hints. Mypy would otherwise allow this code, because it does not force you to use type hints.

If you don't know how to fix this code have a look at the [cheat-sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html).
And if you still don't know what to do there is a `solution.py`
