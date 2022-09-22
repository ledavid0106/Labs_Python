import random
favorite_number = 6
ran = random.randint(0,10)
# distance = ran - favorite_number
# print(ran)
# print(f"{distance} numbers away from my favorite number") 
temp = False
x = 0
while temp == False:
    if ran != favorite_number:
        x += 1 
        ran = random.randint(0,10)
    if ran == favorite_number:
        print(f"The computer took {x} amount of tries to guess my favorite number! ")
        temp = True
