#Task 2
instructor = ["Nevin", "Mike", "Jake", "Dan", "Megan"]
instructor.append("Dan")
instructor.append("James")
instructor.append("John-Boy")
print(instructor)

#Task 3
instructor.pop()
print(instructor)

#Task 4
instructor.remove("Mike")
print(instructor)

list3 = ["David", "Dan", "Danimal"]
first_name = ""
dup = False
x = 0
y = 0
while dup != True:
    if list3[x] == instructor[y]:
        list3.remove(list3[x])
        nickname = input("Sorry that name has been taken, please provide a nickname")
        instructor.append(nickname)  
    else:
        x += 1 
    if x == len(list3):
        while dup != True:
            x = 0
            if list3[x] == instructor[y]:
                list3.remove(list3[x])
                nickname = input("Sorry that name has been taken, please provide a nickname")
                instructor.append(nickname)
            else:
                y += 1    
            while x < len(list3):     
                    instructor.append(list3[x])
                    x += 1
                    dup = True
    if dup == True:
        print(instructor)
        print(len(instructor)) 

list3 = ["David", "Dan", "Danimal"]
first_name = ""
dup = False
# while dup == True:
#     x = 0
#     y = 0
#     for x in range(len(list3)): 
#         while list3[x] == instructor[y]:    
#             list3.remove(list3[x])
#             nickname = input("Sorry that name has been taken, please provide a nickname")
#             instructor.append(nickname)
#             x += 1 
#         if list3[x] == instructor[y]:
#             list3.remove(list3[x])
#             for y in range(len(list)):
#                 y += 1
#         else:
#             instructor.append(list3)
#             print(instructor)
#             print(len(instructor))
#             break 
#     break        
x = 0
y = 0  
while dup == False:
    if list3[x] == instructor[y]:
        list3.remove(list3[x])
        nickname = input("Sorry that name has been taken, please provide a nickname")
        instructor.append(nickname)
    else:
        x += 1
    if x == len(list3):
        break    
x = 0
while dup == False:
    if list3[x] == instructor[y]:
        list3.remove(list3[x])
        nickname = input("Sorry that name has been taken, please provide a nickname")
        instructor.append(nickname)
    else:
        y += 1    
    if y == len(instructor):       
        break  
x = 0
while x < len(list3):
    instructor.append(list3[x])
    x += 1

print(instructor)
print(len(instructor)) 