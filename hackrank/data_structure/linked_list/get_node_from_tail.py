#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)

# Complete the getNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reverse(head):
    if head is None:
        return head

    p = head
    q = head.next

    if q is None:
        h = p

    if q is not None:
        h = reverse(q)
        p.next.next = p
        p.next = None

    return h

def getNode(head, positionFromTail):
    reversed_head = reverse(head)

    cur_pos = 0
    cur_node = reversed_head
    while cur_pos < positionFromTail:
        cur_node = cur_node.next
        cur_pos +=1

    return cur_node.data

if __name__ == '__main__':

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        position = int(input())

        result = getNode(llist.head, position)

        print(str(result) + '\n')
