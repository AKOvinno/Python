word = input("Enter a string: ")
new_word = ""
for ch in range(len(word)-1, -1, -1):
    new_word += word[ch]

if word == new_word:
    print("Palindrome")
else:
    print("Not Palindrome")
