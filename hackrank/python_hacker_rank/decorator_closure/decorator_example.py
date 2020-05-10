# def wrapper(f):
#     def fun(l):
#         new_list=[]
#         for i in l:
#             j = i[-10:]
#             new_list.append('+91 ' + j[:5] + ' ' + j[5:])
#         return f(new_list)
#     return fun

def wrapper(f):
    def phone(l):
        f(["+91 "+c[-10:-5]+" "+c[-5:] for c in l])
    return phone

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
