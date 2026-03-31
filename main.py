import os.path
from pathlib import Path
input_data = []

user_choice = 0

trees = []

#sprawdzanie czy większy czy mniejszy i w zależności od tego dodawania na lewo lub prawo? DO ZROBIENIA


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def in_order_search(self):
        if self.left is not None:
            self.left.in_order_search()
        print(self.value, end=" ")
        if self.right is not None:
            self.right.in_order_search()

    def pre_order_search(self):
        print(self.value, end=" ")
        if self.left is not None:
            self.left.pre_order_search()
        if self.right is not None:
            self.right.pre_order_search()

    def save_tree_to_file(self, filepath):
        with open(filepath, 'w') as file:
            def write_preorder(current_node):
                if current_node is None:
                    return
                file.write(f"{current_node.value}\n")
                write_preorder(current_node.left)
                write_preorder(current_node.right)
            write_preorder(self)

    def load_tree_from_file(self, filepath):

        if not os.path.exists(filepath):
            print("Błąd. Plik nie istnieje")
            return None
        with open(filepath, 'r') as file:
            for line in file:
                value = int(line.strip())
                if self is None:
                    self.value = value
                else:
                    insert(self, value)

        print("Drzewo zostało zbudowane")
        return root


def insert(node, value):
    if node is None:
        return Node(value)

    if value < node.value:
        if node.left is None:
            node.left = Node(value)
        else:
            insert(node.left, value)
    elif value > node.value:
        if node.right is None:
            node.right = Node(value)
        else:
            insert(node.right, value)

    return node


def add_values(values: list, basic_root=None):
    if not values:
        return basic_root

    central_element = len(values) // 2
    print(central_element)

    if basic_root is None:
        basic_root = Node(values[central_element])
    else:
        insert(basic_root, values[central_element])

    add_values(values[:central_element], basic_root)
    add_values(values[central_element + 1:], basic_root)

    return basic_root


while user_choice != 4:
    folder = Path("trees/")
    if folder.exists() and folder.is_dir():
        for file in folder.glob("*.txt"):
            if file.is_file():
                tree = Node(None)
                tree.load_tree_from_file(str(file))
                trees.append(tree)

    print("\n1. Tworzenie drzewa metodą połowienia binarnego\n2. Tworzenie drzewa metodą dodawania z tablicy\n3.Wypisz drzewa z pliku\n4. Wyjście")

    flag = False

    while not flag:
        try:
            user_choice = int(input())
            flag = True
        except ValueError:
            print("Niepoprawna wartość wybrana z menu. Wpisz ponownie\n")

    if user_choice == 1:
        print("Podaj max. 10 wartości oddzielonych spacją\n")
        values = [int(x) for x in input().split(' ')]
        values.sort()
        print(f"Posortowane wartości wejściowe: {values}")
        root = add_values(values)
        print("In order\n")
        root.in_order_search()
        print("\nPre order\n")
        root.pre_order_search()
        root.save_tree_to_file("trees/drzewo1.txt")
    elif user_choice == 3:
        for tree in trees:
            tree.pre_order_search()