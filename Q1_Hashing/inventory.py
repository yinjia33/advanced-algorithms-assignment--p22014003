from medicine import Medicine
from hashtable import HashTable


class PharmacyInventory:

    def __init__(self):
        self.hash_table = HashTable(20)

        self.load_sample_data()

    def load_sample_data(self):

        medicines = [

            Medicine(26001, "Paracetamol", "Tablet", 120, 7.50),
            Medicine(26002, "Panadol", "Tablet", 60, 12.50),
            Medicine(26003, "Vitamin C", "Supplement", 90, 25.00),
            Medicine(26004, "Cough Syrup", "Syrup", 30, 16.90),
            Medicine(26005, "Ibuprofen", "Tablet", 70, 11.80),
            Medicine(26006, "Antacid", "Tablet", 100, 9.50),
            Medicine(26007, "Fish Oil", "Supplement", 55, 39.90),
            Medicine(26008, "Eye Drops", "Liquid", 45, 13.90)

        ]

        for medicine in medicines:
            self.hash_table.insert(medicine)

    def display(self):
        self.hash_table.display()

    def search(self, medicine_id):

        medicine = self.hash_table.search(medicine_id)

        if medicine:
            print("\n========== Medicine Found ==========")
            medicine.display_details()
            print("=" * 36)
        else:
            print("\nMedicine Not Found!")

    def insert(self):

        medicine_id = self.hash_table.get_next_id()
        print(f"Medicine ID (Auto): {medicine_id}")
        name = input("Medicine Name     : ")
        category = self.choose_category()
        quantity = int(input("Quantity         : "))
        price = float(input("Price            : RM "))

        medicine = Medicine(
            medicine_id,
            name,
            category,
            quantity,
            price
        )

        self.hash_table.insert(medicine)

        print("\nMedicine Added Successfully!")

    def update(self):

        medicine_id = int(input("Enter Medicine ID to Update: "))

        medicine = self.hash_table.search(medicine_id)

        if medicine is None:
            print("\nMedicine Not Found!")
            return

        while True:

            print("\n========== Update Medicine ==========")
            medicine.display_details()
            print("=" * 37)

            print("\nWhat would you like to update?")
            print("1. Name")
            print("2. Category")
            print("3. Quantity")
            print("4. Price")
            print("5. Update All")
            print("6. Finish")

            choice = input("Enter your choice: ")

            if choice == "1":
                medicine.name = input("Enter New Name: ")
                print("\nName Updated Successfully!")

            elif choice == "2":
                medicine.category = self.choose_category()
                print("\nCategory Updated Successfully!")

            elif choice == "3":
                medicine.quantity = int(input("Enter New Quantity: "))
                print("\nQuantity Updated Successfully!")

            elif choice == "4":
                medicine.price = float(input("Enter New Price: RM "))
                print("\nPrice Updated Successfully!")

            elif choice == "5":
                medicine.name = input("Enter New Name: ")
                medicine.category = self.choose_category()
                medicine.quantity = int(input("Enter New Quantity: "))
                medicine.price = float(input("Enter New Price: RM "))

                print("\nMedicine Updated Successfully!")
            elif choice == "6":
                print("Update Finished!")
                break


            else:
                print("Invalid Choice!")

    def delete(self):
        medicine_id = int(input("Enter Medicine ID to Delete: "))
        self.hash_table.delete(medicine_id)

    def choose_category(self):
        categories = {
            "1": "Tablet",
            "2": "Syrup",
            "3": "Capsule",
            "4": "Liquid",
            "5": "Supplement",
            "6": "Ointment"
        }

        while True:
            print("\nSelect Category")
            for key, value in categories.items():
                print(f"{key}. {value}")

            choice = input("Enter your choice: ")

            if choice in categories:
                return categories[choice]

            print("Invalid choice! Please try again.")