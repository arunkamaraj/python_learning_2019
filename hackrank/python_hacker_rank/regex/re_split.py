import re
if __name__ == "__main__":
    n = input()
    pattern = '[,.]+'
    p = re.split(pattern, n)
    print(p)
    print('\n'.join(p))
