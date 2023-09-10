
# Create class STORE to keep track of Products ( Product Code, Name and price). 
# Display menu of all products to user. Generate bill as per order.

class Product:
    def __init__(self, product_code, name, price):
        self.product_code = product_code
        self.name = name
        self.price = price

class Store:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def display_menu(self):
        print("\n-----------------   Product Menu   -----------------")
        print("\nProduct Code\tProduct Name\t\t\tPrice\n")
        for product in self.products:
            print(f"{product.product_code}\t\t{product.name}\t\t\t{product.price:.2f} Rupees")
    
    def generate_bill(self, order):
        total_cost = 0.0
        print("\nOrder Details:")
        print("Product Code\tProduct Name\tPrice")
        for product_code, quantity in order.items():
            product = next((p for p in self.products if p.product_code == product_code), None)
            if product:
                cost = product.price * quantity
                total_cost += cost
                print(f"{product.product_code}\t\t{product.name}\t\t{product.price:.2f} Rupees x {quantity} = {cost:.2f} Rupees")
        
        print(f"\nTotal Cost: {total_cost:.2f} Rupees")

store = Store()
store.add_product(Product("P001", "Ballpoint Pen", 10))
store.add_product(Product("P002", "Geometry Set", 100))
store.add_product(Product("P003", "Spiral Notebook", 35))
store.add_product(Product("P004", "Water Colors", 300))
store.add_product(Product("P005", "Whitener", 20))

store.display_menu()

order = {}
print("\n")
while True:
    product_code = input("Enter product code (or 'done' to finish order): ").strip().upper()
    if product_code == 'DONE':
        break
    quantity = int(input("Enter quantity: "))
    if product_code in order:
        order[product_code] += quantity
    else:
        order[product_code] = quantity

store.generate_bill(order)

print("\n")