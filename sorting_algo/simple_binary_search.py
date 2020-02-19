def binary_search(list, item):
    mid = len(list)//2
    found =  False

    if len(list)< 1:
        found = False
    elif list[mid] == item:
        found = True
    elif item > mid:
        found = binary_search(list[mid+1:], item)
    else:
        found = binary_search(list[:mid], item)

    return found

def binary_search_efficient(list, first, last, item):
    first = first
    last = last
    found = False

    if first <= last:
        mid = (first + last)// 2
        if list[mid] == item:
            found = True
        else:
            if list[mid] > item:
                last = mid -1
                found = binary_search_efficient(list,first, last, item)
            else:
                first = mid +1
                found = binary_search_efficient(list, first, last, item)
    return  found

if __name__ == "__main__":
    search_list = [1,2,3,4,5,6,7,8,9]
    first = 0
    last = len(search_list) - 1
    print (binary_search_efficient(search_list, first, last, 9))
    # print(binary_search(search_list, 11))
