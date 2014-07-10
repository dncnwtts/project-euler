# The 12th term in hte Fibonnaci sequence is the first to contain three digits. What is the first term to contain 1000
# digits?

def num_digs(n):
	return len(str(n))

F = [1,1]

i = 1
while i < 1000:
	F.append(F[-1] + F[-2])
	i = num_digs(F[-1])

print 'Answer is {0}'.format(len(F))
