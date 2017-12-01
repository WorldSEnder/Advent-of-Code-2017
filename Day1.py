from itertools import cycle, islice
from functools import reduce

def advance(iterator, n):
  # Next forces the islice to consume from iterator the first n elements
  # Then, we default to None
  next(islice(iterator, n, n), None)
  # convenience
  return iterator

def cmp_and_sum(sum, element):
  a, b = element
  if a == b:
    return sum + int(a)
  return sum

captcha = input()


# Part 1
sum = reduce(cmp_and_sum, zip(captcha, advance(cycle(captcha),                1)), 0)
print(sum)

# Part 2
sum = reduce(cmp_and_sum, zip(captcha, advance(cycle(captcha), len(captcha) // 2)), 0)
print(sum)
