# Containers

Check the code with:

```
nox --no-install -rs check_mypy -- mypy_2
```

There are some important lessons hidden in the solution.

<details>
  <summary>Spoiler</summary>
  
    Use concrete types for function results and abstract types for arguments!
    We do not care, whether the values are a list or a set or something else
    as long as we can _iterate_ over it!
    However we are explicitly returning a list!
  
</details>
