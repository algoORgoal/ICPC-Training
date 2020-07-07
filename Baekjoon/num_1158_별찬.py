# name: 요세푸스 문제
# date: July 7, 2020
# status: solved

import sys


class Node:
    def __init__(self, element=None, next=None):
        self.element = element
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.current = None
        self.size = 0

    def insert(self, element):
        self.size += 1

        if (self.head is None):
            self.head = Node(element)
            self.head.next = self.head
            return
        if (self.head.next is None):
            tail = Node(element)
            tail.next = self.head
            self.head.next = tail
        node = self.head.next
        while (node.next is not self.head):
            node = node.next
        tail = Node(element)
        tail.next = node.next
        node.next = tail

    def delete(self, step):
        if (self.size == 0):
            return None
        if (self.size == 1):
            element = self.head.element
            self.head = None
            self.current = None
            self.size -= 1
            return element
        if (step == 1 and self.current is None):
            node = self.head
            self.head = self.head.next
            return node.element

        self.size -= 1
        count = 0
        if (self.current is None):
            self.current = self.head
            count += 1

        while (count < step - 1):
            self.current = self.current.next
            count += 1

        node = self.current.next

        if (node is self.head):
            self.head = node.next

        self.current.next = self.current.next.next

        return node.element

    def print_elements(self):

        print(self.head.element, end=" ")
        node = self.head.next

        while (node is not self.head):
            print(node.element, end=" ")
            node = node.next
        print()


def solution():
    [n, k] = list(map(lambda num: int(num), sys.stdin.readline().split(' ')))
    linked_list = CircularLinkedList()
    for element in range(1, n + 1):
        linked_list.insert(element)
    answer = ""
    answer += "<"
    for i in range(1, n + 1):
        answer += str(linked_list.delete(k))
        if (i == n):
            continue
        answer += ", "

    answer += ">"
    print(answer)


solution()
