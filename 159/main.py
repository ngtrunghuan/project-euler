import time
import itertools
from functools import reduce
import operator
from tqdm import tqdm

from HashableList import HashableList
# out = {}

# for i in range (1, 1000000):
#   out[i] = 0

# print('Done: initialising output dictionary')

def factorise(n:int):
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

def calculateDigitalRootSum(n:int, store={}):
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
  if n in store:
    return store[n]
  out = 0
  while n > 0:
    out += n % 10
    n = int(n / 10)
  return out

def getFactorCombinations(n:int):
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

  # Product combinations should be unique
  products_combinations = set()

  for i in range(1, total_factors):
    for combo in itertools.combinations(factors_array, i):
      products = HashableList(combo)
      products.append(int(n / reduce(operator.mul, products)))
      products_combinations.add(products)
      
      products = HashableList([reduce(operator.mul, combo)])
      products.append(int(n / reduce(operator.mul, products)))
      products_combinations.add(products)
      

  products_combinations.add(HashableList([n]))

  return products_combinations

def calculateMaxDrs(n, store={}):
  """
  Calculate the maximum digital root sum among all product combinations for natural number n
  """
  combinations = getFactorCombinations(n)
  drs = [sum([calculateDigitalRootSum(factor, store) for factor in factors]) for factors in combinations]
  return max(drs)

def readStore(filename='store.txt'):
  store = {}
  with open(filename, mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    lines = [line.strip('\n').split(',') for line in lines]
    for l in lines:
      store[int(l[0])] = int(l[1])
  return store 

if __name__ == "__main__":

  speedtests = [100, 1000, 10000, 100000]
  for test in speedtests:
    start = time.perf_counter()
    # print('__main__')

    # print('Reading from store...')
    # max_drs_store = readStore()
    # print('Store loaded [{}]'.format(len(max_drs_store)))  
    
    # sum_drs = 0
    # with open('store.txt', mode='a+', encoding='utf-8') as f:
    #   for i in tqdm(range(1, 100000)):
    #     if i in max_drs_store:
    #       sum_drs += max_drs_store[i]
    #     else:
    #       maxDrs = calculateMaxDrs(i, max_drs_store)
    #       max_drs_store[i] = maxDrs
    #       sum_drs += maxDrs
    #       f.write('{},{}\n'.format(i, maxDrs))
      
    # print(sum_drs)

    ### SPEED TEST ###
    # Factorise
    for i in range(2, test):
      _ = calculateMaxDrs(test)
    ##################
    end = time.perf_counter()
    print('Speedtest for {}: {:2f}s'.format(test, end - start))
    # print('--- Elapsed time: {:2f}s'.format(end - start))