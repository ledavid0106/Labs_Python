#Task 1 While Loop Task
count = 0;
while count < 5:
    print("hello!");
    count += 1;

#Task 2 Validation
password = "danimal";
validate = False;
while validate == False:
    validated = input("What is the password?");
    if validated == password:
        print("User Validated")
        break;

password = "danimal";
validate = False;
while validate is False:
    if input("What is the password?") == password:
        print("User Validated")
        validate = True;
#alternative
password = "danimal";
while True:
    validate = input("What is the password?")
    if validate == password:
        break;
print("User Validated");