# Isort your imports so you don't have to

Imports can get messy. Fortunately [isort](https://pycqa.github.io/isort/) can fix a lot of your problems for you!
And ruff makes this tool [easily available](https://docs.astral.sh/ruff/rules/#isort-i) for you:

```
ruff check --fix --select I example.py
```

# Let's make things a little easier

You might have noticed, that some code was added here. Using [flake-8-simplify](https://docs.astral.sh/ruff/rules/#flake8-simplify-sim) we can check what we can simplify here:

```
ruff check --select SIM ltut/level_5/example.py
```

The linting rules in `SIM` are a great way to improve your programming! 

When you are done, you can head over to [`ltut/level_6`](https://github.com/dobraczka/linting-tutorial/blob/main/ltut/level_6/README.md).
