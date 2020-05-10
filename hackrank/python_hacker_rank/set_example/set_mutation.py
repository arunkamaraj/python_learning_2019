if __name__ == "__main__":
    a = int(input())
    a_set = set(map(int, input().split()))
    n = int(input())
    for _ in range(n):
        cmd, arg = input().split()
        data_set = set(map(int, input().split()))

        cmd_to_exec = cmd + "(" + arg + ")"
        print("data_set." + cmd_to_exec)
        eval("data_set." + cmd_to_exec)
