import re

n = int(input())
for i in range(n):
    string = input()
    try:
        re.compile(string)
        is_valid = True
    except:
        is_valid = False
    finally:
        print(is_valid)
