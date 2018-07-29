n = int(input().strip())
all_pairs = []
for a_i in range(n):
    pair = [int(a_temp) for a_temp in input().strip().split(' ')]
    all_pairs.append(pair)

for i in range(n):
    pair = all_pairs[i]
    print (str(2*pair[2]-pair[0]) + " " + str(2*pair[3]-pair[1]))