class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is  None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def append(self, data):
        new_node  = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur_node = self.head

            while cur_node.next is not None:
                cur_node = cur_node.next

            cur_node.next = new_node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_mid(node):
    if node is not None:
        slow_p = node
        fast_p = node

        while fast_p.next is not None and fast_p.next.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

        return slow_p

def merge_list(left, right):
    merged_list = LinkedList()

    while left is not None and right is not None:
        if left.data <= right.data: # = tooks lot of time
            merged_list.append(left.data)
            left = left.next

        elif left.data >= right.data:
            merged_list.append(right.data)
            right = right.next

    while left is not None:
        merged_list.append(left.data)
        left = left.next

    while right is not None:
        merged_list.append(right.data)
        right = right.next

    return merged_list.head

def do_merge_sort(node):
    if node is None or node.next is None: # this condition for node count should be > 1
        return  node

    mid_element = find_mid(node)
    next_to_mid = mid_element.next

    mid_element.next = None

    left = do_merge_sort(node)
    right = do_merge_sort(next_to_mid)
    merged_data = merge_list(left, right)
    return merged_data

def print_list(l):
    if isinstance(l, LinkedList):
        cur_node = l.head
    elif isinstance(l, Node):
        cur_node = l

    while cur_node is not None:
        print(cur_node.data, end =' ')
        cur_node = cur_node.next

def remove_duplicate(node):
    while node is not None and node.next is not None:
        if node.data == node.next.data:
            duplicate = node.next
            node.next = node.next.next

            del duplicate

        node = node.next


if __name__ == "__main__":
    l = LinkedList()

    for i in [1,4,2,7,5,8,3,4,2]:
        l.add(i)

    print_list(l)
    sorted  = do_merge_sort(l.head)

    print('\n\nAfter sorting \n')
    print_list(sorted)

    remove_duplicate(sorted)


    print('\n\nAfter removed duplicate \n')
    print_list(sorted)



