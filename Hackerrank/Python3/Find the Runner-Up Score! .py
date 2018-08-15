if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort()

    largest = arr[n - 1]
for i in reversed(range(n)):
    if arr[i] < largest:
        print(arr[i])
        break
