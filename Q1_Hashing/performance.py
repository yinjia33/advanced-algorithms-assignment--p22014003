import time
from medicine import Medicine
from hashtable import HashTable


def performance_comparison():

    medicines = []

    for i in range(26001, 31001):
        medicines.append(
            Medicine(
                i,
                f"Medicine{i}",
                "Tablet",
                100,
                10.50
            )
        )

    hash_table = HashTable(10007)

    for medicine in medicines:
        hash_table.insert(medicine)


    def array_search(data, medicine_id):
        for medicine in data:
            if medicine.medicine_id == medicine_id:
                return medicine
        return None


    def hash_search(medicine_id):
        return hash_table.search(medicine_id)


    search_keys = [
        26001,
        27000,
        28500,
        30999,
        35000
    ]

    REPEAT = 10000

    print("\n" + "=" * 55)
    print(" HASH TABLE VS ARRAY SEARCH PERFORMANCE ")
    print("=" * 55)

    for key in search_keys:

        start = time.perf_counter_ns()

        for _ in range(REPEAT):
            array_search(medicines, key)

        end = time.perf_counter_ns()

        array_average = (end - start) / REPEAT

        start = time.perf_counter_ns()

        for _ in range(REPEAT):
            hash_search(key)

        end = time.perf_counter_ns()

        hash_average = (end - start) / REPEAT

        print(f"\nSearch Key : {key}")
        print(f"Array Search Average      : {array_average:.2f} ns")
        print(f"Hash Table Average Search : {hash_average:.2f} ns")

        if hash_average < array_average:
            print("Result : Hash Table is faster.")
        elif hash_average > array_average:
            print("Result : Array is faster.")
        else:
            print("Result : Same performance.")

        print("-" * 55)

    print("\nPerformance comparison completed!")