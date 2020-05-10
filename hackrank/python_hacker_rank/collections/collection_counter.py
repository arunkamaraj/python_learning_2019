from collections import Counter
if __name__ == "__main__":
    n = int(input())
    size_list = list(map(int, input().split()))
    cust_no = int(input())

    size_dict = Counter(size_list)
    total_amt = 0
    for i in range(cust_no):
        size, amt = list(map(int, input().split()))
        if size in list(size_dict.elements()):
            size_dict[size] = size_dict[size]-1
            total_amt = total_amt + amt

    print(total_amt)

