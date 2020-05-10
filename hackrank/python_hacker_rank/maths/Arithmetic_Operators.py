def ao(a, b):
    if isinstance(a, int) and isinstance(b, int) and a >= 1 and b >=1:
        print(a+b)
        print(a-b)
        print(a*b)
    else:
        print("Constrain error")

def division_opration(a,b):
    if isinstance(a, int) and isinstance(b, int) and a >= 1 and b >=1:
        print(a//b)
        print(a/b)
    else:
        print("Constrain error")

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    division_opration(a, b)
    # ao(a, b)