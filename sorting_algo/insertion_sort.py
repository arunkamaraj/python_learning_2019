def do_insertion_sort(data):

    for i in range(1,len(data)):
        temp = data[i]
        for j in range(i,-1,-1):
            if data[j-1] > temp:
                # exchange = True
                data[j] = data[j-1]
            else:
                break
        data[j] = temp

    print (data)

def all_insertion_sort(data):
    for i in range(1,len(data)):
        temp = data[i]
        while i > -1 and data[i-1] > temp :
            data[i] = data[i-1]
            i -= 1
        data[i] = temp

    print (data)



if __name__ =="__main__":
    data = [54,26,93,17,77,31,44,55,20]
    # data = [20,10,5,40]
    do_insertion_sort(data)