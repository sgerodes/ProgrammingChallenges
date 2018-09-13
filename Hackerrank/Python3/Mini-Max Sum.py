def miniMaxSum(arr):
    sorted_arr = sorted(arr)
    print(sum(sorted_arr[:4]), sum(sorted_arr[-4:]))
