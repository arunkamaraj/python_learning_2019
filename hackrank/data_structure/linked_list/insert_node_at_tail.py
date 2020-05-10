class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList():
    def __init__(self):
        self.head = None

    def append_node(self, data):
        node = Node(data)
        cur_node = self.head

        if cur_node is None:
            self.head = node
        else:
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = node

def print_linked_list(l):

    cur_node = l.head
    # cur_node = l
    while cur_node:
        print(cur_node.data)
        cur_node = cur_node.next

if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = llist.append_node(llist_item)

    print_linked_list(llist)

