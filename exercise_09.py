words_list = []
for i in range(5):
    word = input("Enter a word: ")
    words_list.append(word)
result_string = " ".join(words_list)
print("Words : ", words_list)
print("One String: ", result_string)