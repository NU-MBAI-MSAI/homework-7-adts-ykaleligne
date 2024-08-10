from queue import LifoQueue, Queue


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

    def traverse_inorder(self):
        result = []
        stack = LifoQueue()
        current = self.root

        while not stack.empty() or current is not None:
            while current is not None:
                stack.put(current)
                current= current.left

            current = stack.get ()
            result.append(current.val)
            current = current.right

        return result

    def breadth_first_traversal(self):
        result = []
        queue= Queue()

        if self.root is  not None:
            queue.put(self.root)

        while not queue.empty():
            node = queue.get()
            result.append(node.val)
            if node.left is not None:
                queue.put(node.left)
            if node.right is not None:
                queue.put(node.right)
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
    nodes = [7, 10, 5, 9, 3, 6]
    bst = BST.create(nodes)
    print(bst.traverse_inorder()) # -> Should be [3, 5, 6, 7, 9, 10]
    print(bst.breadth_first_traversal())  # -> Should be [7, 5, 10, 3, 6, 9]
