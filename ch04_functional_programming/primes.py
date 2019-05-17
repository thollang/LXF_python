def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n
def _not_divisible(n):
    return lambda x: x & n > 0
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n 
        it = filter(_not_divisible(n), it)


if __name__ == "__main__":
    it = primes()
    for i in range(10):
        print(next(it))
