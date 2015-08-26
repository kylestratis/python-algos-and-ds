# Node and Reference binary tree

class Binary_Tree:
    def __init__(self, root_object):
        self.key = root_object
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = Binary_Tree(new_node)
        else:
            t = Binary_Tree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = Binary_Tree(new_node)
        else:
            t = Binary_Tree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_value(self, obj):
        self.key = obj

    def get_root_value(self):
        return self.key

def build_tree():
    tree = Binary_Tree('a')
    tree.insert_left('b')
    tree.insert_right('c')
    b = tree.get_left_child()
    b.insert_right('d')
    c = tree.get_right_child()
    c.insert_left('e')
    c.insert_right('f')
    return tree

def preorder(tree):
    if tree != None:
        print tree.get_root_value()
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())

def postorder(tree):
    if tree != None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print tree.get_root_value()

def inorder(tree):
    if tree != None:
        inorder(tree.get_left_child())
        print tree.get_root_value()
        inorder(tree.get_right_child())