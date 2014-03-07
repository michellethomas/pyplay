
def divis(n):
  is_divis = False
  num = 1
  check_list = [11,13,14,16,17,18,19,20] #Shorter check list instead of range(1,21), for example any num divis 2 is also divis 20
  while is_divis == False:
    divis_nums = 0
    for i in check_list:
      if num%i == 0:
        divis_nums = divis_nums +1
    if divis_nums == n:
      is_divis == True
      return num
    else:
      num = num +1
    if num > 100000000000:
      return num


print divis(20)
