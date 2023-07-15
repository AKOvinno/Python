word = input("Enter a string: ")
new_word = ""
for ch in range(1, len(word), 2):
    new_word += word[ch]
    new_word += word[ch-1]

print(new_word)