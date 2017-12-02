from functools import reduce
from itertools import product
from operator import add

def handle_row_part1(row):
  return max(*row) - min(*row)

def handle_row_part2(row):
  # perhaps not the cleanest idea but it works
  for (ia, a), (ib, b) in product(enumerate(row), repeat=2):
    if ia == ib:
      continue
    if a % b == 0:
      return a // b
  assert False

if __name__ == "__main__":
  with open("input2") as f:
    input = f.read()

  puzzle = [[int(x) for x in l.split("\t")] for l in input.split("\n") if l]

  solution1 = reduce(add, (handle_row_part1(r) for r in puzzle), 0)
  solution2 = reduce(add, (handle_row_part2(r) for r in puzzle), 0)
  print(solution1)
  print(solution2)
