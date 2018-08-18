# _*_ coding:utf-8 _*_


class Node(object):
    """树的节点"""
    def __init__(self, item):
        self.elem = item
        self.l_child = None
        self.r_child = None


class Tree(object):
    """二叉树"""
    def __init__(self):
        self.root = None

    def add(self, item):
        pass

