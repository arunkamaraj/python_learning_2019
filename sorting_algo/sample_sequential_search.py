def sequential_search(list, item):
    found = False
    pos = 0

    while pos < len(list) and not found:
        if list[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found

if __name__ == '__main__':
    search_list = [1,2,3,4,5,65,7,8,9]
    print (sequential_search(search_list, 10))
    print(sequential_search(search_list, 65))
