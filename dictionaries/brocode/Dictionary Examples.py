# Dictionary = a collection of {key:value} pairs
#               ordered and changeable. No duplicates

# ':' <- is called "Colon"

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))  # Use this to see all attributes and methods inside a dictionary
# print(help(capitals))  # If in case of doubts, you can use this function to see how de methods should be called.


# Get the value of the key passed as argument
print(capitals.get("USA"))  # -> Washington D.C.
# If we pass as argument a key that's not inside our dictionary, "none" will be the return.
print(capitals.get("Japan"))  # -> None

# A way to verify if a key exists on your dictionary.
if capitals.get("Japan"):  # -> That capital doesn't exist
    print("That capitals exists.")
else:
    print("That capital doesn't exist")

print()

# the update() method let you add a new entry to your dictionary.
capitals.update({"Germany": "Berlin"})

# You can also update an old value to a new one using the update method.
capitals.update({"USA": "Detroit"})
print(
    capitals)  # -> {'USA': 'Detroit', 'India': 'New Delhi', 'China': 'Beijing', 'Russia': 'Moscow', 'Germany': 'Berlin'}

# That`s is a way we can remove items of the dictionary, just using the pop() function.
capitals.pop("China")
print(capitals)  # -> {'USA': 'Detroit', 'India': 'New Delhi', 'Russia': 'Moscow', 'Germany': 'Berlin'}

# If you want to delete the last insertion on the dictionary, you can just use the popitem() method. It receives no arguments.
capitals.popitem()
print(capitals)  # -> {'USA': 'Detroit', 'India': 'New Delhi', 'Russia': 'Moscow'}

# To clear a dictionary, use clear() method.
# capitals.clear() # Commenting this dude, so we can continue our examples
print(capitals)  # -> {}

# If you want to work with the keys, you can reserve them into a variable and call the method keys()

print()

keys = capitals.keys()  # That's kinda above my level, it's just an example, there is a other easier way to access the keys of a dictionary
print(keys)  # -> dict_keys(['USA', 'India', 'Russia'])

print()

# Here's another way (easier) to get access to all keys in our dictionary
for key in capitals.keys():
    print(key)
    # USA
    # India
    # Russia

print()

# We can also work with values, instead of keys:
values = capitals.values()  # Will return an object with the values, witch resembles a list.
print(values)  # -> dict_values(['Detroit', 'New Delhi', 'Moscow'])

print()

for value in capitals.values():
    print(value)
    # Detroit
    # New Delhi
    # Moscow

print()

# Turns our dictionary in a couple of tuples, e.g: items = [(),(),()]
items = capitals.items()
print(items) # -> dict_items([('USA', 'Detroit'), ('India', 'New Delhi'), ('Russia', 'Moscow')])

print()

for key, value in capitals.items():
    print(f"{key}:{value}") # Using the template string to work with index and orders smartly.

    # USA: Detroit
    # India: New Delhi
    # Russia: Moscow

print()