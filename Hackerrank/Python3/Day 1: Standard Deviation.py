import math

N = int(input().strip())
X = [int(num) for num in input().strip().split()]
X.sort()
mean = sum(X) / len(X)
std_deviation = 0
for num in X:
    std_deviation += (num - mean) ** 2
std_deviation = math.sqrt(std_deviation / N)

print(round(std_deviation, 1))
