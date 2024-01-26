# How to make a good comeback

This new rule will check for [problems in function returns](https://docs.astral.sh/ruff/rules/#flake8-return-ret).
Run the following command to see what is wrong with some of the return statements in the code:

```
ruff check --select RET example.py
```

This time ruff not only tells you the errors, but it also mentions some unsafe fixes.
You can see what they would do if you run:

```
ruff check --fix --unsafe-fixes --diff --select RET example.py
```
I don't think these fixes would be satisfactory.
<details>
  <summary>Here is a hint why</summary>
  
Look at the type hint for the return type of `regulate_voice`.
  
</details>

<details>
  <summary>Here is a follow-up hint</summary>
  
Implicit `Optional` is no [longer allowed](https://github.com/python/peps/pull/689).
We want to return a `str` type and not `None`.
  
</details>

When you addressed these issues (run the command again to see if everything was resolved) you can continue to `ltut/level_4`.
