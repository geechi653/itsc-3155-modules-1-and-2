list1 = []
list2 = []
common = []

for i in range(5):
    list1.append(int(input("Enter an integer for list 1: ")))

for i in range(5):
    list2.append(int(input("Enter an integer for list 2: ")))

for i in list1:
    if i in list2 and i not in common:
        common.append(i)

print("List 1: ", list1)
print("List 2: ", list2)
print("Common: ", common)


#Sources I used are https://www.geeksforgeeks.org/python-print-common-elements-two-lists/ and https://www.programiz.com/python-programming/methods/list/append