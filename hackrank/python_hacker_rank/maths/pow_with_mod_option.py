if __name__ == "__main__":
    a, b, c = [int(input()) for _ in range(3)]
    print(pow(a,b), pow(a,b,c), sep='\n')