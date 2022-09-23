
class ShoppingCart:
    def __init__(self):
        self.products = []
        
    def current_total(self):
        count = 0
        for x in self.products:
            count += 1
        return count

    def add_new(self):
        new = input("What product would you like to add?\n")
        return new
        # self.products.append(new)
    
    def empty_cart(self):
        self.products = []
# app = ShoppingCart()
# print(app.products)
# app.add_new()
# print(app.products)