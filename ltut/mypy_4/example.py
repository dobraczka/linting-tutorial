def foo(my_dict, modifier: int = 1) -> int:
    if "key1" not in my_dict:
        return None
    val = my_dict.get("key1", 0)
    if not isinstance(val, (str, int)):
        raise ValueError("Only str or int allowed as values!")
    if isinstance(val, str):
        return val + str(modifier)
    return val - modifier
