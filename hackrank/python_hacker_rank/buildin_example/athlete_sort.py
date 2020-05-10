if __name__ == "__main__":
    N, M = list(map(int, input().strip().split()))
    data = [list(map(int, input().strip().split())) for i in range(N)]
    K = int(input())
    for i in sorted(data, key=lambda x: x[K]):
        print(*i)
