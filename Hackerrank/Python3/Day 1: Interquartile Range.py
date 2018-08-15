# -----------------------
list_input = lambda: list(map(int, input().split()))
n, ol = input(), sorted(zip(list_input(), list_input()), key=lambda x: x[0])
s = [x for x, f in ol for _ in range(f)]
ls = len(s)
lower_half, upper_half = s[:ls // 2], s[ls // 2 + ls % 2:]
median = lambda l: l[len(l) // 2] if len(l) % 2 else (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2
print('%.1f' % (median(upper_half) - median(lower_half)))
# -------------------
N = int(input())
X = [int(num) for num in input().strip().split(' ')]
F = [int(num) for num in input().strip().split(' ')]
A = []
for i in range(N):
    x = X[i]
    f = F[i]
    for ff in range(f):
        A.append(x)
A.sort()


def middle(arr):
    n = int(len(arr) / 2)
    # print(arr,n,arr[n],sep='\n')
    if len(arr) % 2 == 1:
        return arr[n]
    else:
        return (arr[n] + arr[n - 1]) / 2


half = int(len(A) / 2)
L = A[:half]
if len(A) % 2 == 0:
    U = A[half:]
else:
    U = A[half + 1:]

# print (middle(U))
# print (middle(L))
# print (round(middle(U)-middle(L),1))
# print(A,L,U,sep="\n")
