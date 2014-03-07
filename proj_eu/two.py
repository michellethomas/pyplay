def fibs():
  old = 1
  new = 2
  even_fibs = [2]
  while new < 4000000:
    old, new = new, old + new
    if new % 2 == 0:
      even_fibs.append(new)
  return even_fibs



even_fibs = fibs()
sum_even_fibs = sum(even_fibs)
print sum_even_fibs
