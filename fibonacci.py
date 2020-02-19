# fib series 0,1,1,2,3,5,8,13,21
# def fibonacci(n):
#
#     if n < 0:
#         print("invalid")
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         fib_no  = fibonacci(n-1) + fibonacci(n-2)
#         # print(fib_no)
#         return fib_no
#     # pass

def fibonacci(n, fib_array):

    if n < 0:
        print("invalid")

    fib_array[0] = 0
    fib_array[1] = 1

    for n in range(2,n):
        fib_no  = fib_array[n-1] + fib_array[n-2]
        fib_array[n] = fib_no
    print(fib_array)
    print(fib_array[n])
    # pass

if __name__ == '__main__':
    # print (fibonacci(9))
    fibonacci(9, [0]*9)
