from inventory import PharmacyInventory

inventory = PharmacyInventory()

while True:

    print("\n====== Pharmacy Inventory System ======")
    print("1. Display Medicines")
    print("2. Search Medicine")
    print("3. Insert Medicine")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        inventory.display()

    elif choice == "2":
        medicine_id = int(input("Enter Medicine ID: "))
        inventory.search(medicine_id)

    elif choice == "3":
        inventory.insert()

    elif choice == "4":
        print("Thank you.")
        break

    else:
        print("Invalid Choice.")