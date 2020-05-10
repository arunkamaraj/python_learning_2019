import cmath
if __name__ == "__main__":
    com = complex(input())
    print(abs(com), cmath.phase(com), sep='\n')

