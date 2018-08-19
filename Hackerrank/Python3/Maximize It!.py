from itertools import product

# ------inputs----
K, M = input().strip().split(' ')
K, M = int(K), int(M)
lists = []
for _ in range(K):
    length, lst = input().strip().split(' ', 1)
    lst = [int(num) for num in lst.split(' ')]
    lists.append(lst)

# ------calculations
biggest = -M
perms = product(*lists)
for variant in perms:
    S = sum(map(lambda x: x ** 2, variant)) % M
    if S > biggest:
        biggest = S
print(biggest)
