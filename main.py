import os.path
from pathlib import Path
from trees_logic import BST
from tests import generate_random_data
import sys
sys.setrecursionlimit(15000)

tree_balanced = BST()
tree_degenerate = BST()
values = []

while True:
    print("1. Wczytaj dane i zbuduj drzewa")
    print("2. Wyświetl drzewa")
    print("3. Znajdź minumum")
    print("4. Znajdź maksimum")
    print("5. Usuń węzły z wybranego drzewa")
    print("6. Równoważenie DSW")
    print("7. Usuń całe drzewo (post-order)")
    print("8. Wyjście")

    try:
        user_choice = int(input("Podaj opcję: "))
    except ValueError:
        print("Błędna wartość. Spróbuj ponownie")
        continue

    if user_choice == 1:
        try:
            choice = int(input("Jakie dane chcesz? (1 - z klawiatury, 2 - z generatora)"))
        except ValueError:
            print("Niepoprawna wartość wejściowa")
        if choice == 1:
            user_input = input("Podaj 10 liczb oddzielonych spacją: ")
            raw_values = [int(x) for x in user_input.split()]
            values = list(set(raw_values))[:10]
            values.sort()
            print(f"Posortowane dane wejściowe: {values}")
        elif choice == 2:
            values = generate_random_data(100, 1, 1000)
            values.sort()
        else:
            print("Niepoprawna wartość wejściowa")
            continue

        tree_balanced.build_balanced(values)
        tree_degenerate.build_degenerate(values)
        print("Zbudowano drzewa")
    elif user_choice == 2:
        if not tree_balanced.root:
            print("Brak danych")
            continue

        print("Drzewo zbalansowane:")
        print(f"Wysokość: {tree_balanced.get_height()}")
        print(f"In-order: ", end="")
        tree_balanced.in_order_search()
        print(f"Pre-order: ", end="")
        tree_balanced.pre_order_search()

        print("Drzewo zdegenerowane:")
        print(f"Wysokość: {tree_degenerate.get_height()}")
        print(f"In-order: ", end="")
        tree_degenerate.in_order_search()
        print(f"Pre-order: ", end="")
        tree_degenerate.pre_order_search()
    elif user_choice == 3:
        if not tree_balanced.root:
            print("Brak danych")
            continue
        print("Drzewo zbalansowane: ")
        tree_balanced.find_minimum()
        print("Drzewo zdegenerowane: ")
        tree_degenerate.find_minimum()
    elif user_choice == 4:
        print("Drzewo zbalansowane: ")
        tree_balanced.find_maximum()
        print("Drzewo zdegenerowane: ")
        tree_degenerate.find_maximum()
    elif user_choice == 5:
        if not tree_degenerate.root and not tree_balanced.root:
            print("Brak danych")
            continue
        target = int(input("Z którego drzewa usunąć? (1 - Zbalansowane, 2 - Zdegenerowane)"))
        if target == 1:
            if not tree_balanced.root:
                print("Drzewo zbalansowane jest puste")
                continue
            selected = tree_balanced
        elif target == 2:
            if not tree_degenerate.root:
                print("Drzewo zdegenerowane jest puste")
                continue
            selected = tree_degenerate

        try:
            n = int(input("Ile węzłów chcesz usunąć?: "))
            for _ in range(n):
                val = int(input("Wartość do usunięcia: "))
                selected.remove_element(val)
            print("Węzły zostały usunięte")
        except ValueError:
            print("Błąd. Podano niepoprawny format danych")
    elif user_choice == 6:
        continue
    elif user_choice == 7:
        if not tree_balanced.root and not tree_degenerate.root:
            print("Brak danych")
            continue
        target = int(input("Które drzewo usunąć (1 - Zbalansowane, 2 - Zdegenerowane)"))
        if target == 1:
            if tree_balanced.root:
                tree_balanced.remove_tree()
            else:
                print("Drzewo zbalansowane jest puste")
        elif target == 2:
            if tree_degenerate.root:
                tree_degenerate.remove_tree()
            else:
                print("Drzewo zdegenerowane jest puste")
        else:
            print("Niepoprawny wybór")
    elif user_choice == 8:
        print("Koniec programu")
        break
    else:
        print("Niepoprawny wybór. Spróbuj ponownie.")