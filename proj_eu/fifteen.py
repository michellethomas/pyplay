def count_paths(l, r):
	if l == 0 or r == 0:
		return 1
	else:
		count = 0
		return count + count_paths(l, r-1) + count_paths(l-1, r)








'''

	if l != 2 and r != 2:
		print '(%d, %d)' %(l,r)
		print count_paths(l,r+1, count)
		print count_paths(l+1,r, count)
	else:
		print '(%d, %d)' %(l,r)
		return count +1
'''

#l = [[i,j] for i in range(3) for j in range(3)]

'''
for item in l:
  if item[1]==20:
    print item
  else:
    print item,
'''

print count_paths(6,6)
#recursion
