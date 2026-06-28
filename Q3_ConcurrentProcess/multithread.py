import threading
import time
from factorial import factorial


class MultiThreadCalculator:

    def __init__(self):
        self.results = {}

    def calculate_factorial(self, number):
        self.results[number] = factorial(number)

        print(f"Factorial({number}) generated successfully.")

    def run(self):

        start = time.perf_counter_ns()

        thread1 = threading.Thread(
            target=self.calculate_factorial,
            args=(50,)
        )

        thread2 = threading.Thread(
            target=self.calculate_factorial,
            args=(100,)
        )

        thread3 = threading.Thread(
            target=self.calculate_factorial,
            args=(200,)
        )

        thread1.start()
        thread2.start()
        thread3.start()

        thread1.join()
        thread2.join()
        thread3.join()

        end = time.perf_counter_ns()

        execution_time = end - start

        return execution_time