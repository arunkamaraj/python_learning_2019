
def  do_left_rotation(array, rotate_delta):

    for _ in range(rotate_delta):
        start_ele = array.pop(0)
        array.append(start_ele)

    return array

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    print(*do_left_rotation(a, d))