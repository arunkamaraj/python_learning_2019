from itertools import product

if __name__ == "__main__":
    k, m = list(map(int, input().strip().split()))

    if 1 <= k <=7 and 1 <= m <= 1000:
        all_list = [list(map(int, input().strip().split()))[1:] for _ in range(k)]
        maximize = max([sum(map(lambda x: x ** 2, i)) % m for i in product(*all_list)])
        print(maximize)




