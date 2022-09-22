# # #Task 1
# input = ["Javascript", "Python", "Java", "Django", "React"]
# print(input[1])

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

#Task 5
list1 = ["fan", "bull-", "high-", "barrel-o-", "slap"]
list2 = ["dango", "rider", "horse", "monkeys", "stick"]
x = 0
while x < len(list1):
    print(list1[x] + list2[x])
    x += 1

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
     

#task 7
list1 = ["Japan", "Korea"]
list2 = ["Taiwan", "China", "Vietnam"]
print(list1 + list2)
list1 = ["Japan", "Korea"]
list2 = ["Taiwan", "China", "Vietnam"]
for x in list2:
    list1.append(x)
print(list1)
list1 = ["Japan", "Korea"]
list2 = ["Taiwan", "China", "Vietnam"]
list1.extend(list2)
print(list1)

#task8
list1 = ["Toyota", "Honda", "Tesla"]
list2 = list1.copy()
print(list2)

list1 = ["Toyota", "Honda", "Tesla"]
list2 = []
for x in list1:
    list2.append(x)
print(list2)

list1 = ["Toyota", "Honda", "Tesla"]
list2 = list(list1)
print(list2)

#Task 9
list1 = ["apple", "banana", "peach", "pears", "blueberry"]
list1.sort()
print(list1)
list1.sort(reverse = True)
print(list1)

list1 = ["apple", "banana", "peach", "pears", "blueberry"]
def without(list1):
    for i in range(len(list1)-1):
        for j in range(i+1,len(list1)):
            if list1[i]>list1[j]:
                temp = list1[i]
                list1[i] = list1[j]
                list1[j] = temp
    print(list1)
without(list1)