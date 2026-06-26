class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, medicine):
        index = self.hash_function(medicine.medicine_id)
        start = index

        while self.table[index] is not None:

            if self.table[index].medicine_id == medicine.medicine_id:
                self.table[index] = medicine
                return

            index = (index + 1) % self.size

            if index == start:
                raise Exception("Hash Table is Full")

        self.table[index] = medicine

    def search(self, medicine_id):
        index = self.hash_function(medicine_id)
        start = index

        while self.table[index] is not None:

            if self.table[index].medicine_id == medicine_id:
                return self.table[index]

            index = (index + 1) % self.size

            if index == start:
                break

        return None

    def display(self):
        print("\nCurrent Medicine Inventory")
        print("-" * 70)
        print(f"{'ID':<8}{'Name':<20}{'Category':<15}{'Qty':<10}Price")
        print("-" * 70)

        for item in self.table:
            if item is not None:
                print(item)

        print("-" * 70)