# name: 트리
# date: July 17, 2020
# status: solved

from sys import stdin


class Node:
    def __init__(self, label, parent=None):
        self.label = label
        self.parent = parent
        self.children = []


class Tree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, label, parent_label):
        if not self.root:
            self.root = Node(label)
            return self.root
        parent = self.traverse_in_level_order(parent_label)
        child = Node(label, parent)
        parent.children.append(child)
        return child

    def traverse_in_level_order(self, label):
        queue = []
        queue.append(self.root)

        while queue:
            current = queue.pop(0)
            if current.label == label:
                return current
            if current.children:
                queue += [node for node in current.children]

    def remove(self, label):
        if self.root.label == label:
            self.root = None
            return

        target = self.traverse_in_level_order(label)
        parent = target.parent
        for child_index in range(len(parent.children)):
            if parent.children[child_index].label == label:
                parent.children.pop(child_index)
                return target
        return -1

    def print_labels(self):
        queue = []
        queue.append(self.root)

        printed_list = []
        while queue:
            current = queue.pop(0)
            printed_list.append(current.label)
            if current.children:
                queue += [node for node in current.children]
        print(printed_list, sep=" ")

    def count_leaves(self, node):
        if not node:
            return 0
        if not node.children:
            return 1
        total_leaves = 0
        for child in node.children:
            total_leaves += self.count_leaves(child)
        return total_leaves


def create_tree(label, label_pair_list):
    tree = Tree()
    queue = []
    queue.append(label)
    while queue:
        target_label = queue.pop(0)
        for current_label, parent_label in label_pair_list:
            if parent_label == target_label:
                tree.insert(current_label, parent_label)
                queue.append(current_label)
    return tree


def solution():
    total_nodes = int(stdin.readline())
    parent_label_list = list(map(int, stdin.readline().strip().split(' ')))
    label_to_remove = int(stdin.readline().strip())
    tree = Tree()
    label_pair_list = [[label, parent_label_list[label]]
                       for label in range(len(parent_label_list))]
    tree = create_tree(-1, label_pair_list)
    tree.remove(label_to_remove)
    total_leaves = tree.count_leaves(tree.root)
    print(total_leaves)


solution()
