if __name__ == "__main__":
    n, m = list(map(int, input().strip().split()))
    array = list(map(int, input().strip().split()))[:n]
    A = set(map(int, input().strip().split()))
    B = set(map(int, input().strip().split()))

    print(sum([(i in A) - (i in B) for i in array]))

# True - True
# 0
# True - False
# 1
# False - True
