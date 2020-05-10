import re

if __name__ == "__main__":
    data = input()
    pattern = r"([A-Za-z0-9])\1+" # here the \1 is repetitive of group(1)
    l = re.search(pattern, data)
    print(l.group(1) if l else -1)