import os.path
from pathlib import Path
from trees_logic import BST


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
        user_input = input("Podaj 10 liczb oddzielonych spacją: ")
        raw_values = [int(x) for x in user_input.split()]
        values = list(set(raw_values))[:10]
        values.sort()
        print(f"Posortowane dane wejściowe: {values}")

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
        if not tree_degenerate.root:
            print("Brak danych")
            continue
        target = int(input("Z którego drzewa usunąć? (1 - Zbalansowane, 2 - Zdegenerowane)"))
        selected = tree_balanced if target == 1 else tree_degenerate

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
        if not tree_balanced.root:
            print("Brak danych")
            continue
        target = int(input("Które drzewo usunąć (1 - Zbalansowane, 2 - Zdegenerowane)"))
        if target == 1:
            tree_balanced.remove_tree()
        elif target == 2:
            tree_degenerate.remove_tree()
        else:
            print("Niepoprawny wybór")
    elif user_choice == 7:
        print("Koniec programu")
        break
    else:
        print("Niepoprawny wybór. Spróbuj ponownie.")