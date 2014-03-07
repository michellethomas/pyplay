import math

def find_triangles(n):
  return (n*(n+1))/2
#  if n <=1:
#    return 1
#  return n + find_triangles(n-1)

def find_factor_length(n):
  factors = 0
  for num in range(1,int(math.sqrt(n)+1)):
    if n%num == 0:
      factors += 2
  return factors

max_factors = 0
for i in xrange(1,100000):
  triangle = find_triangles(i)
  factor_length = find_factor_length(triangle)
  if factor_length > 500:
    print '%s %s' %(triangle, factor_length)

