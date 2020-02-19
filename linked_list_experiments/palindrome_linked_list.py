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

    def append(self):
        pass


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(l):
    if isinstance(l, LinkedList):
        cur_node = l.head
    elif isinstance(l, Node):
        cur_node = l

    while cur_node is not None:
        print(cur_node.data, end=' ')
        cur_node = cur_node.next


def find_palindrome(l):
    if l.head.next is None:
        return True
    mid = find_mid(l)
    right = mid.next
    mid.next = None
    left = l.head
    reversed_right = do_reverse(right)
    return palindrome_check(left, reversed_right)

    # print ('\n this is new right', print_list(valid_right), '\n')


def palindrome_check(left, right):
    palindrom = True
    while left is not None and right is not None:
        if left.data == right.data:
            left = left.next
            right = right.next
        else:
            palindrom = False
            break
    return palindrom


def find_mid(l):
    node = l.head
    slow = node
    fast = node

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def do_reverse(node):
    p = node
    q = p.next

    if q is None:
        return p
    head = do_reverse(q)
    p.next.next = p
    p.next = None
    return head


if __name__ == "__main__":
    l = LinkedList()

    for i in [1]:
        l.add(i)

    ans = find_palindrome(l)
    print(ans)
