
def check_triplet(trip):
  if trip['a'] + trip['b'] + trip['c'] == 1000:
    print 'a:%s b:%s c:%s' %(trip['a'], trip['b'], trip['c'])


def formula(m,n):
  a = m**2-n**2
  b = 2*m*n
  c = m**2+n**2
#  print 'a %s  b %s  c %s' %(a,b,c)
  trip = {'a':a, 'b':b, 'c':c}
  check_triplet(trip)


for n in range(0,1000):
  for m in range(1,1000):
    if m > n:
      formula(m, n)



