import timeit
import random
from sort_algorithms import *
import pandas as pd

def read_code_file(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
    return code

def get_algorithm_list():
    return ['bubble_sort','insertion_sort','merge_sort','quick_sort','tim_sort']

def analyze_performance(code):
    time_ex = timeit.repeat(code, number = 1000, repeat = 30)
    return time_ex

def get_input_list(num_elements = 100000):
    random.seed(87)
    random_ints = [random.randint(0, num_elements) for _ in range(num_elements)]
    return random_ints

def get_code_to_execute(algorithm, input_list):
    setup_code = f"from sort_algorithms import {algorithm}"
    code_to_execute = f"{setup_code}\n{algorithm}({input_list})"
    return code_to_execute

if __name__ == '__main__':
    input_list = get_input_list(100)
    algorithm_list = get_algorithm_list()
    algorithm_performance = {}
    for algorithm in algorithm_list:
        code = get_code_to_execute(algorithm,input_list)
        time_ex = analyze_performance(code)
        algorithm_performance[algorithm] = time_ex
    algorithm_performance_df = pd.DataFrame(algorithm_performance)
    algorithm_performance_df.to_csv('algorithm_performance_100.csv')