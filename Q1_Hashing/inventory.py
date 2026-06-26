from medicine import Medicine
from hashtable import HashTable


class PharmacyInventory:

    def __init__(self):
        self.hash_table = HashTable(20)

        self.load_sample_data()

    def load_sample_data(self):

        medicines = [

            Medicine(101, "Paracetamol", "Tablet", 120, 7.50),
            Medicine(102, "Panadol", "Tablet", 60, 12.50),
            Medicine(103, "Vitamin C", "Supplement", 90, 25.00),
            Medicine(104, "Cough Syrup", "Syrup", 30, 16.90),
            Medicine(105, "Ibuprofen", "Tablet", 70, 11.80),
            Medicine(106, "Antacid", "Tablet", 100, 9.50),
            Medicine(107, "Fish Oil", "Supplement", 55, 39.90),
            Medicine(108, "Eye Drops", "Liquid", 45, 13.90)

        ]

        for medicine in medicines:
            self.hash_table.insert(medicine)

    def display(self):
        self.hash_table.display()

    def search(self, medicine_id):

        medicine = self.hash_table.search(medicine_id)

        if medicine:
            print("\nMedicine Found")
            print(medicine)
        else:
            print("\nMedicine Not Found")

    def insert(self):

        medicine_id = int(input("Medicine ID: "))
        name = input("Medicine Name: ")
        category = input("Category: ")
        quantity = int(input("Quantity: "))
        price = float(input("Price: "))

        medicine = Medicine(
            medicine_id,
            name,
            category,
            quantity,
            price
        )

        self.hash_table.insert(medicine)

        print("\nMedicine Added Successfully.")