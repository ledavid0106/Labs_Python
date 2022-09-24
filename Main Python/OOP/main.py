
# from alarm_clock import *


# David_alarm = AlarmClock()

# David_alarm.current()
# David_alarm.toggle()
# David_alarm.set_time()



from customer import *
from product import *
from shopping_cart import *
david = Customer("David")
# dav = ShoppingCart()
print(david.shopping_cart)
print(david.name)

x = 0
while x < 3:
    david.add_cart()
    x += 1
# print(david.shoppingcart)
print()

david.view_all()

david.ShoppingCart()empty_cart()

