import json
import pickle
import pathlib

file_path = pathlib.Path("./json/twitter_users.txt").resolve()
file_path.parent.mkdir(parents=True, exist_ok=True)
twitter_users = "[\
    {'name': 'Omosetan Omorele', 'is_married': True, 'age': 45},\
    {'name': 'John Doe', 'is_married': False, 'age': 15}\
]"
with file_path.open(mode="wb") as file:
    pickle.dump(twitter_users, file)

# print(type(twitter))
# print(twitter)
#
#
# print(file_path)

x = json.dumps(twitter_users)

print(x)
print(type(x))
y = json.loads(x)

print(y)
print(type(y))

pickled_obj = pickle.dumps(twitter_users)
print(pickled_obj)
