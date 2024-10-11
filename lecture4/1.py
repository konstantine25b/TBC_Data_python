import json
def decode(data, default={}):
    try:
        return json.loads(data)
    except:
        return default

thrilled = decode(data="Get started!")
thrilled["comment"] = "I love Python!"
print(thrilled)

frustrated = decode(data="Quit!")
frustrated["comment"] = "I'm done. I'll try something different."
print(frustrated)


fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits, start=1): # index customization
    print(index, fruit)