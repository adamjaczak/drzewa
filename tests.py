import contextlib
import os
import random
from trees_logic import BST
import matplotlib.pyplot as plt
from pathlib import Path
import statistics
import time
import sys

sys.setrecursionlimit(15000)


def generate_random_data(n: int, min_val: int, max_val: int):
    return random.sample(range(min_val, max_val + 1), n)


def generate_plot(n_values, degenerate_times, balanced_times, title):
    plt.figure(figsize=(10, 6))

    plt.plot(n_values, degenerate_times, label="Drzewo zdegenerowane", color='red', marker='o', linewidth=2)
    plt.plot(n_values, balanced_times, label="Drzewo zbalansowane", color='green', marker='s', linewidth=2)

    plt.title(title, fontsize=14)
    plt.xlabel('Liczba elementów [n]', fontsize=11)
    plt.ylabel('Średni czas wykonania [s]', fontsize=11)

    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=12)

    plt.show()


def generate_tests():
    n_values = [500, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 8000, 10000]
    num_of_samples = 20

    results = {
        'creation': {'deg': [], 'bal': []},
        'max': {'deg': [], 'bal': []},
        'in_order': {'deg': [], 'bal': []}
    }

    for n in n_values:
        times = {
            'create_deg': [], 'create_bal': [],
            'max_deg': [], 'max_bal': [],
            'in_order_deg': [], 'in_order_bal': []
        }

        print(f"Rozpoczynam testy dla n = {n}")

        for _ in range(num_of_samples):
            data = generate_random_data(n, 1, n*10)
            data.sort()

            #Testy dla drzewa zdegenerowanego

            tree_deg = BST()

            start = time.perf_counter()
            tree_deg.build_degenerate(data)
            stop = time.perf_counter()
            times['create_deg'].append(stop - start)

            #To jest po to żeby nie mierzyć czasu wywołania funkcji print(). Wyjście jest skierowane na null
            with open(os.devnull, 'w') as devnull, contextlib.redirect_stdout(devnull):
                start = time.perf_counter()
                tree_deg.find_maximum()
                stop = time.perf_counter()
                times['max_deg'].append(stop-start)

                start = time.perf_counter()
                tree_deg.in_order_search()
                stop = time.perf_counter()
                times['in_order_deg'].append(stop-start)

            # Testy dla drzewa zbalansowanego

            tree_bal = BST()
            start = time.perf_counter()
            tree_bal.build_balanced(data)
            stop = time.perf_counter()
            times['create_bal'].append(stop - start)

            with open(os.devnull, 'w') as devnull, contextlib.redirect_stdout(devnull):
                start = time.perf_counter()
                tree_bal.find_maximum()
                stop = time.perf_counter()
                times['max_bal'].append(stop - start)

                start = time.perf_counter()
                tree_bal.in_order_search()
                stop = time.perf_counter()
                times['in_order_bal'].append(stop - start)

        results['creation']['deg'].append(statistics.mean(times['create_deg']))
        results['creation']['bal'].append(statistics.mean(times['create_bal']))

        results['max']['deg'].append(statistics.mean(times['max_deg']))
        results['max']['bal'].append(statistics.mean(times['max_bal']))

        results['in_order']['deg'].append(statistics.mean(times['in_order_deg']))
        results['in_order']['bal'].append(statistics.mean(times['in_order_bal']))

    generate_plot(n_values, results['creation']['deg'], results['creation']['bal'],"Czas tworzenia drezw w zależności od (n)")
    generate_plot(n_values, results['max']['deg'], results['max']['bal'], "Czas szukania wartości MAX w zależności od (n)")
    generate_plot(n_values, results['in_order']['deg'], results['in_order']['bal'], "Czas wyszukiwania in-order w zależności od (n)")


#generate_tests()
