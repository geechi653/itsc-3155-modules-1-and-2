string = input("Enter a string: ")
char_list = list(string)
split_list = [char_list[n:n+3] for n in range(0, len(char_list), 3)]
print(char_list)
print(split_list)








# source used https://stackoverflow.com/questions/4978787/how-do-i-split-a-string-into-a-list-of-characters. 