T = int(input())
all_cubes = []
#---input
for _ in range(T):
    cubes_cnt = int(input())
    cubes_side_length = [int(l) for l in input().split(' ')]
    all_cubes.append(cubes_side_length)

#---logic
for cubes in all_cubes:
    pile = []
    for _ in range(len(cubes)):
        bigger_index = 0 if cubes[0] > cubes[-1] else -1
        cb = cubes.pop(bigger_index)
        if len(pile) != 0 and pile[-1] < cb:
            print ("No")
            break
        else:
            pile.append(cb)
    if len(cubes) == 0:
        print("Yes")



