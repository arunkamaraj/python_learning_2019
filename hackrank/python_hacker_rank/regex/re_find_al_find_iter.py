import re
# pattern = "[a-zA-z]([aeiouAEIOU]{2,})[a-zA-Z]"
pattern = "[qwrtypsdfghjklzxcvbnm]([aeiou]{2,})[qwrtypsdfghjklzxcvbnm]"

if __name__ == "__main__":
    # data = input()
    data = "rabcadeefoooooogyYhFjkIoomnpOeorteeeeet"
    # if 0 < len(data) < 100 and re.findall(pattern, data, flags =re.I):
    #     # print(*[i.group(1) for i in re.finditer(pattern, data)], sep='\n')
    #     print(*re.findall(pattern, data, flags =re.I), sep="\n")
    # else:
    #     print(-1)

    a = re.findall(pattern, data, flags =re.I)
    print('\n'.join(a or ['-1']))