# bubble sort

# my bad code
def do_bubble_sort_my_bad(data):
    n = len(data)
    for i in range(n-1): # problem is here
        for j in range(n-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data



# better do_bubble_sort
def do_bubble_sort(data):
    n = len(data)
    for i in range(n-1, 0, -1): # problem is resolved -- #range(start, stop[, step]) -> range object
        for j in range(i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


if __name__ == "__main__":
    sample_data = [54,26,93,17,77,31,44,55,20]
    print(do_bubble_sort(sample_data))