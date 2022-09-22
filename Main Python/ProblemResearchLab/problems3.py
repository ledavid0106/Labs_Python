#Task1
#first determine what are the inputs and outputs
#input is a positive integer
#output is a happy or sad number
#usage of power and sums
#create an empty variable for numbers to be added into
#create a while loop so that it can run as many times as it needs to
#take the square and sum of each digit and then add it into the empty variable
#if the result of the square and sum is equal to a number in the variable set then it is an infinite loop which also means its a sad number
#if the result eventually hits 1, then it has a happy number

def Happy(n):
  past = set()
  while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return ("Your number is not a happy number :( ")
        past.add(n)
  return ("Your number is a happy number!")
print(Happy(19))


#Task2
#first determine what are the inputs and outputs
#input is 1-100
#output is a number that is divisible by 1 and itself
# for count in range(1,101):
#     if (count % 1 == 0) and (count % count == 0):
#         print(count)
#scratch idea and try to determine if there are any other numbers that it can be divisible by
#bc original idea doesnt account for another numbers (like 4 has 2x2)
#new idea uses for loop with range to see if the number is also divible by other numbers besides 1 and itself
for num in range(1,101):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

#Task3
#first determine what are the inputs and outputs
#input is an int
#output is a series of number that follows fibonacci rule
#the first number in the list should be the given number
#afterwards, the second number in the list should be that same number that was initially given
#once we have established 2 numbers in the set, we can run a while loop that takes the first position in the list and adds the second number in the list
#the resulting number is then added to the end of the list
#then the last number will be added to the number in the position right before it, the resulting added at the end etc
#repeated for 10 times cause we need a stop at some point otherwise it will go forever
def fib():
    num = input("What number would you like to start at? ")
    num = int(num)
    y = 0
    fib = [num]
    if num == 1:
        fib.append(1)
    if num != 1:
        fib.append(num)
    while y < 10:
        num = fib[y] + fib[y+1]
        fib.append(num)
        y += 1
    return fib
print(fib())
