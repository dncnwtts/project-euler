#      A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#      
#      1/2	= 	0.5
#      1/3	= 	0.(3)
#      1/4	= 	0.25
#      1/5	= 	0.2
#      1/6	= 	0.1(6)
#      1/7	= 	0.(142857)
#      1/8	= 	0.125
#      1/9	= 	0.(1)
#      1/10	= 	0.1
#      Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#      
#      Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
#      
#      

# This version doesn't work for cycles longer than 12, because that's just the maximum precision of float decimals. We
# need to do a more precise version of this.
def cycle_len(n):
	rep = long_division(n)
	#print rep
	for i in range(len(rep)):
		for j in range(i+1,len(rep)):
			if rep[i] == rep[j]:
				match = True
				k = 1
				while match and (j + k < len(rep)):
					if rep[i+k] == rep[j+k]:
						k += 1
						pass
					else:
						match = False
				if match:
					return j-i
						
	return

# Maybe I need to actually implement long division.
def long_division(n, tol=5551):
	rep = ''
	num = 1
	while len(rep) < tol:
		x = num/n
		if x == 0:
			num *= 10
			rep = rep + '0'
		else:
			rep = rep + str(x)
			num -= n*x
			num *= 10
	val = rep[-1]
	while val == '0':
		if rep[-1] == '0':
			rep = rep[:-1]
		val = rep[-1]
	return rep

assert cycle_len(7) == 6, "Cycle length calculator is not working."
assert cycle_len(6) == 1, "Cycle length calculator is not working."
assert cycle_len(9) == 1, "Testing..."
assert cycle_len(81) == 9, "Longer test..."
assert cycle_len(44) == 2, "Leading non-cycles."

d = 2
max_len = 0
max_len_val = 0
while d < 1000:
	l = cycle_len(d)
	if l > max_len:
		max_len = l
		max_len_val = d
	d += 1

print max_len_val
