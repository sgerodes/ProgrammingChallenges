if __name__ == '__main__':
    N = int(input())
    list = []
for i in range(N):
    cmd = input().strip()
    if "insert" in cmd:
        command, p1, p2 = cmd.split(' ')
        list.insert(int(p1), int(p2))
    if "print" in cmd:
        print(list)
    if "remove" in cmd:
        command, p1 = cmd.split(' ')
        list.remove(int(p1))
    if "append" in cmd:
        command, p1 = cmd.split(' ')
        list.append(int(p1))
    if "sort" in cmd:
        list.sort()
    if "pop" in cmd:
        list.pop()
    if "reverse" in cmd:
        list.reverse()
