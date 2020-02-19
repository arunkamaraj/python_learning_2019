# diff between bubble and selection sort is to reduce the no of exchange .

def do_selction_sort(data):
    for i in range(len(data)-1):
        min = i
        for j in range(i+1, len(data)):
            if data[min] > data[j]:
                min = j

        if data[min] != data[i]:
            data[i], data[min] = data[min], data[i]

    return data

if __name__ == '__main__':
    data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print (do_selction_sort(data))