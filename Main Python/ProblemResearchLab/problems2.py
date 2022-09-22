#Task1 
#first determine what are the inputs and outputs
#input is a string
#output is the string in reverse
#recognize slice [::-1] as it will start at the end of the string and end at position 0,
    #repeatedly step from right to left by 1 character 
def reverse(str):
    return str[::-1]

#Task2
#first determine what are the inputs and outputs
#input is a string
#output is capitalize the first letter of each word
#recognize different methods of capitalizing such as slice, title, capitalize, etc
#recognize that title will capitalize EACH word
def cap(str):
    return str.title()

#Task3
##first determine what are the inputs and outputs
#input is a string
#output is to determine if the input is the same when in reverse
#recognize the usage of reverse and if
def palindrome(str):
    if reverse(str) == str:
        print(f"{str} is a palindrome!")
    else:
        print(f"{str} is not a palindrome")
palindrome("madam")

#Task4
#first determine what are the inputs and outputs
#input is a string
#output is the compression of the string
# := operator is an operator that assigns values to variables as part of a bigger expression
# in other words it can be used to assign variables while another expression is being evaluated
# we want to recognize if each char is the same, and if they are the same then increase the count of that char but only if they are sequential, then move on to the next char

def compress(st):
   res = ""
   count = 1
   for i in range(1, len(st)):
      if st[i - 1] == st[i]:
         count += 1
      else:
         res = res + st[i - 1]
         if count > 1:
            res += str(count)
         count = 1
   res = res + st[-1]
   if count > 1:
      res += str(count)
   return res

st = "aaabbbbbccccaacccbbbaaabbbaaa" 
print(compress(st))