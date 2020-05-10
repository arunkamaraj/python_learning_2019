if __name__ == "__main__":
    n = input()
    # print(sorted(n, lambda x: -ord(x)))
    n = 'Sorting1234'
    lower= []
    upper=[]
    odd_num =[]
    even_num =[]
    for i in n:
        if i.islower():
            lower.append(i)
        elif i.isupper():
            upper.append(i)
        elif i.isdigit() and int(i) % 2 == 0:
            even_num.append(i)
        elif i.isdigit() and int(i) % 2 != 0:
            odd_num.append(i)

    print(''.join([*sorted(lower), *sorted(upper), *sorted(odd_num), *sorted(even_num)]))

    # myList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468"
    # print(*sorted(input(), key=myList.index), sep="")