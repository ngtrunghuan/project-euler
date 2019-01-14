import time
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
  
  factors = factorise(n)


def max_drs(n):
  """
  Calculate the maximum digital root sum among all product combinations for natural number n
  """
  pass

if __name__ == "__main__":
  start = time.clock()

  # factorsOfN = factorise(100)
  # print(factorsOfN)

  

  end = time.clock()

  print('--- Elapsed time: {:2f}s'.format(end - start))