class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def add(self, element):
        node = Node(data= element)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def append(self, element):
        node = Node(data = element)
        if self.head == None:
            self.head = node
        else:
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next

            cur_node.next = node

def mergesort(h):
    if h == None or h.next == None:
        return h

    mid_element = find_mid(h)
    mid_element_next = mid_element.next
    mid_element.next = None

    left  = mergesort(h)
    right = mergesort(mid_element_next)

    sorted_linked_list = merge(left, right)

    return  sorted_linked_list


def merge(left,right):
    result = linked_list()
    while left is not None and right is not None:
        if left.data < right.data:
            min_data = left.data
            left = left.next
        elif left.data > right.data:
            min_data = right.data
            right = right.next

        result.append(min_data)

    while left is not None:
        result.append(left.data)
        left = left.next
    while right is not None:
        result.append(right.data)
        right = right.next

    return result.head

def find_mid(li):

    slow_ptr = li
    fast_ptr = li

    while fast_ptr.next is not None and fast_ptr.next.next is not None:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next

    return slow_ptr

if __name__ == "__main__":
    li = linked_list()

    # Let us create a unsorted linked list
    # to test the functions created.
    # The list shall be a: 2->3->20->5->10->15
    li.add(5)
    li.add(7)
    li.add(3)
    li.add(0)
    li.add(8)
    li.add(2)

    sorted_output = mergesort(li.head)

    print(sorted_output)
    while sorted_output:
        print (sorted_output.data)
        sorted_output = sorted_output.next






