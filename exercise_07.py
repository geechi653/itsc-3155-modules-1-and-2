numbers = []
even_nums = []

while True:
    user_input = input("Enter an integer or type QUIT to exit: ")
    if user_input.upper() == "QUIT":
        break
    num = int(user_input)
    numbers.append(num)
    even_nums.append(num) if num % 2 == 0 else None

print("All numbers: ", numbers)
print("Even numbers: ", even_nums)


# user_input.upper is for uppercase QUIT and break is same as switch case in java. 
# .append command adds numbers to the list.