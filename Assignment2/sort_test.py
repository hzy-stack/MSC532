from Assignment2.sort.quick_sort import quick_sort
from Assignment2.sort.merge_sort import merge_sort

import sys
import unittest
import random
import time

sys.setrecursionlimit(20000)


class TestSortPerformance(unittest.TestCase):
    results = []

    @classmethod
    def setUpClass(cls):
        # sizes to test: 10^3, 10^4, 10^5
        cls.sizes = [10 ** 3, 10 ** 4, 10 ** 5]
        cls.algorithms = [
            ("quick_sort", quick_sort),
            ("merge_sort", merge_sort),
        ]

    def measure_and_check(self, func, data):
        """Run func on a copy of data, assert correctness, and return elapsed time."""
        start = time.perf_counter()
        out = func(data.copy())
        elapsed = time.perf_counter() - start
        self.assertEqual(out, sorted(data),
                         f"{func.__name__} failed to sort correctly")
        return elapsed

    def test_performance_across_sizes(self):
        for n in self.sizes:
            random.seed(0)
            data_random = [random.randint(0, n) for _ in range(n)]
            data_sorted = list(range(n))
            data_reverse = list(range(n, 0, -1))
            datasets = {
                "random": data_random,
                "sorted": data_sorted,
                "reverse-sorted": data_reverse,
            }

            for algo_name, func in self.algorithms:
                for input_type, data in datasets.items():
                    with self.subTest(algo=algo_name, input=input_type, n=n):
                        t = self.measure_and_check(func, data)
                        # record for the final table
                        self.__class__.results.append((algo_name, input_type, n, t))

    @classmethod
    def tearDownClass(cls):
        header = f"{'Algorithm':<12} {'Input':<15} {'n':<8} {'Time (s)':<10}"
        print("\n" + header)
        print("-" * len(header))
        for algo, inp, n, t in cls.results:
            print(f"{algo:<12} {inp:<15} {n:<8} {t:<10.3f}")


if __name__ == "__main__":
    unittest.main()
