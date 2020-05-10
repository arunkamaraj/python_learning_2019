def exceute_commands(l, com):
    if 'insert' in com:
        cmd, pos, data = com.split()
        l.insert(int(pos), int(data))
    elif 'print' in com:
        print(l)
    elif 'remove' in com:
        cmd, data = com.split()
        l.remove(int(data))
    elif 'append' in com:
        cmd, data = com.split()
        l.append(int(data))
    elif 'sort' in com:
        l.sort()
    elif 'pop' in com:
        l.pop()
    elif 'revers' in com:
        l.reverse()


def simplicity(l, com):
    cmd, *args = com.split()

    if cmd != 'print':
        cmd = cmd + "(" + ",".join(args) + ")"
        eval(cmd)


if __name__ == "__main__":
    l = []
    n = int(input())
    commands = [input() for _ in range(n)]
    for com in commands:
        simplicity(l, com)
