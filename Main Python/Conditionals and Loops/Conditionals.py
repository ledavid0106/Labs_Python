#Task 1 driving age
legal_driving_age = 16;
your_age = input("What is your age? ");
if (int(your_age) >= legal_driving_age):
    print("You are legally able to drive.")
else: print("You are not old enough to drive yet.");    

#Task 2 Random Number

import random;
random_number = random.randint(0,10);
if random_number < 3:
    print("0 or 1 or 2");
elif random_number < 6:
    print("3 or 4 or 5");
elif random_number < 9:
    print("6 or 7 or 8");
else: 
    print("9 or 10");

#Task 3 NFL Team

fav_team = input("What is your favorite NFL Team? Examples: Bears, Vikings, Lions, Packers ");
if fav_team == "Bears":
    print("Quarterback much?");
elif fav_team == "Vikings":
    print("Loud noises!");
elif fav_team == "Lions":
    print("LOL! They bad!");
elif fav_team == "Packers":
    print("Best team in the world! Actually, the universe!")
else:
    print("Pick a different team")

