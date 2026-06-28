import time
from factorial import factorial


class SingleThreadCalculator:

    def run(self):
        start = time.perf_counter_ns()

        self.calculate_factorial(50)
        self.calculate_factorial(100)
        self.calculate_factorial(200)

        end = time.perf_counter_ns()

        execution_time = end - start

        return execution_time

    def calculate_factorial(self, number):

        factorial(number)

        print(f"Factorial({number}) generated successfully.")