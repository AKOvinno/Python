def list_average(num):
    list_len = len(num)
    list_sum = sum(num)
    return list_sum/list_len

num = [1, 2, 3, 4, 5, 6, 7, 8]
avg = list_average(num)
print("Average: ", avg)