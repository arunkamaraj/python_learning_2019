import collections

# 1. need to iter until all deque is processed
# 2.    find min in deque in both left and right
# 3.    if l is empty then insert min else check the min is less then or equal l[-1]
# 4.    if min is less then insert else NO and exit
# 5.    repeat the step 1
# 6. print YES


def validate_pilling_up(size):
    l = []
    valid = 'Yes'
    while len(size) > 0:
        min_size = size.popleft() if size[0] >= size[-1] else size.pop()
        if len(l) > 0:
            if l[-1] >= min_size:
                l.append(min_size)
            else:
                valid = 'No'
                break
        else:
            l.append(min_size)

    print(valid)

if __name__ == "__main__":
    testcase = int(input())
    for i in range(testcase):
        n = int(input())
        cube_size = collections.deque(map(int, input().strip().split()))
        validate_pilling_up(cube_size)

    # # c = collections.deque((4,3,2,1,3,4))
    # c = collections.deque((1,3,2))
    # validate_pilling_up(c)
