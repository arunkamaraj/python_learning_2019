import my_abstract_pack.abstract_pack as ap

def create_linked_list():
    for element in [10,20,30,40,50,60,70]:
        linked_list.add_and_update_tail(element)

def find_mid_by_iter():
    size = linked_list.size()

    mid = size//2

    head = linked_list.head
    for i in range(mid):
        mid_ele = head.get_next()

    print(mid_ele.get_data())

def find_mid_by_floyd_tortoise():
    p_slow = linked_list.head
    p_fast = linked_list.head

    while p_fast and p_fast.get_next() != None:
        p_fast = p_fast.get_next().get_next () if p_fast.get_next() else p_fast.get_next()
        p_slow = p_slow.get_next()

    print(p_slow.get_data())

if __name__ == "__main__":
    linked_list = ap.EfficientUnorderedList()
    create_linked_list()
    # find_mid_by_iter()
    find_mid_by_floyd_tortoise()