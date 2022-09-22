#Task1 
#first determine what are the inputs and outputs
#input is a string
#output is the string in reverse
#recognize slice [::-1] as it will start at the end of the string and end at position 0,
    #repeatedly step from right to left by 1 character 
def reverse(str):
    return str[::-1]
print(reverse("hello"))

def rev(str):
    temp = ""
    for char in str:
        temp = char + temp
    return temp
print(rev("hello"))