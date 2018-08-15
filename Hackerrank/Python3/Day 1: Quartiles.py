def findQuartile(arr):
    if (len(arr) % 2 == 0):
        med = (arr[int(len(arr) / 2)] + arr[int(((len(arr)) / 2 - 1))]) / 2
    elif (len(arr) % 2 == 1):
        med = arr[int((len(arr) - 1) / 2)]
    return int(med)


n = int(input())
X = [int(x) for x in input().split(' ')]
X = sorted(X)
Q2 = findQuartile(X)
X_1, X_2 = [], []
for x in X:
    if (x < Q2):
        X_1.append(x)
    elif (x > Q2):
        X_2.append(x)
Q1 = findQuartile(X_1)
Q3 = findQuartile(X_2)
print(Q1, Q2, Q3, sep='\n')
