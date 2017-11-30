DEFAULT_PREFIX = 'utm_'
DEFAULT_SPLITTER = '&'


def _filter_args(url, prefix=DEFAULT_PREFIX, splitter=DEFAULT_SPLITTER):
  return [x for x in url.split(splitter) if not x.startswith(prefix)]


def clean_url_alphabet_order(url, prefix=DEFAULT_PREFIX,
                             splitter=DEFAULT_SPLITTER):
  """
  Write a function that will parse a url query string like
  "page=2&foo=bar&x=y&utm_source=ss&utm_content=ccc" and return a query
  string where all the params are sorted by their names
  like this "foo=bar&page=2&x=y" and all the "utm_" parameters are removed.
  """
  return splitter.join(sorted(_filter_args(url, prefix, splitter)))


def clean_url_origin_order(url, prefix=DEFAULT_PREFIX,
                           splitter=DEFAULT_SPLITTER):
  """
  Write a function that will parse a url query string like
  "page=2&foo=bar&x=y&utm_source=ss&utm_content=ccc" and return a query
  string where all the params retain their original order
  "page=2&foo=bar&x=y" and all the "utm_" parameters are removed.
  """
  return splitter.join(_filter_args(url, prefix, splitter))
