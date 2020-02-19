def factorial(n):
    if n == 1:
        return 1
    elif n > 1:
        result = n * factorial(n-1)
    return result

if __name__ == "__main__":
    print (factorial(4))