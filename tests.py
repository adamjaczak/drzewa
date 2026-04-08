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


def generate_plot(n_values, degenerate_times, balanced_times):
    plt.figure(figsize=(10, 6))

    plt.plot(n_values, degenerate_times, label="Drzewo zdegenerowane", color='red', marker='o', linewidth=2)
    plt.plot(n_values, balanced_times, label="Drzewo zbalansowane", color='green', marker='s', linewidth=2)

    plt.title("Czas tworzenia drzew w zależności od (n) rozmiaru danych", fontsize=14)
    plt.xlabel('Liczba elementów [n]', fontsize=11)
    plt.ylabel('Średni czas wykonania [s]', fontsize=11)

    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=12)

    plt.show()


def generate_tests():
    n_values = [500, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 8000, 10000]
    num_of_samples = 20

    times_degenerate = []
    times_balanced = []

    for n in n_values:
        print(f"Rozpoczynam testy dla n = {n}")
        times_n_degenerate = []
        times_n_balanced = []

        test_samples = []
        for _ in range(num_of_samples):
            data = generate_random_data(n, 1, n*10)
            data.sort()
            test_samples.append(data)

        for data in test_samples:
            tree_deg = BST()
            start = time.perf_counter()
            tree_deg.build_degenerate(data)
            stop = time.perf_counter()
            times_n_degenerate.append(stop - start)

        for data in test_samples:
            tree_bal = BST()
            start = time.perf_counter()
            tree_bal.build_balanced(data)
            stop = time.perf_counter()
            times_n_balanced.append(stop - start)

        mean_degenerate = statistics.mean(times_n_degenerate)
        mean_balanced = statistics.mean(times_n_balanced)

        times_degenerate.append(mean_degenerate)
        times_balanced.append(mean_balanced)

    generate_plot(n_values, times_degenerate, times_balanced)


generate_tests()