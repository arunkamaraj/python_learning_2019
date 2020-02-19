import my_abstract_pack.abstract_pack as abstract_type

def efficient_list_operation():
    mylist = abstract_type.EfficientUnorderedList()
    # adding nodes
    mylist.add_and_update_tail(10)

    print("head", mylist.head.get_data())
    print("tail", mylist.tail.get_data())

    mylist.add_and_update_tail(20)
    print("head", mylist.head.get_data())
    print("tail", mylist.tail.get_data())

    mylist.add_and_update_tail(30)
    print("head", mylist.head.get_data())
    print("tail", mylist.tail.get_data())

    # size
    print(mylist.size())

    #
    print ("--------------------")

    mylist.remove_and_update_tail(10)
    print("head", mylist.head.get_data())
    print("tail", mylist.tail.get_data())

    print("size of the list ", mylist.size())

    print ("--------------------")
    mylist.append_and_update_tail(100)
    print("head", mylist.head.get_data())
    print("tail", mylist.tail.get_data())

    print("size of the list ", mylist.size())

def ordinary_list_operation():
    mylist = abstract_type.UnorderedList()

    # adding nodes
    for value in [10,20,30]:
        mylist.add(value)
        print("head", mylist.head.get_data())

    # size
    print("size of the list ", mylist.size())

    # search
    print ("search in the list for value 10",mylist.search(10))
    print ("search in the list for value 100", mylist.search(100))

    # # remove
    # mylist.remove(10)
    # mylist.remove(100)
    #
    # #append
    # mylist.append(100)

    #index
    for i in [100]:
        print("index of", mylist.index(i))

if __name__ == '__main__':
    ordinary_list_operation()
    # efficient_list_operation()