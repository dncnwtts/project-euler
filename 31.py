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
	if s == 200:
		return True
	else:
		return False


comb = [0,1,1,2,0,1,1,3]
assert add(comb), "Adding function is incorrect."

max_inds = [200/coin for coin in coins]
# each of this is the maximum number of each coin needed.
