from transaction_system import TransactionSystem
from performance import performance_comparison

system = TransactionSystem()

while True:

    print("\n========== Transaction Management System ==========")
    print("1. Display Transactions")
    print("2. Merge Sort Transactions")
    print("3. Binary Search")
    print("4. Linear Search")
    print("5. Performance Comparison")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        system.display_transactions()

    elif choice == "2":

        print("\n=============================== Before Merge Sort ==============================")
        system.display_transactions()

        system.sort_transactions()

        print("\n=============================== After Merge Sort ===============================")
        system.display_transactions()

    elif choice == "3":

        print("\n====== Binary Search ======")
        system.binary_search_transaction()

    elif choice == "4":

        print("\n====== Linear Search ======")
        system.linear_search_transaction()

    elif choice == "5":

        performance_comparison()

    elif choice == "6":

        print("\nThank you for using the Transaction Management System.")
        break

    else:

        print("\nInvalid choice. Please try again.")