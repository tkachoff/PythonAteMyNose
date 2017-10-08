"""
Implement a Quick Sort in Python using lists comprehensions.
This implementation will be inefficient, but very pythonic.
"""


def quick_sort(iterable, reverse=False):
    if len(iterable) == 0:
        return []
    pivot = iterable[0]
    smaller = quick_sort([x for x in iterable[1:] if x < pivot], reverse)
    larger = quick_sort([x for x in iterable[1:] if x >= pivot], reverse)
    if reverse:
        return larger + [pivot] + smaller
    else:
        return smaller + [pivot] + larger


if __name__ == '__main__':
    li = [1, 4, 6, 8, 3, 5, 8, 9, 6, 4, 2]
    print(quick_sort(li))
    print(quick_sort(li, reverse=True))
