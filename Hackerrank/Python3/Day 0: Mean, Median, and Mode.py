n = int(input().strip())
arr = [int(num) for num in input().strip().split(' ')]

mean = 0
for num in arr:
    mean += num
print(mean / n)
arr.sort()
nm = int((n - 1) / 2)
print((arr[nm] + arr[nm + 1]) / 2)

most_occurances = 0
mode_list = []
for num in arr:
    occ = arr.count(num)
    if occ == most_occurances:
        mode_list.append(num)
    elif occ > most_occurances:
        mode_list = []
        mode_list.append(num)
        most_occurances = occ
mode_list.sort()
print(mode_list[0])
