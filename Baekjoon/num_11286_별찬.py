# name: 절댓값 힙
# date: July 7, 2020
# status: solved

import sys


class Heap:
    def __init__(self):
        self.tree = [0]
        self.size = 1

    def insert(self, element):

        self.tree.append(element)

        if (self.size == 1):
            self.size += 1

            return element
        self.size += 1
        ROOT_POS = 1
        current_pos = self.size - 1
        parent_pos = current_pos // 2

        while (current_pos > ROOT_POS):

            if (compare_abs(self.tree[parent_pos], self.tree[current_pos])):
                return element
            swap(self.tree, parent_pos, current_pos)
            current_pos = parent_pos
            parent_pos //= 2

        return element

    def delete(self):

        ROOT_POS = 1
        last_pos = self.size - 1
        if (last_pos == 0):

            return 0
        if (last_pos == 1):
            self.size -= 1

            return self.tree.pop()

        swap(self.tree, ROOT_POS, last_pos)
        removed = self.tree.pop()
        self.size -= 1
        last_pos -= 1

        current_pos = ROOT_POS
        left_pos = current_pos * 2
        right_pos = current_pos * 2 + 1
        while(current_pos <= last_pos):
            if ((left_pos > last_pos or compare_abs(self.tree[current_pos], self.tree[left_pos])) and (right_pos > last_pos or compare_abs(self.tree[current_pos], self.tree[right_pos]))):
                return removed
            elif (left_pos > last_pos or compare_abs(self.tree[current_pos], self.tree[left_pos])):
                swap(self.tree, current_pos, right_pos)
                current_pos = right_pos
            elif (right_pos > last_pos or compare_abs(self.tree[current_pos], self.tree[right_pos])):
                swap(self.tree, current_pos, left_pos)
                current_pos = left_pos
            else:
                selected_pos = left_pos if compare_abs(
                    self.tree[left_pos], self.tree[right_pos]) else right_pos
                swap(self.tree, current_pos, selected_pos)
                current_pos = selected_pos
            left_pos = 2 * current_pos
            right_pos = 2 * current_pos + 1

        return removed

    def print_tree(self):
        print(self.tree)


def swap(li, first, second):
    li[first] = li[first] ^ li[second]
    li[second] = li[first] ^ li[second]
    li[first] = li[first] ^ li[second]


def compare_abs(first, second):
    if (abs(first) == abs(second)):
        return first < second
    return abs(first) < abs(second)


def solution():
    count = int(sys.stdin.readline())
    operations = [int(sys.stdin.readline()[:-1]) for i in range(count)]
    heap = Heap()

    for element in operations:
        if (element == 0):
            print(heap.delete())
            continue
        heap.insert(element)


solution()
