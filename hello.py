class Product:
    def __init__(self, product_name, product_price, product_description):
        self.product_name = product_name
        self.product_price = product_price
        self.product_description = product_description
        
    def get_name(self):
        return self.product_name

    def set_name(self, name):
        self.product_name = name


p1= Product("Laptop", 1000, "A high-performance laptop")
print(p1.get_name())  # Output: Laptop

    