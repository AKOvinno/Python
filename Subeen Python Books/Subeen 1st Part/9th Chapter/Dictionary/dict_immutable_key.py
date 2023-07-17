dt = {"a": "A", "b": "B", "c": "C"}
dt[(1, 2, 3)] = "tuple"
print(dt)

# list can't be used as dictionary key, it will show error
# li = [1, 2, 3]
# dt[li] = "list"


s = {1, 2, 3, 4}
print(s)
print(type(s))
# set can't be used as dictionary key, it will show error
# dt[s] = "set"