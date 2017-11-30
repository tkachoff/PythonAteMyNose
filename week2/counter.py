"""
Elements counting.
It refers to the sections 1.12 and 1.4-1.5 of the Python Cookbook.
Implement the Counter class. It should only support operations like
__iter__, __getitem__ and .most_common(n). Try to make it as efficient
as possible in terms of performance. Think of an underlying data structure
that should be used and also a base class.
"""
import heapq


class Counter:
  def __init__(self, iterable):
    self.mapping = dict()
    for item in iterable:
      self.mapping[item] = self.mapping.get(item, 0) + 1

  def most_common(self, n):
    return heapq.nlargest(n, self.items(), key=lambda x: x[1])

  def __iter__(self):
    return iter(self.mapping)

  def __getitem__(self, item):
    return self.mapping[item]

  def items(self):
    return self.mapping.items()
