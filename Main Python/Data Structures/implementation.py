#Task1 Dictionary, Set, and Tuple
#1 tuple
from cmath import pi
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
def pi_day(months):
    if months.index("March"):
        print("March has National Pi Day!")
pi_day(months)

#2 set
fruits_and_vegi = {"Apples", "Oranges", "Blueberry", "Cabbage", "Lettuce"}
fruits_and_vegi.update(["Peaches", "Cuties", "Gai Lan", "Gourd"])
for var in fruits_and_vegi:
    print(var)

#3 dictionary
users = { 
        "first_name": "David",
        "last_name": "Le",
        "email_address": "ledavid@gmail.com",
        "phone_number": "(123)-456-7890"
        }  
print(f"The users information: \nFirst name: {users['first_name']} \nLast name: {users['last_name']} \nEmail address: {users['email_address']} \nPhone number: {users['phone_number']} ") 
