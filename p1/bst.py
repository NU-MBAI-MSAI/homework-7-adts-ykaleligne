class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if other is None or not isinstance(other, Node):
            return False
        else:
            return self.val == other.val and self.left == other.left and self.right == other.right

    def __hash__(self):
        return hash(self.val)


class BST:
    def __init__(self, root=None):
        self.root = root

    def insert(self, number):
        # This is a nested function - it's only needed inside this function.
        def insert_node(tree):
            if number < tree.val and tree.left is not None:
                insert_node(tree.left)
            elif number < tree.val:
                tree.left = Node(number)
            elif number > tree.val and tree.right is not None:
                insert_node(tree.right)
            elif number > tree.val:
                tree.right = Node(number)
        if self.root is None:
            self.root = Node(number)
        else:
            insert_node(self.root)

    def traverse_pre(self):
        result = []

        def _traverse_pre(node):
            if node is not None:
                result.append(node.val)
                _traverse_pre(node.left)
                _traverse_pre(node.right)

        _traverse_pre(self.root)
        return result

    def traverse_post(self):
        result = []

        def _traverse_post(node):
            if node is not None:
                _traverse_post(node.left)
                _traverse_post(node.right)
                result.append(node.val)

        _traverse_post(self.root)
        return result

    def __eq__(self, other):
        return self.root == other.root

    @staticmethod
    def create(nodes):
        tree = BST()
        if nodes:
            tree.root = Node(nodes.pop(0))
            for node in nodes:
                tree.insert(node)
        return tree


if __name__ == '__main__':
    nodes = [25, 20, 30, 29, 35, 15, 22]
    tree = BST.create(nodes)
    print(tree.traverse_pre()) # -> This should return the list [25, 20, 15, 22, 30, 29, 35]
    print(tree.traverse_post()) # -> This should return the list [15, 22, 20, 29, 35, 30, 25]
