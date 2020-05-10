import re
if __name__ == "__main__":
    S = input()
    k = input()

    if 0 < len(S) < 100 and 0 < len(k) < len(S):
        pattern = re.compile(k)
        matching = pattern.search(S)

        if not matching:
            print((-1, -1))
        else:
            while matching:
                print((matching.start(), matching.end()-1))
                matching = pattern.search(S, matching.start()+1)
