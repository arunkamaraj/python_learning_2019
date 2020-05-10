
def loop_test(n):
    if (1<= n <=20):
        for i in range(n):
            print(i*i)
    else:
        print("Out of range")


if __name__ == '__main__':
    n = int(input())
    loop_test(n)