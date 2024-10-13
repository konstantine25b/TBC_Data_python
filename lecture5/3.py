from typing import List
from collections.abc import Iterator, Callable, Sequence

from typing import TypeVar 

MapD = TypeVar("MapD")
MapR = TypeVar("MapR")

def mapr(func:Callable[[MapD],MapR], collection:Sequence[MapD]) -> list[MapR]: # let's debug together
    if len(collection) == 0: return []
    return mapr(func=func, collection=collection[:-1]) + [func(collection[-1])]
# Example function to be applied
def square(x: int) -> int:
    return x * x

# Client function to test mapr
def client():
    numbers: List[int] = [1, 2, 3, 4, 5]
    result = mapr(square, numbers)
    print("Original numbers:", numbers)
    print("Squared numbers:", result)

client()
