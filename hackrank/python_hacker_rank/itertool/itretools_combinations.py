from itertools import combinations

if __name__ == "__main__":
    word, k = input().split()

    z = [combinations(sorted(word), i) for i in range(1, int(k)+1)]

    for i in z:
        for j in i:
            print(''.join(j))
