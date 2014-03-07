
num = 2
power = 1000

power_digit = '%s' %num**power
digit_sum = 0

for thing in power_digit:
  digit_sum += int(thing)

print digit_sum
