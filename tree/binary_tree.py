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
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.l_child is None:
                cur_node.l_child = node
                return
            else:
                queue.append(cur_node.l_child)
            if cur_node.r_child is None:
                cur_node.r_child = node
                return
            else:
                queue.append(cur_node.r_child)

    def breath_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=' ')
            if cur_node.l_child is not None:
                queue.append(cur_node.l_child)
            if cur_node.r_child is not None:
                queue.append(cur_node.r_child)

    def preorder(self, node):
        """先序遍历"""
        if not node:
            return
        print(node.elem, end=' ')
        self.preorder(node.l_child)
        self.preorder(node.r_child)

    def inorder(self, node):
        """中序遍历"""
        if not node:
            return
        self.inorder(node.l_child)
        print(node.elem, end=' ')
        self.inorder(node.r_child)

    def postorder(self, node):
        """后序遍历"""
        if not node:
            return
        self.postorder(node.l_child)
        self.postorder(node.r_child)
        print(node.elem, end=' ')


if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.breath_travel()
    print(' ')
    tree.preorder(tree.root)
    print(' ')
    tree.inorder(tree.root)
    print(' ')
    tree.postorder(tree.root)
    print(' ')



