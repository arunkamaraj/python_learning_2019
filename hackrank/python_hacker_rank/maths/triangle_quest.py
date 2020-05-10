# 1
# 121
# 12321
# 1234321
# 123454321


# for i in range(1 ,int(input())+1):
  # print(*range(1, i + 1),*range(i-1, 0, -1), sep='')
# for i in range(1, int(input()) + 1):
#     print(*(list(range(1, i + 1)) + list(range(i - 1, 0, -1))), sep='')

for i in range(1,int(input())+1) :
    print( ((10**i-1)//9)**2 )
