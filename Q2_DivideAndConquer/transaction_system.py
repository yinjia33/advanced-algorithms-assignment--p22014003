from transaction import Transaction
from merge_sort import merge_sort
from search import binary_search, linear_search
import merge_sort

class TransactionSystem:

    def __init__(self):

        self.sorted = False

        self.transactions = [

            Transaction(26010, "Alice", "Keyboard", 120.00, "2026-05-02"),
            Transaction(26003, "John", "Mouse", 35.90, "2026-04-18"),
            Transaction(26015, "Emma", "Monitor", 599.00, "2026-06-01"),
            Transaction(26001, "Chris", "Laptop", 3299.00, "2026-03-20"),
            Transaction(26008, "David", "SSD", 420.00, "2026-04-30"),
            Transaction(26006, "Lisa", "Headset", 150.00, "2026-05-11"),
            Transaction(26012, "Sarah", "Printer", 690.00, "2026-05-26"),
            Transaction(26005, "Mike", "USB Drive", 45.00, "2026-04-08"),
            Transaction(26009, "Kevin", "Router", 289.00, "2026-05-19"),
            Transaction(26002, "Amy", "Webcam", 230.00, "2026-03-25")

        ]

    def display_transactions(self):

        print("\n=============================== Transaction List ===============================")
        print("-" * 80)
        print(f"{'ID':<10}{'Customer':<15}{'Product':<18}{'Amount':<15}Date")
        print("-" * 80)

        for transaction in self.transactions:
            print(transaction)

        print("-" * 80)

    def sort_transactions(self):

        if self.sorted:
            print("\nTransactions are already sorted.")
            return

        merge_sort.recursive_calls = 0

        self.transactions = merge_sort.merge_sort(self.transactions)

        self.sorted = True

        print("\nTransactions Sorted Successfully!")
        print(f"Total Recursive Calls : {merge_sort.recursive_calls}")

    def binary_search_transaction(self):

        if not self.sorted:
            print("\nPlease sort the transactions first using Merge Sort!")
            return

        while True:

            try:
                transaction_id = int(input("Enter Transaction ID: "))
                break

            except ValueError:
                print("Please enter a valid Transaction ID.")

        transaction = binary_search(self.transactions, transaction_id)

        if transaction:

            print("\n========== Transaction Found ==========")
            transaction.display_details()
            print("=" * 39)

        else:

            print("\nTransaction Not Found!")

    def linear_search_transaction(self):

        transaction_id = int(input("Enter Transaction ID: "))

        transaction = linear_search(self.transactions, transaction_id)

        if transaction:

            print("\n========== Transaction Found ==========")
            transaction.display_details()
            print("=" * 39)

        else:

            print("\nTransaction Not Found!")