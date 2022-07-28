def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    c = 1
    i = 1
    while i < len(list1):
        if list1[i] == list1[i -1]:
            c += 1
    return c == len(list1)