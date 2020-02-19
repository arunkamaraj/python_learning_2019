class Linked_list:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.down = self.head
            self.head = new_node

    def append(self, element):
        new_node = Node(element)

        if self.head is None:
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.down is not None:
                cur_node = cur_node.down

            cur_node.down = new_node

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None


def merge_list(x,y):
    if x is None:
        return y

    if y is Node:
        return x

    sorted_list = Linked_list()

    while x is not None and y is not None:
        if x.data < y.data:
            min_node = x
            x = x.down
        elif x.data > y.data:
            min_node = y
            y = y.down

        sorted_list.append(min_node.data)

    while x is not None:
        sorted_list.append(x.data)
        x = x.down

    while y is not None:
        sorted_list.append(y.data)
        y = y.down

    return sorted_list.head

def print_node(node):
    while node is not None:
        print(node.data , end= ' ')
        node = node.down

def flatten_list(node):

    if node.right is None:
        return node

    sorted = merge_list(node, flatten_list(node.right))
    return sorted

if __name__ == "__main__":
    a = Linked_list()
    b = Linked_list()
    c = Linked_list()

    for i in [7,4,1]:
        a.add(i)

    for j in [8,6,2]:
        b.add(j)

    for k in [10,9,3]:
        c.add(k)

    a.head.right = b.head
    a.head.right.right = c.head

    output = flatten_list(a.head)
    print_node(output)




