from typing import Union

def add(x: int, y: int, as_str: bool = False) -> Union[int, str]:
    result = x + y
    if as_str:
        return str(result)
    return result
