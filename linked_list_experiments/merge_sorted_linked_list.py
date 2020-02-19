class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, element):
        new_node = Node(element)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head.next
            self.head = new_node

    def append(self, element):
        new_node = Node(element)

        if self.head is None:
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next

            cur_node.next = new_node

def merge_sorted_list_using_third_linkedlist(a, b):
    new_list = LinkedList()

    while a is not None and b is not None:
        if a.data < b.data:
            new_list.append(a.data)
            a = a.next
        elif a.data > b.data:
            new_list.append(b.data)
            b = b.next

    while a is not None:
        new_list.append(a.data)
        a = a.next

    while b is not None:
        new_list.append(b.data)
        b = b.next

    print_list(new_list.head)

def print_list(d):
    while d is not None:
        print (d.data)
        d = d.next

def merge_sorted_list(a,b):
    if a is None:
        return b
    elif b is None:
        return a



if __name__ == "__main__":
    a = LinkedList()
    b = LinkedList()

    for i in [1,3,5]:
        a.append(i)

    for j in [2,4,6,7]:
        b.append(j)

    merge_sorted_list_using_third_linkedlist(a.head, b.head)
    # merge_sorted_list(a.head, b.head)



