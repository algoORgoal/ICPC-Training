# name: max heap
# data: July 7, 2020
# status: solved

import sys


def solution():
    count = int(sys.stdin.readline())
    elements = []

    for i in range(0, count):
        elements.append(int(sys.stdin.readline()))

    heap = [0]
    for element in elements:
        if (element == 0 and len(heap) - 1 == 0):
            print(element)
        elif (element == 0):
            print(remove(heap))
        else:
            insert(heap, element)


def insert(heap, element):
    ROOT_POS = 1

    heap.append(element)
    node_pos = len(heap) - 1
    par_pos = node_pos // 2

    while (node_pos > ROOT_POS and heap[node_pos] > heap[par_pos]):
        swap(heap, node_pos, par_pos)
        node_pos = par_pos
        par_pos //= 2


def remove(heap):
    if (len(heap) - 1 == 1):
        return heap.pop()

    root_pos = 1
    last_pos = len(heap) - 1
    swap(heap, root_pos, last_pos)

    if (len(heap) - 1 == 2):
        return heap.pop()

    removed = heap.pop()
    last_pos -= 1

    node_pos = 1
    left_pos = 2 * node_pos
    right_pos = left_pos + 1

    while (node_pos <= last_pos):
        # both sides can't be switched
        if ((left_pos > last_pos or heap[left_pos] < heap[node_pos]) and (right_pos > last_pos or heap[right_pos] < heap[node_pos])):
            return removed
        # right side can't be switched
        if (right_pos > last_pos or heap[right_pos] < heap[node_pos]):
            swap(heap, node_pos, left_pos)
            node_pos = left_pos
        # left side can't be switched
        elif (left_pos > last_pos or heap[left_pos] < heap[node_pos]):
            swap(heap, node_pos, right_pos)
            node_pos = right_pos
        # both sides can be switched
        else:
            if (heap[left_pos] > heap[right_pos]):
                swap(heap, node_pos, left_pos)
                node_pos = left_pos
            else:
                swap(heap, node_pos, right_pos)
                node_pos = right_pos
        left_pos = 2 * node_pos
        right_pos = 2 * node_pos + 1


def swap(heap, first, second):
    heap[first] = heap[first] ^ heap[second]
    heap[second] = heap[first] ^ heap[second]
    heap[first] = heap[first] ^ heap[second]


solution()
