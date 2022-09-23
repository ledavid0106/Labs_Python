from shopping_cart import *

class Customer:
    def __init__(self, value):
        self.shoppingcart = []
        self.name = value
    
    def add_cart(self):
        product = ShoppingCart().add_new()
        self.shoppingcart.append(product)

        # new_product = ShoppingCart.add_new()
        # self.shoppingcart.append(new_product)
    
    def view_all(self):
        for item in self.shoppingcart:
            print(item)
   
