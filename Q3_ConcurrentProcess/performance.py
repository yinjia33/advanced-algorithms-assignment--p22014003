from multithread import MultiThreadCalculator
from singlethread import SingleThreadCalculator


def performance_comparison():

    multi = MultiThreadCalculator()
    single = SingleThreadCalculator()

    multi_total = 0
    single_total = 0

    print("================ Performance Comparison ================\n")

    for i in range(1, 11):

        print(f"Round {i}")
        print("\nConcurrent Processing")
        multi_time = multi.run()
        print("\nSingle Thread")
        single_time = single.run()

        multi_total += multi_time
        single_total += single_time

        print(f"\nConcurrent Processing : {multi_time} ns")
        print(f"Single Thread         : {single_time} ns")

        if multi_time < single_time:
            print("Result : Concurrent Processing is faster.")
        elif multi_time > single_time:
            print("Result : Single Thread is faster.")
        else:
            print("Result : Same performance.")

        print("-" * 55)

    multi_average = multi_total / 10
    single_average = single_total / 10

    print("\n================ Average Execution Time ================\n")

    print(f"Concurrent Processing Average : {multi_average:.2f} ns")
    print(f"Single Thread Average         : {single_average:.2f} ns")

    print()

    if multi_average < single_average:
        print("Overall Result : Concurrent Processing is faster.")
    elif multi_average > single_average:
        print("Overall Result : Single Thread is faster.")
    else:
        print("Overall Result : Both have similar performance.")

    print("\n" + "="* 56)