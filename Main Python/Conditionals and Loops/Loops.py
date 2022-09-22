#Task 1 ForLoop
for hello in range(5):
    print("Hello")

#Task 2 Counting
count = 0
for count in range(11):
    print(count);
    count += 1;

for count in range(0,11):
    print(count)

#Task 3 counting backwards

for count in range(10,-1,-1):
    print(count);

#Task 4 Prompted Output

desire_count = int(input("How many times would you like to iterate devCodeCamp? "));
for count in range(desire_count):
    print("devCodeCamp");

#Task 5 Packers Split up
for character in "Packers":
    print(character);

#Task 6 
for count in range(0,101):
    if count == 0:
        print("0");
    elif ((count % 3) == 0) and ((count % 5) == 0):
        print("fizzbuzz")
    elif (count % 3) == 0:
        print("fizz");
    elif (count % 5) == 0:
        print("buzz")
    else: 
        print(count);


