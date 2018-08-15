def index_equals_value(arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        i = (start + end) // 2
        if arr[i] - i < 0:
            start = i + 1
        elif (arr[i] - i == 0) and ((i == 0) or (arr[i - 1] - (i - 1) < 0)):
            return i
        else:
            end = i - 1

    return -1
