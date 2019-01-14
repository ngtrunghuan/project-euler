import collections

class HashableList(list):
  def __hash__(self):
    counter = collections.Counter(self)
    d = dict(counter)
    # arr = [(key, d[key] for key in sorted]
    keystring = ';'.join(['{}:{}'.format(key, d[key]) for key in sorted(d.keys())])
    return hash(keystring)

if __name__ == "__main__":
  a = HashableList([2, 2, 2, 5, 5, 5])
  b = HashableList([5, 5, 2, 2, 2, 5])
  print(a.__hash__())
  print(b.__hash__())
  print(a.__hash__() == b.__hash__())
