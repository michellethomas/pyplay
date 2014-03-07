import math

end_num = 2000000+1

def find_all_multiples(num):
  stop_num = int(math.ceil(end_num/float(num)))
  multiple_list = []
  for n in xrange(num,stop_num):
    multiple_list.append(num*n)
  return multiple_list


primes = []
multiples = set()

for num in xrange(2,end_num):
  if num not in multiples:
    primes.append(num)
    multiples.update(find_all_multiples(num))

print primes
print multiples

prime_sum = 0
for thing in primes:
  prime_sum += thing

print prime_sum
