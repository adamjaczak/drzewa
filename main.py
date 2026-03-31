input_data = []

user_choice = 0

#sprawdzanie czy większy czy mniejszy i w zależności od tego dodawania na lewo lub prawo? DO ZROBIENIA


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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


def add_values(values: list):
    central_element = values[len(values) // 2]
    less_values = values[:central_element]
    greater_values = values[central_element+1:]
    root = insert(None, central_element)


def in_order_search(tree_root: Node):
    if not tree_root:
        return
    in_order_search(tree_root.left)
    print(tree_root.value, end=" ")
    in_order_search(tree_root.right)


def pre_order_search(tree_root: Node):
    if not tree_root:
        return
    print(tree_root.value, end=" ")
    pre_order_search(tree_root.left)
    pre_order_search(tree_root.right)


while user_choice != 3:
    print("\n1. Tworzenie drzewa metodą połowienia binarnego\n2. Tworzenie drzewa metodą dodawania z tablicy\n3. Wyjście")

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
        root = insert(None, values)
        print("In order\n")
        in_order_search(root)
        print("\nPre order\n")
        pre_order_search(root)
