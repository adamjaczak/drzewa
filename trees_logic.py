class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Nodeo(value)
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    break
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = Node(value)
                    break
                current = current.right
            else:
                break

    def build_balanced(self, values):
        def build(arr):
            if not (arr):
                return None
            mid = len(arr) // 2
            node = Node(arr[mid])
            node.left = build(arr[:mid])
            node.right = build(arr[mid + 1:])
            return node

        self.root = build(values)

    def build_degenerate(self, values):
        self.root = None
        for val in values:
            self.insert(val)

    def get_height(self):
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        return height(self.root)

    def find_minimum(self):
        if not self.root:
            print("Drzewo puste. Brak wartości minimalnej")
            return None
        current = self.root
        path = []
        while current.left:
            path.append(str(current.value))
            current = current.left
        path.append(str(current.value))
        print("Ścieżka znajdowania minimum: ", " -> ".join(path))
        return current.value

    def find_maximum(self):
        if not self.root:
            print("Drzewo puste. Brak wartości maksymalnej")
            return None
        current = self.root
        path = []
        while current.right:
            path.append(str(current.value))
            current = current.right
        path.append(str(current.value))
        print("Ścieżka znajdowania minimum: ", " -> ".join(path))
        return current.value

    def remove_element(self, value):
        def remove(node, val):
            if not node:
                return node
            if val < node.value:
                node.left = remove(node.left, val)
            elif val > node.value:
                node.right = remove(node.right, val)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left

                temp = node.right
                while temp.left:
                    temp = temp.left
                node.value = temp.value
                node.right = remove(node.right, node.value)

            return node

        self.root = remove(self.root, value)

    def in_order_search(self):
        def in_order(node):
            if node:
                in_order(node.left)
                print(node.value, end=" ")
                in_order(node.right)

        in_order(self.root)
        print()

    def pre_order_search(self):
        def pre_order(node):
            if node:
                print(node.value, end=" ")
                pre_order(node.left)
                pre_order(node.right)

        pre_order(self.root)
        print()

    def remove_tree(self):
        def post_order_delete(node):
            if node:
                post_order_delete(node.left)
                post_order_delete(node.right)
                print(f"Usuwanie następującego węzła: {node.value}")

        post_order_delete(self.root)
        self.root = None
        print("Drzewo zostało usunięte")
