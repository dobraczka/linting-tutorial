from typing import overload, Literal, Union

@overload
def add(x: int, y: int, as_str: Literal[False] = False) -> int:
    pass

@overload
def add(x: int, y: int, as_str: Literal[True]) -> str:
    pass

def add(x: int, y: int, as_str: bool = False) -> Union[int, str]:
    result = x + y
    if as_str:
        return str(result)
    return result

if __name__ == "__main__":
    x = add(2, 4)
    add(x, 5, as_str=True).startswith("1")
