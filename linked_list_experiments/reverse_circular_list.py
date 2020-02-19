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


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


def make_it_circular(l):
    cur_node = l.head

    while cur_node.next is not None:
        cur_node = cur_node.next

    cur_node.next = l.head


def print_list():
    pass


def reverse_list(node, l):
    p = node
    q = node.next

    if q is l.head:
        new_head = p
        return new_head

    new_head = reverse_list(q, l)

    p.next.next = p
    p.next = new_head

    return new_head


if __name__ == "__main__":
    l = LinkedList()

    for i in [4, 3, 2, 1]:
        l.add(i)

    make_it_circular(l)

    new_head = reverse_list(l.head, l)

    l.head = new_head

    print(l)
