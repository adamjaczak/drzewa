import random
from trees_logic import BST


def generate_random_data(n: int, min_val: int, max_val: int):
    data = []
    for _ in range(n):
        data.append(random.randint(min_val, max_val))
    return data


def generate_data_for_tests():
    n_values = [500, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 8000, 10000]
    tests_data = []
    for n in n_values:
        n_data = generate_random_data(n, 1, n*10)
        n_data.sort()
        tests_data.append(n_data)

    return tests_data


