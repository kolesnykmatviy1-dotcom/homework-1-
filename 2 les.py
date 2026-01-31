class Product:
     def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

     def calculate_total_price(self):
        return self.price * self.quantity

     def display_info(self):
        print(f"goods: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantily: {self.quantity}")
        print(f"Total cost: {self.calculate_total_price()}")
product1 = Product("Milk", 25, 2)
product1.display_info()