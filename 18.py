##  By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
##  
##  3
##  7 4
##  2 4 6
##  8 5 9 3
##  
##  That is, 3 + 7 + 4 + 9 = 23.
##  
##  Find the maximum total from top to bottom of the triangle below:
##  
##  75
##  95 64
##  17 47 82
##  18 35 87 10
##  20 04 82 47 65
##  19 01 23 75 03 34
##  88 02 77 73 07 63 67
##  99 65 04 28 06 16 70 92
##  41 41 26 56 83 40 80 70 33
##  41 48 72 33 47 32 37 16 94 29
##  53 71 44 65 25 43 91 52 97 51 14
##  70 11 33 28 77 73 17 78 39 68 17 57
##  91 71 52 38 17 14 91 43 58 50 27 29 48
##  63 66 04 68 89 53 67 30 73 16 69 87 40 31
##  04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
##  
##  NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
##  
import time

test = [
[3],
[7,4],
[2,4,6],
[8,5,9,3]]

# The brute force way of looking at this is there are 2**n possible ways to go;
# you can either move to the right, or keep the same value. We can just make
# these 2**n arrays of True/False values, and then use them to create the sums.

# I'm also considering a recursive solution, where if we have k Trues to assign,
# we can loop over the n potential slots, then call the same function again for
# k-1 Trues to assign over n-1 potential slots (with the assigned slot removed).
	
def _return_all_paths(n, depth=1, verbose=False):
	all_paths = [[True]*n ] + [[False]*n]
	#all_paths = []
	for k in range(1,n)[::-1]:
		if k == 1:
			paths = []
			for i in range(n):
				path = [False]*n
				path[i] = True
				paths.append(path)
			return paths
		else:
			for i in range(k):
				#print n,k
				#print 'Entering level {0}'.format(depth+1)
				sub_paths = return_all_paths(n-1,depth=depth+1, verbose=verbose)
				for j in range(len(sub_paths)):
					sub_paths[j].insert(i, True)
				all_paths += sub_paths
			if verbose:
				if len(all_paths) > 57922:
					print len(all_paths)	
					#time.sleep(1)
					#print all_paths
			return all_paths

def return_all_paths(n, depth=1,verbose=False):
	all_paths = []
	if n == 1:
		paths = [[True],[False]]
		return paths
	else:
		true_paths = return_all_paths(n-1,depth=depth+1,verbose=verbose)
		for path in true_paths:
			path.append(True)
			all_paths.append(path)

		false_paths = return_all_paths(n-1,depth=depth+1,verbose=verbose)
		for path in false_paths:
			path.append(False)
			all_paths.append(path)
		return all_paths

# To insert into an existing list at a position, use (for example)
##  >>> x = [1,2,3,4,5]
##  >>> x.insert(2,'insertion')
##  >>> print(x)
##  [1, 2, 'insertion', 3, 4, 5]


def max_sum(grid, verbose=False):
	bool_array = return_all_paths(len(grid)-1, verbose=verbose)
	if verbose:
		print 'Finished boolean array'
		#print bool_array
		print 'Output boolean array length was {0}'.format(len(bool_array))
	
	path_indices = []
	for i in range(len(bool_array)):
		path_indices.append([(0,0)])
		n = 0
		for j in range(len(bool_array[i])):
			if bool_array[i][j]:
				n += 1
			path_indices[i].append( (n,j+1))
	if verbose: print 'Created path indices'

	max_sum = 0
	for path in path_indices:
		s = 0
		for i in range(len(grid)):
			s += grid[path[i][1]][path[i][0]]
		if s > max_sum:
			max_sum = s
	
	return max_sum

test_answer = max_sum(test, verbose=False)
assert test_answer == 23, "I got {0} instead".format(test_answer)

grid = [
[75],
[95,64],
[17,47,82],
[18,35,87,10],
[20,4,82,47,65],
[19,1,23,75,3,34],
[88,2,77,73,7,63,67],
[99,65,4,28,6,16,70,92],
[41,41,26,56,83,40,80,70,33],
[41,48,72,33,47,32,37,16,94,29],
[53,71,44,65,25,43,91,52,97,51,14],
[70,11,33,28,77,73,17,78,39,68,17,57],
[91,71,52,38,17,14,91,43,58,50,27,29,48],
[63,66,4,68,89,53,67,30,73,16,69,87,40,31],
[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]

t0 = time.time()
answer = max_sum(grid, verbose=True)
t = time.time()
print answer, "Took me {0} seconds".format(t-t0)
