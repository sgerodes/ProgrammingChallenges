def firstDuplicate(array):
    num_set = set()
    for number in array:
        length=len(num_set)
        num_set.add(number)
        if length==len(num_set):
            return number
    return -1