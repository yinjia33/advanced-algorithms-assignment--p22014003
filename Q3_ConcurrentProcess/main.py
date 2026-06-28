from multithread import MultiThreadCalculator
from singlethread import SingleThreadCalculator
from performance import performance_comparison

multi = MultiThreadCalculator()
single = SingleThreadCalculator()

while True:

    print("\n========== Concurrent Processing System ==========")
    print("1. Run Concurrent Processing")
    print("2. Run Single Thread")
    print("3. Performance Comparison")
    print("4. Exit")

    choice = input("Enter your choice: ")
    print()

    if choice == "1":

        execution_time = multi.run()

        print("\nConcurrent Processing Completed Successfully!")
        print(f"Execution Time : {execution_time} ns")

    elif choice == "2":

        execution_time = single.run()

        print("\nSingle Thread Processing Completed Successfully!")
        print(f"Execution Time : {execution_time} ns")

    elif choice == "3":

        performance_comparison()

    elif choice == "4":

        print("\nThank You!")
        break

    else:

        print("\nInvalid Choice!")