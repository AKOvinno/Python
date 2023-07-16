fruits = ["Mango", "Banana", "Orange", "Apple", "Coconut"]
fruits.remove("Orange")
print(fruits)

# fruits.remove("Pineapple") we can use loop and condition to get rid of error

item = "Apple"
if item in fruits:
    fruits.remove(item)
else:
    print(item, "not in list")

print(fruits)
