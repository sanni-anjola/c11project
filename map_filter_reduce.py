from functools import reduce
import operator
list_of_numbers = [1, 2, 3, 4, 5]

mapped_list = list(map(lambda x: x**2, list_of_numbers))

print(mapped_list)
print(mapped_list)

list_of_dict = [{"name": "Asake", "gender": "F"}, {"name": "Boyo", "gender": "M"}]

mapped_list_of_dict = list(
    map(lambda x: ("Mr. " if x["gender"] == "M" else "Mrs. ") + x["name"], list_of_dict)
)
print(mapped_list_of_dict)
print([("Mr. " if x["gender"] == "M" else "Mrs. ") + x["name"] for x in list_of_dict])


filtered_list_of_dict = list(
    filter(lambda x: x["gender"] == "M", list_of_dict)
)

print(filtered_list_of_dict)
print([name for name in list_of_dict if name['gender'] == 'M'])

sum_reduce = reduce(lambda acc, val: acc + val, list_of_numbers)
sum_reduce2 = reduce(operator.mul, list_of_numbers)

print(sum_reduce)
print(sum_reduce2)

fruits = ["pear", "cucumber", "water me", "banana"]

print(reduce(lambda x, y: x if len(x) >= len(y) else y, fruits, ""))