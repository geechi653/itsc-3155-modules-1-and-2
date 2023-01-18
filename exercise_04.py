n = int(input("Enter a number: "))
float_list = []

for i in range(n):
    float_list.append(float(input("Enter a float: ")))

print("Float List: ", float_list)
average = sum(float_list) / n
print("Average: ", average)


#I used https://stackoverflow.com/questions/34651733/how-to-append-a-string-to-a-float-list and https://stackoverflow.com/questions/28928397/in-f-what-is-the-difference-between-float-and-float-list