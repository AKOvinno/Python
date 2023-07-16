li = [1, 2, 3, 4]
new_li = []

for x in li:
    new_li.append(2 * x)

print(new_li)

# Using list comprehensions
new_list = [2 * x for x in li]
print(new_list)

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_li = [x for x in range(1, 11) if x % 2 == 0]
print(even_li)