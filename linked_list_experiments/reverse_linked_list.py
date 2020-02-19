class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head =  new_node

def print_linked_list(l_obj):
    cur_node = l_obj.head
    while cur_node is not None:
        print (cur_node.data, end=' ')
        cur_node = cur_node.next
# this is wrong
def reverse_linked_list(l,node):
    if node is None:
        return

    p = node
    q = node.next

    if q is None:
        l.head =  p
        return p

    q = reverse_linked_list(l,q)

    q.next = p
    p.next = None
    return p

if __name__ == "__main__":
    l = LinkedList()

    for i in [4,3,2,1,0]:
        l.add(i)

    print_linked_list(l)
    r = reverse_linked_list(l,l.head)
    print ("_______")

    print (r.data)
    print_linked_list(l)
