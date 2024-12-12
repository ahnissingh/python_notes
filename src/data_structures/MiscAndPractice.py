my_dict = {
    'name': 'Ahnis',
    'password': 'root',
    'cake': 'large'
}
chai_types = {
    'Masala': 'Spicy',
    'Ginger': 'Zesty',
    'Green': 'Mild'
}
# 1 )
# ZIP OPERATOR
key_values_pairs = zip(my_dict.keys(), my_dict.values())
for key, value in key_values_pairs:
    print(f"Key {key} Value {value}")
# 2
for key, value in chai_types.items():
    print(f"{key} : {value}")
# 3
for key in chai_types:
    print(key, chai_types[key])

if "Masala" in chai_types:
    print("I have masala chai")
# Pop last
chai_types.popitem()
# Pop specific
chai_types.pop('Ginger')
print(chai_types)

del chai_types['Masala']
# Nested Dictionaries
tea_shop = {
    "chai": {
        "Masala": "Spicy",
        "Ginger": "Zesty",
        "Green": "Fresh",
        "Black": "Strong",
    },
    "Food":
        {
            "Petty": "Delicious",
            "Samosa": "Aaloo",
        }
}
# Dictionary Comprehension
squared_even_numbers = {x: x ** 2 for x in range(0, 11, 2)}
print(squared_even_numbers)

keys = ['Masala', 'Ginger', 'Lemom']
default_value = 'Delicious'
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)
