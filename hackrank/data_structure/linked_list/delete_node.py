class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def add_in_tail(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            cur_node = self.head
            while cur_node.next != None:
                cur_node = cur_node.next
            cur_node.next = node

    def add_in_head(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def delete_node(self, pos):
        cur_node = self.head
        cur_pos = 0
        if cur_node:
            if pos == 0:
                self.head = self.head.next
            else:
                while cur_pos < pos-1:
                    cur_node = cur_node.next
                    cur_pos +=1

                cur_node.next = cur_node.next.next

def print_linked_list(l):
        cur_node = l.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next


if __name__ == "__main__":
    llist_count = int(input())

    llist = LinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.add_in_tail(llist_item)

    # print_linked_list(llist)

    llist.delete_node(2)

    print_linked_list(llist)