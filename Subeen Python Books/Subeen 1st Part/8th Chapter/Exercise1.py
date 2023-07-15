#input = Hello Test! 123 123, good.

text = input("Enter a string: ")

text_upper = ""
text_lower = ""
text_num = ""
text_other = ""

for ch in text:
    if (ch.isupper()):
        text_upper += ch
    elif (ch.islower()):
        text_lower += ch
    elif (ch.isnumeric()):
        text_num += ch
    else:
        text_other += ch

print(text_upper)
print(text_lower)
print(text_num)
print(text_other)