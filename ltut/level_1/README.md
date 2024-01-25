# Level 1

Welcome to your first level of the ruff tutorial 🧙 !

In the following the tutorial assumes you are inside the level's folder (in this case `ltut/level_1`) when running any commands.

## Ruff

Ruff has two commands you will use in this tutorial: `ruff format` and `ruff check`.
Open `ltut/level_1/example.py` in your favourite IDE/text editor.
Maybe you will already notice a bunch of issues with this little example.
If not, don't worry, this is what this tutorial wants to teach you!

Let's run the first command:

```
ruff check --select F,E example.py
```

This will run the ruff linter with the [Pyflakes](https://docs.astral.sh/ruff/rules/#pyflakes-f) and [Pycodestyle](https://docs.astral.sh/ruff/rules/#pycodestyle-e-w) rules, which will check your code against some rules of the [Python Style Guide](https://peps.python.org/pep-0008/) (a stylized guide for PEP 8 can be found [here](https://peps.python.org/pep-0008/)).

After running the command you will see, that the session failed.
This is intentional.
You will also see, that the errors ruff found, can be easily fixed.

You can run:

```
ruff check --fix --select F,E example.py
```

What changed? If you cloned the repository you can run:

```
git diff ltut/level_1/example.py
```

If you now run:

```
ruff check --select F,E example.py
```

You will see, that no errors are detected anymore.

## Formatting

Python gives you a lot of freedom w.r.t how you can format your code.
In order to avoid long discussions about code style you can simply enforce one.
A popular choice is [black](https://github.com/psf/black).
Ruff provides an incredibly fast [drop-in replacement](https://docs.astral.sh/ruff/formatter/) for black.

Run the following to see what changes the formatter would make:

```
ruff format --diff example.py
```

Having a consistent format enables you to focus on the more important aspects of programming.
After a while you will immediately notice if python code is not formatted accordingly!

Now let's format the code:

```
ruff format example.py
```

## Not everything can be automated

There are only some errors ruff can fix automatically.
Now you have to do the fixing yourself.
Run the following: 

```
ruff check --select F,E,N example.py
```

This will additionally check if your code violated the PEP8 naming conventions.

You can find the ruff rules [here](https://docs.astral.sh/ruff/rules/#pep8-naming-n).
The specific violation is found [here](https://docs.astral.sh/ruff/rules/invalid-function-name/). 

If you fixed the error(s) save the file and run

```
ruff check --select F,E,N example.py
```
again. Now there should be no errors. Congratulations! You finished the first level!
