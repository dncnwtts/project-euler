'''
Using the eight british coins, 200p, 100p, 50p, 20p, 10p, 5p, 2p, and 1p, how many different ways are there to make 2
pounds?
'''

# A hint, possible test case is that one possible combination is [0,1,1,2,0,1,1,3]

coins = [200,100,50,20,10,5,2,1]


def add(comb):
	assert len(comb) == 8, "Incorrect length."
	s = 0
	for i in range(len(coins)):
		s += coins[i]*comb[i]
	return s


comb = [0,1,1,2,0,1,1,3]
assert add(comb) == 200, "Adding function is incorrect."

max_inds = [200/coin for coin in coins]
# each of this is the maximum number of each coin needed.

# My first idea is to see how many of the largest coin add up to the first. If
# there is any remainder, then find the next largest denomination that can go
# in, see how many are left, until we find the magic number.

# The next step is tricky. I think the answer is to replace large coins with
# smaller coins.
