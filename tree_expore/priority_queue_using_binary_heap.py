import my_abstract_pack.abstract_pack as ap

if __name__ == "__main__":
    pq = ap.binary_heap()

    # for i in [21,19,11,5,9,18,14,33,17,27]:
    for i in [5,9,11,14,18,19,21,33,17,27,7]:
        pq.insert(i)
    # pq.insert(9)
    # pq.insert(5)
    # pq.insert(6)
    # pq.insert(2)
    # pq.insert(3)
    print("before delete", pq.heap_list)

    pq.del_min()

    print("After delete", pq.heap_list)
