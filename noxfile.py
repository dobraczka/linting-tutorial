import os

from nox import session

LEVEL_1_RULES = {"E", "F", "N"}
LEVEL_2_RULES = LEVEL_1_RULES.union({"B"})
LEVEL_3_RULES = LEVEL_2_RULES.union({"RET"})
LEVEL_4_RULES = LEVEL_3_RULES.union({"A", "UP"})
LEVEL_5_RULES = LEVEL_4_RULES.union({"I", "SIM"})
LEVEL_6_RULES = LEVEL_5_RULES.union({"PL"})

LEVEL_RULES = {
    "level_1": LEVEL_1_RULES,
    "level_2": LEVEL_2_RULES,
    "level_3": LEVEL_3_RULES,
    "level_4": LEVEL_4_RULES,
    "level_5": LEVEL_5_RULES,
    "level_6": LEVEL_6_RULES,
}


@session
def formatter(session):
    args = session.posargs or ["level_1"]
    for arg in args:
        if arg.startswith("level"):
            level = arg
    session.install(".")
    session.run("ruff", "format", os.path.join("ltut", level, "example.py"))


@session
def check(session):
    args = session.posargs or ["level_1"]
    fix = "--no-fix"
    for arg in args:
        if arg.startswith("fix"):
            fix = "--fix"
        elif arg.startswith("level"):
            level = arg
    rules = ",".join(LEVEL_RULES[level])
    session.install(".")
    session.run(
        "ruff",
        "check",
        fix,
        "--select",
        rules,
        os.path.join("ltut", level, "example.py"),
    )


@session
def check_subsequent(session):
    session.install(".")
    for level in range(1, 7):
        lev_string = f"level_{level}"
        lev_plus_string = f"level_{level+1}" if level < 6 else "level_6_solution"
        rules = ",".join(LEVEL_RULES[lev_string])
        session.run(
            "ruff",
            "check",
            "--select",
            rules,
            os.path.join("ltut", lev_plus_string, "example.py"),
        )

@session
def check_mypy(session):
    args = session.posargs or ["mypy_1"]
    for arg in args:
        if arg.startswith("mypy"):
            level = arg
    session.install(".")
    file_to_check = f"ltut/{level}/example.py"
    session.run("ruff", "check", "--select", "ANN", file_to_check)
    session.run("mypy", file_to_check)

@session
def check_mypy_solution(session):
    args = session.posargs or ["mypy_1"]
    for arg in args:
        if arg.startswith("mypy"):
            level = arg
    session.install(".")
    file_to_check = f"ltut/{level}/solution.py"
    session.run("ruff", "check", "--select", "ANN", file_to_check)
    session.run("mypy", file_to_check)
