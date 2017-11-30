import random
import unittest
from collections import Counter
from week2 import counter

words = [
  'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
  'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
  'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
  'my', 'eyes', "you're", 'under'
]


class TestCounter(unittest.TestCase):
  def test_most_common(self):
    origin_counter = Counter(words)
    my_counter = counter.Counter(words)
    self.assertEqual(origin_counter.most_common(3),
                     my_counter.most_common(3))

  def test_get(self):
    origin_counter = Counter(words)
    my_counter = counter.Counter(words)
    item = random.choice(words)
    self.assertEqual(origin_counter[item],
                     my_counter[item])

  def test_iterator(self):
    origin_counter = Counter(words)
    my_counter = counter.Counter(words)
    for f, b in zip(origin_counter, my_counter):
      self.assertEqual(f, b)


if __name__ == "__main__":
  unittest.main()
