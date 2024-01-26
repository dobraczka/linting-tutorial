# Something lurks in the shadows

In many cases your IDE will already tell you about this, but you should not use variable names that [shadow Python builtins](https://docs.astral.sh/ruff/rules/#flake8-builtins-a)

To check for this run:

```
ruff check --select A example.py
```

# Keeping up with the Pythashians

Often we write code with support for a specific Python version in mind. When a Python version reaches it's [end of life](https://endoflife.date/python) (e.g. Python 3.8 in 8 months), we can upgrade our code.
You can see the rules [here](https://docs.astral.sh/ruff/rules/#pyupgrade-up).
To automatically check for possible upgrade opportunities run:

```
ruff check --select UP example.py
```

The targeted version was set in the `pyproject.toml` (Python 3.9).
Again you can automatically fix some issues.

When you addressed these issues run

```
ruff check --select N,E,B,RET,F,UP,A example.py
```

to see if all errors are fixed.

You can now continue to `ltut/level_5`.
