class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(l):
    if isinstance(l,LinkedList):
        cur_node = l.head
    elif isinstance(l, Node):
        cur_node = l

    while cur_node is not None:
        print(cur_node.data , end= ' ')
        cur_node = cur_node.next

def find_last_occuerance_and_remove(item, l):
    node = l.head
    occurance_node = None
    while node is not None:
        if node.data == item:
            occurance_node = node
        node = node.next

    if occurance_node:
        occurance_node.data = occurance_node.next.data
        occurance_node.next = occurance_node.next.next


if __name__ == "__main__":
    l = LinkedList()

    for i in [7,10,2,3,4,5,6,2,5,6]:
        l.add(i)

    print_list(l)

    key_item = 2 # need to find the last occurrence of that item and need to remove that.

    find_last_occuerance_and_remove(key_item, l)
    print ('\n')
    print_list(l)