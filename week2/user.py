"""
Implement a class User with aributes name, age. The instances of this
class should be sortable by age by default.
So sorted([User(name='Eric', age=34), User(name='Alice', age=22)])
will return a list of sorted users by their age (ASC).
How would you sort those objects by name? Hint for the default sorting:
__cmp__, functools.total_ordering.
"""
import functools


@functools.total_ordering
class User:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __eq__(self, other):
    return self.age == other.age

  def __gt__(self, other):
    return self.age > other.age

  def __repr__(self):
    return 'User(name="{name}", age="{age}")'.format(name=self.name,
                                                     age=self.age)
