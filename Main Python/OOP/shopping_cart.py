
class ShoppingCart:
    def __init__(self):
        self.products = []
        
    def current_total(self):
        count = 0
        for count in self.products:
            count += 1
        print(count)

    def add_new(self, ):
        new = input("What product would you like to add?\n")
        self.products.append(new)
        return new
    
    def empty_cart(self):
        self.products = []
# test = ShoppingCart()
# test.add_new()
# print(test.products)
# app = ShoppingCart()
# print(app.products)
# app.add_new()
# print(app.products)