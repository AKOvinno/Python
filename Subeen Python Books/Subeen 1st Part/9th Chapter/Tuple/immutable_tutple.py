li = [1, 2, 3]
print(li)
li[0] = 5
print(li)

tpl = (1, 2, 3)
print(tpl)
tpl[0] = 5
# It will throw an error saying 'tuple' object doesn't support item assignment
print(tpl)