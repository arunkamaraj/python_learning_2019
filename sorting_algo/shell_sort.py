# my own idea ..... eeeeeeeeeeeeeeeee
def do_shell_sort(data):
    n = len(data)
    gap = n//2
    sorted_data_with_gap = data
    while gap > 0:
        sorted_data_with_gap = do_insertion_sort(gap,n,sorted_data_with_gap)
        gap //= 2

    return sorted_data_with_gap

def do_insertion_sort(gap,n,shell_data):
    for i in range(gap,n):
        temp = shell_data[i]
        while i-gap >=0 and shell_data[i-gap] > temp:
            shell_data[i] = shell_data[i-gap]
            i-=gap
        shell_data[i] = temp

    return shell_data


if __name__ == '__main__':
    data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print (do_shell_sort(data))