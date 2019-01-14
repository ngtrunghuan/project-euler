import time
import itertools
from functools import reduce
import operator

from HashableList import HashableList
# out = {}

# for i in range (1, 1000000):
#   out[i] = 0

# print('Done: initialising output dictionary')

def factorise(n):
  """
  Factorise a natural number n into prime factors.
  Parameters
  ----------
  n : int
    Natural number n
  
  Returns
  -------
  dict
    Dictionary containing prime factors as keys and their powers as values.
  
  Raises
  ------
  ValueError
    Expected input of type "int"
  """
  if not isinstance(n, int):
    raise ValueError('Expected type {} but got {} instead.'.format(int, type(n)))
  
  out = {}
  factor = 2
  while factor <= n:
    if n % factor == 0:
      if factor not in out:
        out[factor] = 1
      else:
        out[factor] += 1
      n = int(n / factor)
    else:
      factor += 1
  return out

def drs(n):
  """
  Calculate the digital root sum of a natural number n
  Parameters
  ----------
  n : int
    Natural number n
  
  Returns
  -------
  int
    Digital root sum of input n
  
  Raises
  ------
  ValueError
    Expected input of type "int"
  """
  if not isinstance(n, int):
    raise ValueError('Expected type {} but got {} instead.'.format(int, type(n)))
  
  out = 0
  while n > 0:
    out += n % 10
    n = int(n / 10)
  return out

def factor_combinations(n):
  """
  Return all unique product combinations for natural number n
  Parameters
  ----------
  n : int
    Natural number n
  
  Returns
  -------
  set<[int]>

  Raises
  ------
  ValueError
    Expected input of type "int"
  """
  if not isinstance(n, int):
    raise ValueError('Expected type {} but got {} instead.'.format(int, type(n)))
  if n == 0:
    return set()
    
  factors = factorise(n)
  total_factors = sum(factors.values())
  factors_array = list(itertools.chain.from_iterable([[key] * factors[key] for key in factors.keys()]))

  # factors_array.append(1)
  # print(factors_array)

  # Product combinations should be unique
  products_combinations = set()

  for i in range(1, total_factors):
    for combo in itertools.combinations(factors_array, i):
      products = HashableList(combo)
      products.append(int(n / reduce(operator.mul, products)))
      products_combinations.add(products)
  products_combinations.add(HashableList([1, n]))

  return products_combinations

def max_drs(n):
  """
  Calculate the maximum digital root sum among all product combinations for natural number n
  """
  pass

if __name__ == "__main__":
  start = time.perf_counter()

  test = 1
  factorsOfN = factorise(test)
  print(factorsOfN)
  print(factor_combinations(test))

  

  end = time.perf_counter()

  print('--- Elapsed time: {:2f}s'.format(end - start))