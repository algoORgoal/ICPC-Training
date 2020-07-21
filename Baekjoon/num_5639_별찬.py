# name: Binary Search Tree
# date: July 20, 2020
# status: solved

import sys
sys.setrecursionlimit(10 ** 4 * 2)


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        node = self.search(self.root, key)
        if key < node.key:
            node.left = Node(key)
        else:  # there is no duplicate.
            node.right = Node(key)

    def search(self, node, key):
        if (not node.left and key < node.key) or (not node.right and key > node.key):
            return node
        if key < node.key:
            return self.search(node.left, key)
        if key > node.key:
            return self.search(node.right, key)
        # both sides don't exist or key is matched
        return node

    def traverse_in_postorder(self, node):
        if node:
            for key in self.traverse_in_postorder(node.left):
                yield key
            for key in self.traverse_in_postorder(node.right):
                yield key
            yield node.key

    def traverse_in_postorder2(self, node):
        if node.left:
            self.traverse_in_postorder2(node.left)
        if node.right:
            self.traverse_in_postorder2(node.right)
        print(node.key)

    def traverse_in_postorder_using_tree(self):
        stack = []
        stack.append(self.root)
        current = self.root
        while True:
            while current:
                if current.right:
                    stack.append(current.right)
                stack.append(current)
                current = current.left
            while stack:
                current = stack.pop()
                if not stack:
                    return
                if stack[len(stack) - 1] is current.right:
                    node = current
                    current = stack.pop()
                    stack.append(node)
                    break
                else:
                    print(current.key)


def solution():
    tree = Tree()
    while True:
        line = sys.stdin.readline()
        if line == '':
            break
        key = int(line.strip())
        tree.insert(key)
        if '\n' not in line:
            break
    tree.traverse_in_postorder_using_tree()


solution()
