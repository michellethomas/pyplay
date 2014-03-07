import sys

def find_factors(factors, num):
  for n in range(1,30):
    if num%n == 0:
      factors.append(n)
      factors.append(num/n)

def is_prime(factor):
  stop_point = factor/2
  print 'is %s prime?' %factor
  for n in xrange(2,stop_point):
    if factor%n == 0:
      print 'not prime'
      return False
  print 'prime'
  return True

def second_pass(num):
  is_not_divisible = True
  i = 2
  print 'finding factors for %s' %num
  while is_not_divisible:
    if num%i == 0:
      is_not_divisible = False
      print 'factors found for %s: %s, %s' %(num, i, num/i)
      return [i, num/i]
    i+=1
#  for factor in factors:
#    if isinstance(factor,list):
#      for item in factor:
#        print 'item %s' %item
#        for n in range(2,30):
#          if item%n == 0:
#            factor.append(n)
#            factor.append(item/n)

def main():
  prime_factors = []
  num = int(sys.argv[1])
  factors = [num]
  something_not_prime = True

  while something_not_prime:
    new_factors = []
    for num in factors:
      new_factors.extend(second_pass(num))

    factors = new_factors

    prime_factors.extend([num for num in factors if is_prime(num)])
    factors = [num for num in factors if not is_prime(num)]
    print 'prime factors        %s' %prime_factors
    print 'still to factor      %s' %factors
    if not factors:
      something_not_prime = False
#    for i in range(len(factors)):
#      something_not_prime = False
#      if not is_prime(factors[i]):
#        num = factors[i]
#        del factors[i]
#        something_not_prime = True

  print factors

if __name__== "__main__":
  main()
