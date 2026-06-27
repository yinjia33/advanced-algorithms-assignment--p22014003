import time
from transaction import Transaction
from merge_sort import merge_sort
from search import binary_search, linear_search


def performance_comparison():

    # ====================================
    # Generate Sample Data (5000 Records)
    # ====================================

    transactions = []

    for i in range(26001, 31001):

        transactions.append(
            Transaction(
                i,
                f"Customer{i}",
                f"Product{i}",
                100.00,
                "2026-06-01"
            )
        )

    # ====================================
    # Merge Sort Performance
    # ====================================

    start = time.perf_counter_ns()

    sorted_transactions = merge_sort(transactions)

    end = time.perf_counter_ns()

    merge_sort_time = end - start

    # ====================================
    # Search Keys
    # ====================================

    search_keys = [
        26001,
        27000,
        28500,
        30999,
        35000
    ]

    REPEAT = 10000

    print("\n" + "=" * 60)
    print(" MERGE SORT & SEARCH PERFORMANCE COMPARISON ")
    print("=" * 60)

    print(f"\nMerge Sort Time : {merge_sort_time} ns")

    print("\n" + "-" * 60)

    for key in search_keys:

        # -------------------------
        # Binary Search
        # -------------------------

        start = time.perf_counter_ns()

        for _ in range(REPEAT):
            binary_search(sorted_transactions, key)

        end = time.perf_counter_ns()

        binary_average = (end - start) / REPEAT

        # -------------------------
        # Linear Search
        # -------------------------

        start = time.perf_counter_ns()

        for _ in range(REPEAT):
            linear_search(sorted_transactions, key)

        end = time.perf_counter_ns()

        linear_average = (end - start) / REPEAT

        print(f"\nSearch Key : {key}")
        print(f"Binary Search Average : {binary_average:.2f} ns")
        print(f"Linear Search Average : {linear_average:.2f} ns")

        if binary_average < linear_average:
            print("Result : Binary Search is faster.")
        elif binary_average > linear_average:
            print("Result : Linear Search is faster.")
        else:
            print("Result : Same performance.")

        print("-" * 60)

    print("\nPerformance comparison completed!")