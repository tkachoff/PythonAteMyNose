import unittest

from week2 import url_cleaner


class TestUrlCleaner(unittest.TestCase):
  def test_positive_alphabet(self):
    url = "page=2&foo=bar&x=y&utm_source=ss&utm_content=ccc"
    result = url_cleaner.clean_url_alphabet_order(url=url)
    self.assertEqual(result, "foo=bar&page=2&x=y")

  def test_positive_original(self):
    url = "page=2&foo=bar&x=y&utm_source=ss&utm_content=ccc"
    result = url_cleaner.clean_url_origin_order(url=url)
    self.assertEqual(result, "page=2&foo=bar&x=y")


if __name__ == "__main__":
  unittest.main()
