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

#Task 6
list3 = ['David', 'Dan', 'Danimal', "Nevin"]
list4 = []
first_name = ""
def dups(names):
    dup = False
    more = False
    x = 0
    y = 0
    while dup != True:
        if names[x] in instructor:
            # list3.remove(list3[x])
            list4.append(names[x])
            nickname = input(f"Sorry {names[x]} has been taken, please provide a nickname ")
            instructor.append(nickname)
            x += 1
        else:
            x += 1
        if x == (len(names)):
            while dup != True:
                if list4[y] in instructor:
                    instructor.remove(list4[y])
                    if list4[y] in instructor:
                        instructor.remove(list4[y])
                        list4.remove(list4[y])                    
                if list4[y] in names:
                    instructor.remove(list4[y])
                    list4.remove(list4[y])
                if list4 == []:
                    x = 0
                    while x < len(names):
                        instructor.append(names[x])
                        x += 1
                    dup = True
    while more == False:
        first_name = input("Did you want to add any other names? ")
        if first_name == "No":
            return instructor
        else:
            instructor.append(first_name)
    return instructor
print(dups(list3))    
     