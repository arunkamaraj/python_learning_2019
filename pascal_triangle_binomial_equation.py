#refer note


def pascal_trinagel(n):
    for line in range(n):
        for k in range(0,line+1):
            print (binomial_co_efficient(line,k)," ", end = "")
        print("\n")

def binomial_co_efficient(n,k):
    result = 1

    if k > n-k:
        k = n-k

    for j in range(k):
        result = result * (n - j)
        result = int(result / (j+1))

    return result


if __name__ == '__main__':
    pascal_trinagel(5)
    # print(binomial_co_efficient(5,3))
