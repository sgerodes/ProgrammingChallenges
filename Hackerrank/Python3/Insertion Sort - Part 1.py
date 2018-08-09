n = int(input().strip())
Arr = [int(a_temp) for a_temp in input().strip().split(' ')]
k = Arr[n-1]

token = True

for i in reversed(range(n-1)):
    if (Arr[i]>k):
        Arr[i+1] = Arr[i]
        print (*Arr)

    else:
        Arr[i+1]=k
        print (*Arr)
        break;
    if i == 0:
        Arr[i] = k
        print (*Arr)
