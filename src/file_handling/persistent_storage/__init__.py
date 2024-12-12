import pickle

# Example Python object to pickle
data = {
    'name': 'Alice',
    'age': 28,
    'city': 'Wonderland',
    'friends': ['Bob', 'Charlie', 'David']
}
with open('data.pickle', 'wb') as file:
    pickle.dump(data, file)

with  open('data.pickle', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
