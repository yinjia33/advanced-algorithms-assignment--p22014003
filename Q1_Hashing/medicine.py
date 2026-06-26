class Medicine:
    def __init__(self, medicine_id, name, category, quantity, price):
        self.medicine_id = medicine_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return (
            f"{self.medicine_id:<8}"
            f"{self.name:<20}"
            f"{self.category:<15}"
            f"{self.quantity:<10}"
            f"RM {self.price:.2f}"
        )