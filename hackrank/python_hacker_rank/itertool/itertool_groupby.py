import itertools

if __name__ == "__main__":
    s = input().strip()
    print (*[(len(list(k)), int(i)) for i, k in itertools.groupby(s)])



