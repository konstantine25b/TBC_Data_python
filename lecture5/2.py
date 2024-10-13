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


from collections import UserDict

class AccessCountDict(UserDict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.access_count = {}

    def __getitem__(self, key):
        # Increment access count for the key
        if key in self.data:
            self.access_count[key] = self.access_count.get(key, 0) + 1
        return super().__getitem__(key)

    def get_access_count(self, key):
        # Return the access count for the key, defaulting to 0
        return self.access_count.get(key, 0)

# Client code
access_dict = AccessCountDict()
access_dict['x'] = 100   # Setting a key-value pair

# Access the key 'x' multiple times
print(access_dict['x'])   # Output: 100 (1st access)
print(access_dict['x'])   # Output: 100 (2nd access)

# Get the access count for 'x'
print(access_dict.get_access_count('x'))  # Output: 2


from collections.abc import MutableMapping

class CustomMap(MutableMapping):
    def __init__(self):
        self.store = {}  # Internal dictionary to store the actual data
    
    def __getitem__(self, key):
        # Always return 10, regardless of the actual value stored
        return 10
    
    def __setitem__(self, key, value):
        # Store the key-value pair in the internal dictionary
        self.store[key] = value
    
    def __delitem__(self, key):
        # Remove the key from the internal dictionary
        del self.store[key]
    
    def __iter__(self):
        # Return an iterator over the dictionary keys
        return iter(self.store)
    
    def __len__(self):
        # Return the number of items in the dictionary
        return len(self.store)

# Client code
custom_map = CustomMap()

# Adding a key-value pair to the CustomMap
custom_map['a'] = 10

# Accessing the key 'a'
print(custom_map['a'])  # Output: 10 (because __getitem__ always returns 10)

