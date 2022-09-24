from shopping_cart import *

class Customer:
    def __init__(self, value):
        self.shopping_cart = ShoppingCart().products
        self.name = value
    
    def add_cart(self):
        product = ShoppingCart().add_new()
        self.shopping_cart.append(product)

        # new_product = Shopping_Cart.add_new()
        # self.shopping_cart.append(new_product)
    
    def view_all(self):
        for item in self.shopping_cart:
            print(item)
   
