#Task1 Dictionary, Set, and Tuple
#1 tuple
def pi():
    months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    print(months[2])


# the task wants you to index the tuple (just like a list) and print the indexed value ("March")

#2 set
fruits_and_vegi = {"Apples", "Oranges", "Blueberry", "Cabbage", "Lettuce"}
fruits_and_vegi.update(["Peaches", "Cuties", "Gai Lan", "Gourd"])
def fruit():
    for var in fruits_and_vegi:
        print(var)

#3 dictionary
users = { 
        "first_name": "David",
        "last_name": "Le",
        "email_address": "ledavid@gmail.com",
        "phone_number": "(123)-456-7890"
        }  
def use():
    print(f"The users information: \nFirst name: {users['first_name']} \nLast name: {users['last_name']} \nEmail address: {users['email_address']} \nPhone number: {users['phone_number']} ") 


list = [
    { 
        "first_name": "Cam",
        "last_name": "Tran",
        "relation": "Cousin"
    },
    { 
        "first_name": "Nguyen",
        "last_name": "Nguyen",
        "relation": "Cousin"
    },
    { 
        "first_name": "Hau",
        "last_name": "Le",
        "relation": "Cousin"
    },      
]

def relations(lists):
    for key in lists:
        print(key.get("first_name"), key.get("relation"))

