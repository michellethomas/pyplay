
def multiples():
  nums = []
  for i in range(0,1000):
    if i%3==0 or i%5==0:
      nums.append(i)
  return nums

def main():
 mult = multiples()
 sum_multiples = sum(mult) 
 print sum_multiples

if __name__ == '__main__':
  main()
