class Transaction:

    def __init__(self, transaction_id, customer_name, product_name, amount, transaction_date):
        self.transaction_id = transaction_id
        self.customer_name = customer_name
        self.product_name = product_name
        self.amount = amount
        self.transaction_date = transaction_date

    def __str__(self):
        return (
            f"{self.transaction_id:<10}"
            f"{self.customer_name:<15}"
            f"{self.product_name:<18}"
            f"RM {self.amount:<10.2f}"
            f"{self.transaction_date}"
        )

    def display_details(self):
        print(f"Transaction ID : {self.transaction_id}")
        print(f"Customer Name  : {self.customer_name}")
        print(f"Product Name   : {self.product_name}")
        print(f"Amount         : RM {self.amount:.2f}")
        print(f"Date           : {self.transaction_date}")