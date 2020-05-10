if __name__ == "__main__":
    a_length = int(input())
    a = set(map(int, input().split()))
    b_length = int(input())
    b = set(map(int, input().split()))
    if a_length == len(a) and b_length == len(b):
        for i in sorted(a.symmetric_difference(b)):
            print(i, end="\n")
