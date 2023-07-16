li = [1, 2, 3]
li2 = [3, 4, 5, 6]

li.extend(li2)
print(li)

print(li.count(3))
print(li.count(100))

del(li[1])
print(li)
del(li[0])
print(li)

del(li)
print(li) # It will throw error because now there is no list