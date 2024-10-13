from collections import defaultdict

# Example with defaultdict(list)
default_dict = defaultdict(list)

# Adding values to non-existent keys
default_dict['fruits'].append('apple')
default_dict['fruits'].append('banana')
default_dict['vegetables'].append('carrot')

print(default_dict)



from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['one'] = 1
ordered_dict['three'] = 3
ordered_dict['two'] = 2

# Iterate to see if the order is preserved
for key, value in ordered_dict.items():
    print(f"{key}: {value}")


from collections import ChainMap

# Define two dictionaries
deposit = {"amount": 1000, "interest_rate": 10.2}
car = {"model": "BMW", "mileage": 23008}

# Combine the dictionaries into a ChainMap
chain_map = ChainMap(deposit, car)

# Accessing keys from the ChainMap
print(chain_map['amount'])         # Output: 1000 (from the 'deposit' dictionary)
print(chain_map['interest_rate'])  # Output: 10.2 (from the 'deposit' dictionary)
print(chain_map['model'])          # Output: 'BMW' (from the 'car' dictionary)

# If a key is present in both dictionaries, the first dictionary's value is used
deposit['model'] = 'Tesla'
print(chain_map['model'])          # Output: 'Tesla' (from the 'deposit' dictionary)



from collections import UserDict

class LoggingDict(UserDict):
    # Override __setitem__ to log changes
    def __setitem__(self, key, value):
        print(f"Logging: Setting {key} = {value}")
        super().__setitem__(key, value)  # Call the parent class's method to store the item

# Creating a LoggingDict instance
log_dict = LoggingDict()

# Adding and updating items in the LoggingDict
log_dict['a'] = 1   # Logs the insertion of 'a': 1
log_dict['b'] = 2   # Logs the insertion of 'b': 2
log_dict.update({'c': 3})  # Logs the update of 'c': 3
