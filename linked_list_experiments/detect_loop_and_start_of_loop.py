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


def create_testing_loop(node, start, end):
    while node is not None:
        if node.data == start:
            node_start = node
        elif node.data == end:
            node_end = node
        node = node.next

    node_end.next = node_start


def print_list(l):
    if isinstance(l, LinkedList):
        cur_node = l.head
    elif isinstance(l, Node):
        cur_node = l

    while cur_node is not None:
        print(cur_node.data, end=' ')
        cur_node = cur_node.next


def detetcting_loop(l):
    node = l.head
    p = node
    q = node

    while (p and q and q.next):
        p = p.next
        q = q.next.next

        if p.data == q.data:
            return p
    return

def find_start_of_loop(l, loop):
    if loop:
        node = l.head
        p = node
        q = loop

        while p != q:
            p = p.next
            q = q.next
        return p

if __name__ == "__main__":
    l = LinkedList()

    for i in [9, 8, 7, 6, 5, 4, 3, 2, 1, ]:
        l.add(i)

    # set up loop
    node = l.head
    create_testing_loop(node, 1, 9)

    # detect loop
    loop = detetcting_loop(l)
    print(loop.data
          )

    # start of the loop
    start_node = find_start_of_loop(l, loop)

    print(start_node.data)
