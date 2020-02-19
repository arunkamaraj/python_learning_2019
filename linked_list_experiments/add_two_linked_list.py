class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.size +=1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(l):
    if isinstance(l, LinkedList):
        cur_node = l.head
    elif isinstance( l, Node):
        cur_node = l

    while cur_node is not None:
        print(cur_node.data, end=' ')
        cur_node = cur_node.next

def make_equal_size(a,b):
    if a.size == b.size:
        return
    elif a.size > b.size:
        diff = a.size - b.size
        for i in range(diff):
            b.add(0)
    elif a.size < b.size:
        diff = b.size - a.size
        for i in range(diff):
            a.add(0)

def reverse_linked_list(l, a):
    if l is None:
        return a
    p = l
    q = l.next

    if q is None:
        a.head = p
        return

    q = reverse_linked_list(q, a)

    p.next.next = p
    p.next = None
    return a.head

def adding(x, y):
    result = LinkedList()
    carry = 0

    for _ in range(a.size):
        temp_result = x.data + y.data
        if carry > 0:
            temp_result = temp_result + carry
            carry = 0

        division = temp_result // 10
        if division > 0:
            carry = division
            result.add(temp_result % 10)
            x = x.next
            y = y.next
        else:
            result.add(temp_result)
            x = x.next
            y = y.next

    if carry > 0:
        result.add(carry)

    return result

if __name__ == "__main__":
    a = LinkedList()
    b = LinkedList()

    for i in [1,2,8,9,9]:
        a.add(i)

    for j in [3,6,9]:
        b.add(j)

    # print("before size", a.size, "and", b.size)
    make_equal_size(a,b)
    # print("After size", a.size, "and", b.size)

    reverse_linked_list(a.head, a)
    reverse_linked_list(b.head, b)
    added_value = adding(a.head, b.head)
    print_list(added_value)
