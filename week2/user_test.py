import random
import string
import unittest

from week2 import user


def name_generator():
  return random.choice(string.ascii_uppercase) + ''.join(
      random.choice(string.ascii_lowercase) for _ in
      range(random.randint(5, 10)))


list_users = []
for i in range(20):
  list_users.append(
    user.User(name=name_generator(), age=random.randint(15, 60)))


class TestUser(unittest.TestCase):
  def test_positive_sorted(self):
    sorted_list = sorted(list_users)
    list_users.sort(key=lambda x: x.age)
    self.assertEquals(sorted_list, list_users)


if __name__ == "__main__":
  unittest.main()
