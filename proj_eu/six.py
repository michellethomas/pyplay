

def sum_of_squares(n):
  squares = []
  for i in range(0,n+1):
    squares.append(i*i)
  return sum(squares) 

def square_of_sum(n):
  sums = sum(range(0,n+1))
  return sums*sums


print sum_of_squares(100)
print square_of_sum(100)
print square_of_sum(100) -sum_of_squares(100)
