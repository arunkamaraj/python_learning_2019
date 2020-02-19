def do_merge_sort(data, lb, ub):
    mid = (lb + ub )//2
    if lb < ub:
        do_merge_sort(data, lb, mid)
        do_merge_sort(data, mid+1, ub)
        print(data[lb:ub + 1])

    # print (data[lb:ub+1])

def do_merge_sort_try(data):
    if len(data) > 1:
        mid = len(data)//2
        left_side = data[:mid]
        right_side = data[mid:]

        do_merge_sort_try(left_side)
        do_merge_sort_try(right_side)
        merge_data(data, left_side, right_side)

    # print ("Final Output", data)

def merge_data(data, left_side, right_side):
    # print("data:", data, " left_side:", left_side, " right_side:", right_side)
    i= 0
    j= 0
    k= 0

    # comparing both side and move the pointer to corresponding side
    while i < len(left_side) and j < len(right_side):
        if left_side[i] < right_side[j]:
            data[k] = left_side[i]
            i+=1
        elif left_side[i] > right_side[j]:
            data[k] = right_side[j]
            j+=1
        k += 1

    # if left have remaining element
    while i < len(left_side):
        data[k] = left_side[i]
        i+=1
        k+=1

    # if right have remaining element
    while j < len(right_side):
        data[k] = right_side[j]
        j+=1
        k+=1

if __name__ == "__main__":
    data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    do_merge_sort_try(data)
    print ('-----------', data)

