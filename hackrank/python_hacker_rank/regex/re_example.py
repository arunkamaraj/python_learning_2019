import re

if __name__ == "__main__":
    pattern = "(\+|\-)?\d*\.\d*"
    n = int(input())
    l = [True if re.fullmatch(pattern, input())!= None else False for i in range(n)]
    print(*l, sep='\n')
