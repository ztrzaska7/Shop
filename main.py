class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def remove_item(self, product):
        self.items = [(p, q) for p, q in self.items if p != product]

    def calculate_total(self):
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        return total

class Order:
    def __init__(self, shopping_cart, payment_method):
        self.shopping_cart = shopping_cart
        self.payment_method = payment_method

    def process_order(self):
        total = self.shopping_cart.calculate_total()
        self.payment_method.pay(total)
        print("Order processed successfully!")

class PaymentMethod:
    def __init__(self, name):
        self.name = name

    def pay(self, amount):
        print(f"Payment of {amount} processed using {self.name}.")


product1 = Product("Product 1", 10.99)
product2 = Product("Product 2", 19.99)


cart = ShoppingCart()
cart.add_item(product1, 2)
cart.add_item(product2, 1)


payment_method = PaymentMethod("Credit Card")


order = Order(cart, payment_method)
order.process_order()
