# name: editor
# data: July 8, 2020
# status: solved

import sys


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.current = None

    # add character at the end of text
    def push(self, data):
        node = Node(data)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

        self.current = node
        return node

    # add character right to the cursor
    def insert(self, data):
        node = Node(data)
        node.next = self.current.next
        node.prev = self.current
        self.current.next = node
        node.next.prev = node
        self.current = node
        return node

    # delete character left of the cursor
    def delete(self):
        if (self.current is self.head):
            return None
        node = self.current
        self.current.prev.next = self.current.next
        self.current.next.prev = self.current.prev
        self.current = self.current.prev
        return node

    # move cursor one character to the left
    def move_left(self):
        if (self.current is not self.head):
            self.current = self.current.prev

    # move cursor one character to the right
    def move_right(self):
        if (self.current.next is not self.tail):
            self.current = self.current.next

    def print_elements(self):
        node = self.head.next
        while (node is not self.tail):
            print(node.data, end="")
            node = node.next
        print()


def solution():
    text = sys.stdin.readline()[:-1]
    linked_list = DoublyLinkedList()
    for letter in text:
        linked_list.push(letter)
    count = int(sys.stdin.readline())
    for i in range(0, count):
        line = sys.stdin.readline()
        sign = line[0]
        if sign == 'L':
            linked_list.move_left()
        elif sign == 'D':
            linked_list.move_right()
        elif sign == 'B':
            linked_list.delete()
        elif sign == 'P':
            alphabet = line.split(' ')[1][0]
            linked_list.insert(alphabet)
    linked_list.print_elements()


solution()
