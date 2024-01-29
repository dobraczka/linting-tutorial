# What's next?

## Integrate ruff into your IDE

It makes sense to see linting rule violations already while writing code, so you avoid to even introduce these issues into the code base.
Ruff can be easily integrated into your workflow this way. See [here](https://docs.astral.sh/ruff/integrations/).

## pyproject.toml

ruff [can be configured](https://docs.astral.sh/ruff/configuration/) in the [`pyproject.toml`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/).
This file is used by many packaging tools, linters and type checkers and can be the central configuration point for your project.
It serves to address with `setup.py` and Setuptools (see [PEP518](https://peps.python.org/pep-0518/)).
One python packing and dependency management tool that uses `pyproject.toml` is [poetry](https://python-poetry.org/docs/).

## Pre-commit hooks

Similar to avoiding rule violations by adding ruff to your IDE you can avoid to *commit* such issues.
This is where [pre-commit](https://pre-commit.com/) hooks come in. You can configure specific steps that run before your changes are committed.
You can for example run [ruff](https://docs.astral.sh/ruff/integrations/#pre-commit).
Other useful hooks include checking if you added large files or if any of your files contain merge-conflict strings.
An overview of the hooks can be found [here](https://pre-commit.com/hooks.html).
For reference, this is what is currently in my default pre-commit configuration:
```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: check-added-large-files
      - id: check-case-conflict
      - id: check-merge-conflict
      - id: check-symlinks
      - id: check-yaml
      - id: debug-statements
      - id: end-of-file-fixer
      - id: mixed-line-ending
      - id: requirements-txt-fixer
      - id: trailing-whitespace
  - repo: https://github.com/tox-dev/pyproject-fmt
    rev: "1.3.0"
    hooks:
      - id: pyproject-fmt
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.3
    hooks:
      - id: ruff
        args: ["--fix", "--show-fixes"]
      - id: ruff-format
```

## Type checking

The code you have seen today used type hints. Whether this is good or not is up for debate, there is even the idea that nowadays python is split into two languages [typed and untyped](https://threeofwands.com/python-is-two-languages-now-and-thats-actually-great/).
I think type hints are tremendously helpful to keep track of what you are doing and using a type checker can help you spot bugs.
Nowadays there are several type checkers around for python.
The most commonly used is [mypy](https://www.mypy-lang.org/) and they make a great case for static typing:

> **Compile-time type checking**
> 
>   Static typing makes it easier to find bugs with less debugging.
> 
> **Easier maintenance**
> 
>   Type declarations act as machine-checked documentation. Static typing makes your code easier to understand and easier to modify without introducing bugs.
> 
> **Grow your programs from dynamic to static typing**
> 
>   You can develop programs with dynamic typing and add static typing after your code has matured, or migrate existing Python code to static typing. 

There have been some [other contenders](https://www.infoworld.com/article/3575079/4-python-type-checkers-to-keep-your-code-clean.html) in the realm of type-checkers.

## Orchestration tools

Running linters, type checkers, tests and so on can be a cumbersome process. In order to simplify this you can use tools like [tox](https://tox.wiki/en/4.12.1/user_guide.html) or [nox](https://nox.thea.codes/en/stable/).
These tools can be used to install dependencies for specific tasks in isolated environments and run scripts for different python versions.
I prefer nox, because [it is more versatile](https://tox.wiki/en/4.12.1/index.html#useful-links) and I find the configuration slightly simpler.
I use this tool (among other things) to build docs, run ruff and mypy and to execute tests.

## That is a lot of stuff to set up each time...

To avoid configuring yourself to death each time you start a project you should take your time once and do it properly.
This is where [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/README.html) comes into play.
You can create templates from which you can initialise new projects. There are [a lot](https://github.com/audreyfeldroy/cookiecutter-pypackage) of templates out there.
And of course you can always adapt existing ones to your needs (for example as [I did](https://github.com/audreyfeldroy/cookiecutter-pypackage)).
If you create a lot of projects this way and change the template often you can use [cruft](https://cruft.github.io/cruft/) to keep the changes synched across projects.
