def factorial(n):
  factorial_prod = 1
  for i in range(1,n):
    factorial_prod = factorial_prod * i
  return factorial_prod

def factorial_rec(n, total):
  print 'fac(%d, %d)' % (n, total)
  total = total * n
  n = n-1
  if n > 0:
    return factorial_rec(n,total)
  else:
    return total

  print 'exiting, returning None'

def fac(n):
  if n <= 1:
    return 1
  return n * fac(n - 1)

print 'fac is:', fac(4)

for i in range(10000):
  try:
    fac(i)
  except RuntimeError:
    print i
    break
#factorial = str(factorial(100))
factorial_rec = factorial_rec(5,1)
print factorial_rec

factorial_sum = 0
#for item in factorial:
#  factorial_sum += int(item)

#print factorial_sum
