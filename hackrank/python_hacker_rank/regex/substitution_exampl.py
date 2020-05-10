import re


def replace_fun(match):
    # print(match)
    if match.group() == '&&':
        return 'and'
    elif match.group() == '||':
        return 'or'
if __name__ == "__main__":
    n = int(input())
    data = [input() for i in range(n)]
    print(data)
    p = "(?<= )(&&|\|\|)(?= )"
    # important this i tried as  p = " && | \|\| " with space
    print(re.sub(p, replace_fun, '\n'.join(data)), end='\n')
