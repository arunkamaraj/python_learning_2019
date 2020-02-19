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

def remove_duplicate(l):
    p = l.head
    while p is not None and p.next is not None:
        q = p # same p and q bcz to avoid issue in removing duplicate

        while q.next is not None:
            if p.data == q.next.data:
                duplicate = q.next

                q.next = q.next.next

                del duplicate

            else:
                q = q.next
        p = p.next

def print_list(l):
    if isinstance(l, LinkedList):
        cur_node = l.head
    elif isinstance(l, Node):
        cur_node = l

    while cur_node is not None:
        print (cur_node.data, end=' ')
        cur_node = cur_node.next

if __name__ == "__main__":
    l = LinkedList()

    for i in [1,2,3, 3, 8]:
    # for i in [1,3,2,1]:
        l.add(i)

    print_list(l)

    remove_duplicate(l)

    print("\nafter removal\n")

    print_list(l)

