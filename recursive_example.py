
def sumList(list_data):
    if len(list_data) == 1:
        return list_data[0]
    else:
        return list_data[0] + sumList(list_data[1:])

if __name__ == '__main__':
    print(sumList([1,3,5,7,9]))
