class Point: # a hashable object is an object that has a fixed hash value for its lifetime and can be used as a key in dictionaries or stored in sets. 
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __hash__(self):
        return hash((self.x, self.y)) # int - determines where the object is stored in a hash table. try hash(self.y)
    
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
    
# int, float, string, frozenset - hashable
# list, set, dictionary - unhashable
# do you observe some pattern? what about a tuple, is it hashable or? 
point1 = Point(1, 2)
point2 = Point(1, 2)
point3 = Point(2, 3)

# Dictionary usage
points_dict = {point1: 'A'}
print(points_dict[point2])  # Outputs 'A' because point1 and point2 are considered equal

# Set usage
points_set = {point1, point2, point3}
print(len(points_set))  # Outputs 2 because point1 and point2 are equal
