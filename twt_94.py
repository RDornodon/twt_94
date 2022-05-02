import itertools as T
def sieve(limit):
    a = [1] * limit;
    a[0] = a[1] = 0
    for (i, is_prime) in enumerate(a):
        if is_prime:
            yield i
            for n in range(i * i, limit, i):
                a[n] = 0

S=[*sieve(9999)]
for I in[I:=input]*int(I()):print(next(filter(lambda v:all(map(v.__mod__,filter((v**.5).__ge__,S))),[*sorted(int(''.join(_))for _ in T.permutations(I()))][::-1])))