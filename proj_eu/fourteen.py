def sequence(n,length):
  if n == 1:
    return (1,length)
  elif n%2 == 0:
    return sequence(n/2,length+1)
  else:
    return sequence(3*n+1,length+1)

highest_sequence = 0
highest_num = 0
for i in range(2,999999):
  result =  sequence(i,1)
  if result[1] > highest_sequence:
    highest_sequence = result[1]
    highest_num = i
    print highest_sequence

print highest_sequence
print highest_num
