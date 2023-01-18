original_list = []
for i in range(10):
    original_list.append(int(input("Enter an integer: ")))
    
new_list = []
for i in original_list:
    if original_list.count(i) == 1:
        new_list.append(i)
        
print("Original List: ", original_list)
print("Nums that appear once: ", new_list)