from collections.abc import Iterator, Callable
from pprint import pprint
from typing import TypeVar, TypeAlias, Any

ItemT = TypeVar("ItemT") # define a generic type variable, makes the function more adaptable because it can accept any type for ItemT, while still providing type checking

def group_by_iter(n:int, iterable:Iterator[ItemT]) -> Iterator[tuple[ItemT,...]]: # tuple[ItemT,...] a tuple with any number of elements, all of which must be of ItemT type
    def group(n:int, iterable:Iterator[ItemT]) -> Iterator[ItemT]:
        for i in range(n):
            try:
                yield next(iterable)
            except StopIteration:
                return
    while row:= tuple(group(n,iterable)): # The walrus operator, introduced in Python 3.8, allows you to assign a value to a variable as part of an expression.
        yield row



filtered_numbers = list(filter(lambda x: x%3==0 or x%5==0, range(300)))
print(list(group_by_iter(7,iter(filtered_numbers))))


ItemFilterPredicate:TypeAlias = Callable[[Any], bool]

def group_filter_iter(n:int, predicate:ItemFilterPredicate, items:Iterator[ItemT]) -> Iterator[tuple[ItemT,...]]: 
    def group(n:int, iterable:Iterator[ItemT]) -> Iterator[ItemT]:
        for i in range(n):
            try:
                yield next(iterable)
            except StopIteration:
                return
    subset = filter(predicate,items)
    while row:= tuple(group(n,subset)):
        yield row

rule = ItemFilterPredicate = lambda x: x%3==0 or x%5==0

from collections.abc import Callable, Iterable

class AggregateFiltered:
    __slots__ = ["filter", "function"] # feature in Python that allows to explicitly define a fixed set of attributes (or instance variables) that objects of the class can have

    def __init__(self,filter:Callable[[float], bool],func:Callable[[float], float]) -> None: # stows the two function objects, filter and func, in the object's instance variables.
        self.filter = filter
        self.function = func

    def __call__(self, iterable:Iterable) -> float: # method returns a value based on a generator expression that uses two internal function definitions
        return sum(self.function(x) for x in iterable if self.filter(x))
    
# Define a filter function to select numbers greater than 10
def filter_func(x: float) -> bool:
    return x > 10

# Define a function to square the selected numbers
def square_func(x: float) -> float:
    return x * x

# Create an instance of AggregateFiltered
agg = AggregateFiltered(filter_func, square_func)

# Call the instance with an iterable (e.g., a list of numbers)
result = agg([1, 5, 12, 15, 7, 18])
print(result)  # Output: 12^2 + 15^2 + 18^2 = 144 + 225 + 324 = 693
