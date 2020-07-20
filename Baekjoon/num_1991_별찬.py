# name: 트리 순회
# date: July 17, 2020
# status: solved

from sys import stdin


class Node:
    def __init__(self, label, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root=None):
        self.root = None

    def insert(self, label_dict):
        self.root = Node('A')

        def insert_recursion(target_node):
            left_label, right_label = label_dict[target_node.label]
            if left_label != '.':
                target_node.left = Node(left_label)
                insert_recursion(target_node.left)
            if right_label != '.':
                target_node.right = Node(right_label)
                insert_recursion(target_node.right)

        insert_recursion(self.root)

    def traverse_in_preorder(self, node):
        if node:
            yield node.label
            for left in self.traverse_in_preorder(node.left):
                yield left
            for right in self.traverse_in_preorder(node.right):
                yield right

    def traverse_in_inorder(self, node):
        if node:
            for left in self.traverse_in_inorder(node.left):
                yield left
            yield node.label
            for right in self.traverse_in_inorder(node.right):
                yield right

    def traverse_in_postorder(self, node):
        if node:
            for left in self.traverse_in_postorder(node.left):
                yield left
            for right in self.traverse_in_postorder(node.right):
                yield right
            yield node.label


def solution():
    total_nodes = int(stdin.readline().strip())
    label_list = [stdin.readline().strip().split(' ')
                  for i in range(total_nodes)]
    label_dict = {current_label: [left_label, right_label]
                  for current_label, left_label, right_label in label_list}
    tree = Tree()
    tree.insert(label_dict)

    preorder_list = ''.join(tree.traverse_in_preorder(tree.root))
    print(preorder_list)

    inorder_list = ''.join(tree.traverse_in_inorder(tree.root))
    print(inorder_list)

    postorder_list = ''.join(tree.traverse_in_postorder(tree.root))
    print(postorder_list)


solution()
