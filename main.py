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
        self.height = 1

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

    def find_minimum(self):
        print(self.value, end=" -> ")

        if self.left is None:
            print("X")
            return self.value

        return self.left.find_minimum()

    def find_maximum(self):
        print(self.value, end=" -> ")

        if self.right is None:
            print("X")
            return self.value

        return self.right.find_maximum()

    def find_value(self, target_value):
        if target_value == self.value:
            return self
        elif target_value < self.value and self.left is not None:
            return self.left.find_value(target_value)
        elif target_value > self.value and self.right is not None:
            return self.right.find_value(target_value)

        return None

    def remove_tree(self):
        if self.left is not None:
            self.left.remove_tree()
            self.left = None
        if self.right is not None:
            self.right.remove_tree()
            self.right = None

        self.value = None


def get_minimum_from_node(node: Node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def remove_element(n: Node, value):
    if n is None:
        return n

    if value < n.value:
        n.left = remove_element(n.left, value)
    elif value > n.value:
        n.right = remove_element(n.right, value)
    else:
        if n.left is None:
            return n.right
        elif n.right is None:
            return n.left

        potential_next_value = get_minimum_from_node(n.right)
        n.value = potential_next_value.value
        n.right = remove_element(n.right, potential_next_value.value)

    return n


def load_tree_from_file(filepath):

    if not os.path.exists(filepath):
        print("Błąd. Plik nie istnieje")
        return None

    new_root = None
    with open(filepath, 'r') as file:
        for line in file:
            value = int(line.strip())
            new_root = insert(new_root, value)

    print("Drzewo zostało zbudowane")
    return new_root


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
    left_height = node.left.height if node.left is not None else 0
    right_height = node.right.height if node.right is not None else 0
    node.height = 1 + max(left_height, right_height)
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


folder = Path("trees/")
if folder.exists() and folder.is_dir():
    for file in folder.glob("*.txt"):
        if file.is_file():
            tree = load_tree_from_file(str(file))
            trees.append(tree)
while user_choice != 4:

    print("\n1. Tworzenie drzewa metodą połowienia binarnego\n2. Tworzenie drzewa metodą dodawania z tablicy\n3. Operacje na drzewach z plików\n4. Wyjście")

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
        print("In order:")
        root.in_order_search()
        print("\nPre order:")
        root.pre_order_search()
        print(f"Wysokość drzewa: {root.height}")
        files = list(folder.glob("*.txt"))
        root.save_tree_to_file(f"trees/drzewo{len(files)+1}.txt")
        minimum = root.find_minimum()
        print(f"Wartość minimalna to: {minimum}")
        maximum = root.find_maximum()
        print(f"Wartość maksymalna to: {maximum}")
        remove_element(root, 9)
        root.pre_order_search()
    elif user_choice == 3:
        if len(trees) == 0:
            print("Brak drzew w plikach. Dodaj napierw drzewa")
            continue
        user_tree_choice = 0
        while user_tree_choice != len(trees) + 1:
            print(trees)
            print("Wybierz odpowiednie drzewo")
            for index, tree in enumerate(trees):
                if tree.value is not None:
                    print(f"{index+1}.", end=" ")
                    tree.pre_order_search()
                    print("")
            print(f"{len(trees)+1}. Wyjście")

            flag = False
            while not flag:
                try:
                    user_tree_choice = int(input())
                    if not 1 <= user_tree_choice <= len(trees) + 1:
                        print("Wybierz drzewo oznaczone cyfrą!")
                    else:
                        flag = True
                except ValueError:
                    print("Niepoprawna wartość. Spróbuj ponownie")

            if user_tree_choice == len(trees) + 1:
                break
            else:
                chosen_tree = trees[user_tree_choice - 1]
                chosen_tree_index = trees.index(chosen_tree)

                user_menu_choice = 0
                while user_menu_choice != 5:
                    print("1. Znajdź minimum\n2. Znajdź maksimum\n3. Usuń wartości\n"
                          "4. Wypisz wszystkie elementy (in-order) (pre-order)\n5. Usuń całe drzewo\n6. Wróć")
                    try:
                        user_menu_choice = int(input())
                        if not 1 <= user_menu_choice <= 6:
                            raise ValueError("Tylko wartości od 1-6")
                    except ValueError:
                        print("Wprowadź poprawną wartość")

                    if user_menu_choice == 1:
                        chosen_tree.find_minimum()
                    elif user_menu_choice == 2:
                        chosen_tree.find_maximum()
                    elif user_menu_choice == 3:
                        print("Ile elementów chcesz usunąć?")
                        n = int(input())
                        elements_to_remove = []
                        print("Podaj wartości do usunięcia")
                        for i in range(n):
                            elements_to_remove.append(int(input()))

                        for element in elements_to_remove:
                            remove_element(chosen_tree, element)

                        print("Pre-order po usunięciu")
                        chosen_tree.pre_order_search()
                    elif user_menu_choice == 4:
                        print("Pre - order")
                        chosen_tree.pre_order_search()
                        print("In - order")
                        chosen_tree.in_order_search()
                    elif user_menu_choice == 5:
                        chosen_tree.remove_tree()
                        file = Path(f"trees/drzewo{chosen_tree_index + 1}.txt")
                        if file.exists() and file.is_file():
                            file.unlink()
                        break

