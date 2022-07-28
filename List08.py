def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    i = 0
    while i < 5:
        if list1[i] == 0:
            list1[i] = False
        elif list1[i] == 1:
            list1[i] = True
        i += 1
    return list1