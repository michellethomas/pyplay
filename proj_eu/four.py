'''
Future changes: also could use itertools.product
'''


def find_two_three_digit():
  palindromes = []
  for i in xrange(999, 100, -1):
    for x in xrange(999, 100, -1):
      palindrome = is_palindrome(i*x)
      if palindrome == True:
        palindromes.append(i*x)
  return palindromes
   

def is_palindrome(n):
  num = list(str(n))
  first_half = num[:len(num)/2]
  second_half = num[len(num)/2:]
  if first_half == second_half[::-1]:
    return True
  else:
    return False


p = find_two_three_digit()
print max(p)
