import time
from medicine import Medicine
from hashtable import HashTable

# =====================================
# Generate Sample Data
# =====================================

medicines = []

for i in range(1, 5001):
    medicines.append(
        Medicine(
            i,
            f"Medicine{i}",
            "Tablet",
            100,
            10.50
        )
    )

# =====================================
# Create Hash Table
# =====================================

hash_table = HashTable(10007)

for medicine in medicines:
    hash_table.insert(medicine)

# =====================================
# Linear Search (Array)
# =====================================

def array_search(data, medicine_id):
    for medicine in data:
        if medicine.medicine_id == medicine_id:
            return medicine
    return None

# =====================================
# Hash Table Search
# =====================================

def hash_search(medicine_id):
    return hash_table.search(medicine_id)

# =====================================
# Test Keys
# =====================================

search_keys = [
    1,        # Existing
    500,      # Existing
    2500,     # Existing
    4999,     # Existing
    9999      # Non-existing
]

REPEAT = 10000

print("=" * 55)
print(" HASH TABLE VS ARRAY SEARCH PERFORMANCE ")
print("=" * 55)

for key in search_keys:

    # -------------------------
    # Array Search Timing
    # -------------------------

    start = time.perf_counter_ns()

    for _ in range(REPEAT):
        array_search(medicines, key)

    end = time.perf_counter_ns()

    array_average = (end - start) / REPEAT

    # -------------------------
    # Hash Table Timing
    # -------------------------

    start = time.perf_counter_ns()

    for _ in range(REPEAT):
        hash_search(key)

    end = time.perf_counter_ns()

    hash_average = (end - start) / REPEAT

    # -------------------------
    # Display Result
    # -------------------------

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

print("\nPerformance comparison completed.")