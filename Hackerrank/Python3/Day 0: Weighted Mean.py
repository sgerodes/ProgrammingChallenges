N = int(input())
X = [int(num) for num in input().strip().split()]
W = [int(num) for num in input().strip().split()]

# print(X,W,sep='\n')
w_mean = 0
for i in range(N):
    w_mean += X[i] * W[i]
# print(w_mean)
w_mean /= sum(W)
print(round(w_mean, 1))
