# The sum of squares of the first ten natural numbers is 385, square of the sum of the first ten natural numbers is
# 3025. The difference between them is 2640. Find the difference for the first 100 natural numbers.

n = 10
ssq = 0
for i in range(n+1):
	ssq += i**2

sqs = (n*(n+1)/2)**2

answer = sqs - ssq

assert answer == 2640, "Answer is {0}".format(answer)

n = 100
ssq = 0
for i in range(n+1):
	ssq += i**2

sqs = (n*(n+1)/2)**2

answer = sqs - ssq
print answer
