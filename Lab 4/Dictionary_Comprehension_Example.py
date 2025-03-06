# Create a dictionary where keys are numbers and values are their squares
numbers = [1, 2, 3, 4, 5]
squares = {num: num**2 for num in numbers}

print(squares)

print("="*50)

# ========================================================================== #

# Create a dictionary by pairing elements from two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
dictionary = {k: v for k, v in zip(keys, values)}

print(dictionary)

print("="*50)

# ========================================================================== #

# Transform keys to uppercase and values to their squares
original_dict = {"a": 1, "b": 2, "c": 3}
transformed_dict = {k.upper(): v**2 for k, v in original_dict.items()}

print(transformed_dict)