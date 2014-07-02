# How many lattice paths are there for a 20x20 grid?

# The answer for an nxn grid should be 2n choose n.

def fact(n):
	if n == 1:
		return n
	else:
		return n*fact(n-1)

def num_paths(n):
	return fact(2*n)/fact(n)**2

answer = fact(3)
assert answer == 6, "Whoops"

answer = num_paths(2)
assert answer == 6, "Answer was {0}".format(answer)

answer = num_paths(3)
assert answer == 20, "Answer was {0}".format(answer)

answer = num_paths(4)
assert answer == 70, "Answer was {0}".format(answer)

answer = num_paths(20)
print answer
