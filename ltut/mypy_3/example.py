def add(x: int, y: int, as_str: bool = False):
    result = x + y
    if as_str:
        return str(result)
    return result
