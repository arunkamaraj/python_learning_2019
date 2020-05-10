import re

if __name__ == "__main__":
    pattern = "#([0-9A-Fa-f]{3}){1,2}"
    aux=''
    data = '\n'.join(iter(input, aux))
    print(*re.findall(pattern, data), sep='\n')
