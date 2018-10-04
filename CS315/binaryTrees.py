#!/usr/local/bin/python3
# Kelly Sovacool
# CS315 Homework 8
import binarytree


def main():
    root = Node(15)
    for key in [6, 18, 3, 7, 17, 20, 2, 4, 13, 9, 5]:
        root.insert(Node(key))

    binarytree.show(root)
    print(root.search(6).predecessor)
    print(root.search(6).successor)


class Node(binarytree.Node):
    nil = None

    def __init__(self, key):
        self.key = key
        self.left = Node.nil
        self.right = Node.nil

    @property
    def predecessor(self):
        # rightmost element of left subtree
        return self.left.maximum

    @property
    def successor(self):
        # leftmost element of right subtree
        return self.right.minimum

    def search(self, key):
        x = self
        while x != Node.nil and key != x.key:
            x = x.left if key < x.key else x.right
        return x

    @property
    def minimum(self):
        x = self
        while x.left != Node.nil:
            x = x.left
        return x

    @property
    def maximum(self):
        x = self
        while x.right != Node.nil:
            x = x.right
        return x

    def insert(self, new_node):
        x = self
        pos = Node.nil
        parent = Node.nil
        while x != Node.nil:
            parent = x
            if new_node.key < x.key:
                x = x.left
                pos = 'left'
            else:
                x = x.right
                pos = 'right'
        if pos == 'left':
            parent.left = new_node
        elif pos == 'right':
            parent.right = new_node
        else:
            raise ValueError('position of parent %s is %s'.format(parent, pos))

    @property
    def walk(self):
        sorted_list = list()
        Node.in_order_tree_walk(self, sorted_list)
        return sorted_list

    @staticmethod
    def in_order_tree_walk(x, sorted_list):
        if x != Node.nil:
            Node.in_order_tree_walk(x.left, sorted_list)
            sorted_list.append(x.key)
            Node.in_order_tree_walk(x.right, sorted_list)


binarytree.customize(
    node_init=lambda val: Node(val),
    node_class=Node,
    null_value=None,
    value_attr='key',
    left_attr='left',
    right_attr='right'
)

main()
