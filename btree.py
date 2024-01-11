class Node:
    def __init__(self, data):

        # self.title = data.title
        # self.author = data.author
        # self.isbn = data.isbn
        # self.price = data.price
        # self.category = data.category
        # self.available = data.available

        self.key = data.isbn
        self.data = data
        self.left = None
        self.right = None

    def insert(self, node, data):
        if node is None:
            print(f'>>>[NODE ISBN {data.isbn}]')
            return Node(data)

        if data.isbn < node.key:
            node.left = self.insert(node.left, data)
        elif data.isbn > node.key:
            node.right = self.insert(node.right, data)

        return node

    def search(self, root, key):

            if root is None or root.key == key:
                return root

            if key < root.key:
                return self.search(root.left, key)

            return self.search(root.right, key)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()