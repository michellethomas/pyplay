def is_prime(factor):
  stop_point = (factor/2) +1
  for n in xrange(2,stop_point):
    if factor%n == 0:
      return False
  return True

def get_primes():
  primes = []
  counter = 0
  for i in xrange(2,1000000):
    if is_prime(i):
      counter += 1
      primes.append(i)
      if counter == 10002:
        return primes

primes = sorted(get_primes())
primes[10000]
