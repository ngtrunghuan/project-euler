import math
from tqdm import tqdm
from datetime import datetime
from multiprocessing import Pool, freeze_support
from functools import partial

def gcd(a, b):
    while b != 0:
        t = a
        a = b
        b = t % b
    return a

def gcd_multi(n):
    out = []
    start = datetime.now()
    for a in range(2, n-1):
        max = math.floor(n*n - a*a)
        for b in range(a, max):
            if gcd(a, b) == 1:
                out.append((a, b))
        del max
    end = datetime.now()
    print('time elapsed: {}'.format((end - start).total_seconds()))
    return out
def pythagorean_triplet(n):
    start = datetime.now()
    print('pythagorean_triplet({})'.format(n))
    
    out = []
    for a in range(2, n-1):
        for b in range(a, n):
            if gcd(a, b) == 1:
                c = math.sqrt(a*a + b*b)
                if c == int(c) and c < n:
                    out.append((a, b, c))

    print('found: {} triplets'.format(len(out)))
    
    end = datetime.now()
    print('time elapsed: {}'.format((end - start).total_seconds()))
    return out

def pythagorean_triplet_singleprocess(a, n):
    start = datetime.now()
    print('pythagorean_triplet({})'.format(n))
    
    out = []
    for b in range(a, n):
        if gcd(a, b) == 1:
            c = math.sqrt(a*a + b*b)
            if c == int(c) and c < n:
                out.append((a, b, c))

    print('found: {} triplets'.format(len(out)))
    
    end = datetime.now()
    print('time elapsed: {}'.format((end - start).total_seconds()))
    return out

def pythagorean_triplet_multiprocess(n):
    function = partial(pythagorean_triplet, n=n)
    params = range(2, n-1)
    p = Pool(10)
    out = []
    for result in tqdm(p.map(function, params), total=len(params)):
        out.append(result)
        del result
    return out

def solve(n):
    print('solve project euler 540 for {}'.format(n))
    triplets = pythagorean_triplet_multiprocess(n)
    # out = []
    # for a, b, c in tqdm(triplets):
    #     if gcd(a, b) == 1:
    #         out.append((a, b, c))
    return len(triplets)

if __name__ == "__main__":
    freeze_support()
    n = 3141592653589793
    # c = 0
    # while n > 1:
    #     n = n / 2
    #     c = c + 1
    # print(c)
    # print(gcd(4, 9))
    # pythagorean_triplet(1000)
    print(solve(3141592653589793))
    # print(math.sqrt(n))
    # gcd_multi(1000)