# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.
# 
def isp(n):
	# n = sum(digs*10**n)
	exp = len(str(n))
	digs = []
	for i in range(exp)[::-1]:
		rem = n % 10**i
		digs.append( (n - rem)/10**i)
		n = n - digs[-1]*10**i
	for j in range(len(digs)/2):
		if digs[j] != digs[-1-j]:
			return False
	return True

def lp(ndigs):
	lp = []
	for i in range(10**(ndigs-1),10**ndigs):
		for j in range(10**(ndigs-1),10**ndigs):
			lp_test = i*j
			if isp(lp_test):
				lp.append(lp_test)
	return max(lp)

answer = lp(2)

assert isp(151), "Palindrome test function failed."
assert answer == 9009, "Incorrect test, got {0}".format(answer)

answer = lp(3)
print answer
