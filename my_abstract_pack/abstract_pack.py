class Stack:

    def __init__(self):
        self.item = []

    def push(self, data):
        self.item.append(data)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[-1]

    def is_empty(self):
        return len(self.item) == 0

    def size(self):
        return len(self.item)


class Queue:
    def __init__(self):
        self.item = []

    def enqueue(self, value):
        self.item.insert(0, value)

    def dequeue(self):
        return self.item.pop()

    def is_empty(self):
        return len (self.item) == 0

    def size(self):
        return len(self.item)


class Deque:
    def __init__(self):
        self.item =[]

    def rear_add(self, data):
        self.item.insert(0, data)

    def rear_remove(self):
        return self.item.pop(0)

    def front_add(self, data):
        self.item.append(data)

    def front_remove(self):
        return self.item.pop()

    def is_empty(self):
        return self.item == []

    def size(self):
        return len(self.item)

class Node:
    def __init__(self, value):
        self.data= value
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_value):
        self.data = new_value

    def set_next(self, next_node):
        self.next = next_node

class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        temp  = Node(data)
        temp.next = self.head
        self.head = temp

    def size(self):
        current = self.head
        counter = 0

        while current != None:
            counter = counter +1
            current = current.get_next()

        return counter

    def search(self, value):
        current = self.head

        Found = False

        while current != None and not Found:
            if current.get_data() == value:
                Found = True
            else:
                current =  current.get_next()

        return Found

    def remove(self, value):
        current = self.head
        previous = None

        Found = False

        while current is not None and not Found:
            if current.get_data() == value:
                Found = True
            else:
                previous = current
                current = current.get_next()

        if Found and previous != None:
            previous.next = current.get_next()

        elif Found and previous == None:
            self.head = current.get_next()
        else:
            print ("we could not find the value to remove")

    def append(self, value):
        current = self.head
        temp = Node(value)

        if current:
            while current.get_next() is not None:
                print (current.get_data())
                current = current.get_next()
            current.set_next(temp)

        else:
            self.head = temp

    def insert(self):
        pass

    def index(self, value):
        postion = 0
        current = self.head

        Found = False

        while current != None and not Found:
            if current.get_data() == value:
                Found = True
            else:
                current =  current.get_next()
                postion = postion + 1

        if  Found:
            return  postion
        else:
            return "Item not available"

    def pop(self):
        pass



class EfficientUnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_and_update_tail(self, data):
        temp  = Node(data)
        temp.next = self.head
        self.head = temp
        if self.tail is None:
            self.tail = temp

    def size(self):
        current = self.head
        counter = 0

        while current != None:
            counter = counter +1
            current = current.get_next()

        return counter

    def search(self, value):
        current = self.head

        Found = False

        while current != None and not Found:
            if current.get_data() == value:
                Found = True
            else:
                current =  current.get_next()

        return Found

    def remove_and_update_tail(self, value):
        current = self.head
        previous = None

        Found = False

        while current is not None and not Found:
            if current.get_data() == value:
                Found = True
            else:
                previous = current
                current = current.get_next()

        if Found and previous != None:
            previous.next = current.get_next()

        elif Found and previous == None:
            self.head = current.get_next()
        else:
            print ("we could not the value to remove")

        if self.tail.get_data() == value:
            self.tail = previous

    def append_and_update_tail(self, value):
        tail = self.tail
        temp = Node(value)

        if tail:
            tail.set_next(temp)
        else:
            self.head = temp

        self.tail = temp

    def insert(self):
        pass

    def index(self):
        pass

    def pop(self):
        pass


class OrderedList:

    def __init__(self):
        self.head = None

    def add(self, value):
        current = self.head
        previous = None
        temp = Node(value)
        stop = False


        while current is not None and not stop :
            if current.get_data() > value:
                stop = True

            else:
                previous = current
                current = current.get_next()

        if previous:
            temp.set_next(current)
            previous.set_next(temp)
        else:
            temp.set_next(self.head)
            self.head = temp


    def search(self, value):
        current = self.head
        found = False
        stop = False

        while current is not None and not found and not stop:
            if current.get_data() == value:
                found = True

            else:
                if current.get_data() > value:
                    stop = True
                else:
                    current = current.get_next()

        return found

    def remove(self, value):
        current = self.head
        previous = None
        found = False
        stop = False

        while current is not None and not found and not stop:
            if current.get_data() == value:
                found = True

            else:
                if current.get_data() > value:
                    stop = True
                else:
                    previous = current
                    current = current.get_next()

        if previous and found:
            previous.set_next(current.get_next())

        elif found and previous is None:
            self.head = current.get_next()
        else:
            print("we could not the value to remove")


    def size(self):
        current = self.head
        counter = 0

        while current is not None:
            counter = counter + 1
            current = current.get_next()

        return counter

    def __str__(self):
        result ='['
        current = self.head
        if current:
            while current != None:
                result = result + str(current.get_data()) + ','
                current = current.get_next()

            result = result + ']'
        else:
            result = '[]'

        return result

class Map:
    def __init__(self, size):
        self.size = size
        self.keyInfo = [None]* size
        self.dataInfo = [None] * size

    def get(self, key):
        startslot = self.hash_function(key, self.size)
        found = False
        stop = False
        position = startslot


        if self.keyInfo[position] == key:
            found = True
        else:
            while not found and not stop:
                position = self.rehash_funtion(position, self.size)

                if self.keyInfo[position]== key:
                    found = True
                elif position == startslot:
                    stop = True

        if found and not stop:
            return self.dataInfo[position]
        else:
            return  "Item not found map"

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.keyInfo))

        if self.keyInfo[hash_value] is None:
            self.keyInfo[hash_value] = key
            self.dataInfo[hash_value] = data

        elif self.keyInfo[hash_value] == key:
            self.dataInfo[hash_value] = data

        else:
            next_value = self.rehash_funtion(hash_value, len(self.keyInfo))

            while self.keyInfo[next_value] is not None and  self.keyInfo[next_value] != key:
                next_value = self.rehash_funtion(next_value, len(self.keyInfo))

            if self.keyInfo[next_value] is None:
                self.keyInfo[next_value] = key
                self.dataInfo[next_value] = data

            elif self.keyInfo[next_value] == key:
                self.dataInfo[next_value] = data


    def delete(self):
        pass

    def hash_function(self, key, size):
        return key % size

    def rehash_funtion(self, key, size):
        return (key + 1) % size

    def __setitem__(self, key, data):
        self.put(key, data)

    def __getitem__(self, key):
        return self.get(key)


# this class structure is my own try actual example show with simple class
class binary_tree_list_rep():
    def __init__(self, root):
        self.t = [root, [], []]

    def insert_left(self, root, tree):
        sub_tree = binary_tree_list_rep(tree)
        left_tree = root.pop(1)
        if len(left_tree)> 1:
            sub_tree.t[1]= left_tree
            root.insert(1,sub_tree.t)

        else:
            root.insert(1, sub_tree.t)

    def insert_right(self,root, tree):
        sub_tree = binary_tree_list_rep(tree)
        right_tree = root.pop(2)
        if len(right_tree):
            sub_tree.t[2]= right_tree
            root.insert(2, sub_tree.t)

        else:
            root.insert(2, sub_tree.t)

    def get_root(self):
        return  self.t[0]

    def set_root(self, element):
        self.t[0] = element

    def get_left(self, root):
        return root[1]

    def get_right(self, root):
        return root[2]


class binary_tree():
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert_left(self, data):

        if self.left_child is None:
            self.left_child = binary_tree(data)

        else:
            child = binary_tree(data)
            child.left_child = self.left_child
            self.left_child = child

    def insert_right(self, data):
        if self.right_child is None:
            self.right_child = binary_tree(data)

        else:
            child = binary_tree(data)
            child.right_child =  self.right_child
            self.right_child = child

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_root_data(self):
        return self.data

    def set_root_data(self, newdata):
        self.data = newdata


class TreeHelper:

    @staticmethod
    def do_build_parse_tree(expr):
        token_list = expr.split()
        bt = binary_tree('')
        stack = Stack()
        stack.push(bt)  # to avoid ) final closing bracket we are hitting null index so
        current_node = bt

        for i in token_list:
            if i == '(':
                current_node.insert_left('')
                stack.push(current_node)
                current_node = current_node.get_left_child()

            elif i in [str(j) for j in range(100)]:
                current_node.set_root_data(i)
                current_node = stack.pop()

            elif i in ['+', '-', '*', '/']:
                current_node.set_root_data(i)
                stack.push(current_node)
                current_node.insert_right('')
                current_node = current_node.get_right_child()
            elif i == ')':
                current_node = stack.pop()
                # stack.push(current_node)
            else:
                print('unknown tokens', i)

        return bt

class binary_heap():
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def percolate_up(self, i):
        # handling parent and child index in same variable
        while i > 0 and self.heap_list[i] < self.heap_list[i //2]:
            temp = self.heap_list[i//2]
            self.heap_list[i//2] = self.heap_list[i]
            self.heap_list[i] = temp

            i//=2

    def percolate_down(self,i):

        while i*2 < self.current_size:
            min = self.min_child(i)
            if self.heap_list[i] > self.heap_list[min]:
                temp = self.heap_list[min]
                self.heap_list[min] = self.heap_list[i]
                self.heap_list[i] = temp

                i = min
            else:
                break

    def insert(self, data):
        # My attempt
        # self.heap_list.append(data)
        # new_data_idx = self.heap_list.index(data)
        # parent_idx = (len(self.heap_list) - 1) // 2
        #
        # while parent_idx > 0 and self.heap_list[parent_idx] > self.heap_list[new_data_idx]:
        #     temp = self.heap_list[parent_idx]
        #     self.heap_list[parent_idx] = self.heap_list[new_data_idx]
        #     self.heap_list[new_data_idx] = temp
        #
        #     new_data_idx = self.heap_list.index(data)
        #     parent_idx //=  2
        self.heap_list.append(data)
        self.current_size += 1
        self.percolate_up(self.current_size)

    def del_min(self):
        self.heap_list[1]= self.heap_list[self.current_size]
        self.heap_list.pop()
        self.current_size -= 1 # i missed to reduce the current size it leads to index error
        self.percolate_down(1)

    def min_child(self, i):
        if self.heap_list[i*2] < self.heap_list[(i*2)+1]:
            return i*2
        else:
            return (i*2) +1

    def build_heap(self):
        pass

    def size(self):
        return self.current_size

    def is_empty(self):
        return self.current_size < 1


class TreeNode:
    def __init__(self, key, payload, left=None, right=None, parent=None):
        self.key = key
        self.payload = payload
        self.left_child = left
        self.right_child = right
        self.parent = parent
        self.balance_factor = 0

    def has_left_child(self):#8
        return self.left_child

    def has_right_child(self):#9
        return self.right_child

    def is_left_child(self): #2
        return self.parent and self.parent.left_child == self

    def is_right_child(self): #3
        return self.parent and self.parent.right_child == self

    def is_root(self): #1
        return self.parent is None

    def is_leaf(self):#4
        return self.right_child is None and self.left_child is None

    def has_any_children(self): #5
        return self.right_child or self.left_child

    def has_both_children(self): #6
        return  self.right_child and self.left_child

    def replace_node(self, key, payload, left=None, right=None, parent=None):
        pass

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def left_rotate(self):
        pass

    def right_rotate(self):
        pass

    def re_balance(self, cur_node):
        if cur_node.balance_factor > 0:
            if cur_node.left_child.balance_factor < 0:
                self.left_rotate(cur_node.left_child)
                self.right_rotate(cur_node)
            else:
                self.right_rotate(cur_node)

        elif cur_node.balance_factor < 0:
            if cur_node.right_child.balance_factor >0:
                self.right_rotate(cur_node.right_child)
                self.left_rotate(cur_node)
            else:
                self.left_rotate(cur_node)


    def update_balance_factor(self,cur_node):
        if cur_node.balance_factor < 0 or cur_node.balance_factor > 0:
            self.re_balance(cur_node)
            return # bcz, it is recursive fun it should return something to the rec call
        if cur_node:
            if cur_node.is_left_child():
                cur_node.parent.balance_factor +=1
            elif cur_node.is_right_child():
                cur_node.parent.balance_factor -=1

            if cur_node.parent.balance_factor != 0:
                self.update_balance_factor(cur_node.parent)

    def put(self,key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
            self.size +=1

    def _put(self, key, value, node):
        if key < node.key:
            if node.has_left_child():
                self._put(key, value, node.left_child)
            else:
                node.left_child = TreeNode(key,value,parent=node)
                self.update_balance_factor(node.left_child)
                self.size += 1

        else:
            if node.has_right_child():
                self._put(key, value, node.right_child)
            else:
                node.right_child = TreeNode(key, value, parent=node)
                self.update_balance_factor(node.right_child)
                self.size += 1


    def get(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result
            else:
                return None
        else:
            return

    def _get(self,key, current_node):
        if not current_node:
            return None
        elif key == current_node.key:
            return current_node
        elif key < current_node.key:
            return self._get(key,current_node.left_child)
        elif key > current_node.key:
            return  self._get(key, current_node.right_child)

    def find_successor(self):
        return self.right_child.find_min()

    def find_min(self):
        succ = self
        while succ.has_left_child():
            succ = succ.left_child()
        return succ

    def spliceout(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.right_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.is_left_child():
                self.parent.left_child = self.right_child
            else:
                self.parent.right_child = self.right_child

            self.right_child.parent = self.parent


    def remove(self, node_to_delete):
        if node_to_delete.is_leaf():
            if node_to_delete.parent.left_child == node_to_delete:
                node_to_delete.praent.left_child = None
            else:
                node_to_delete.praent.right_child = None

        elif node_to_delete.has_both_children():
            succ = node_to_delete.find_successor()
            succ.spliceout()
            node_to_delete.key = succ.key
            node_to_delete.payload = succ.payload

        else: # single child
            if node_to_delete.has_left_child():
                if node_to_delete.parent.left_child == node_to_delete:
                    node_to_delete.parent.left_child = node_to_delete.left_child
                    node_to_delete.left_child.parent = node_to_delete.parent

                elif node_to_delete.parent.right_child == node_to_delete:
                    node_to_delete.parent.right_child = node_to_delete.left_child
                    node_to_delete.left_child = node_to_delete.parent

            elif node_to_delete.has_right_child():
                if node_to_delete.parent.right_child == node_to_delete:
                    node_to_delete.parent.right_child = node_to_delete.right_child
                    node_to_delete.right_child = node_to_delete.parent

                elif node_to_delete.parent.left_child == node_to_delete:
                    node_to_delete.parent.left_child = node_to_delete.right_child
                    node_to_delete.right_child = node_to_delete.parent

    def delete(self, key):
        if self.size > 1:
            node_to_delete = self.get(key)
            if node_to_delete:
                self.remove(node_to_delete)
                self.size -= 1
                # needs to handle the cases

            else:
                raise KeyError("key is missing")

        elif self.size ==1 and self.root.key ==key:
            self.root = None
            self.size -=1
        else:
            raise KeyError("key is missing")


    def __setitem__(self, key, value):
        self.put(key, value)

class Vertex:
    def __init__(self, key, vertex_status = 'white'):
        self.id = key
        self.color = vertex_status
        self.length = 0
        self.predecessor = None
        self.connected_to = {}

    def add_neighbor(self, nbr, weight):
        self.connected_to[nbr] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def __str__(self):
        return str(self.id) + " is connected to" + str([i.id for i in self.get_connections()])


class Graphs:
    def __init__(self):
        self.vertex_list = {}
        self.num_vertex = 0

    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vertex_list[key] = new_vertex
        self.num_vertex += 1

    def add_edges(self, f, t, cost= 0):
        if f not in self.vertex_list:
            self.add_vertex(f)
        if t not in self.vertex_list:
            self.add_vertex(t)

        self.vertex_list[f].add_neighbor(self.vertex_list[t], cost)

    def add_both_edges(self,f,t):
        self.add_edges(f,t)
        self.add_edges(t,f)

    def get_vertex(self, key):
        return self.vertex_list[key] if key in self.vertex_list else None

    def get_vertices(self):
        return self.vertex_list.keys()

    def contain(self, key):
        return key in self.vertex_list
