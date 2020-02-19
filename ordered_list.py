import my_abstract_pack.abstract_pack as abstract_type


def ordered_linked_list(mylist):
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)

    print(mylist.size())
    print(mylist.search(93))
    print(mylist.search(100))
    print(mylist)


if __name__ == '__main__':
    ol = abstract_type.OrderedList()
    ordered_linked_list(ol)
