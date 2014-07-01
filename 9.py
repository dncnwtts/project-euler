# There exists exactly one pythagorean triplet (a < b < c, a^2+b^2=c^2) for which a+b+c=1000. Find a*b*c.

a = 0
b = 0
c = 0
def trip_sum(n):
	for c in range(1,n):
		for b in range(1, c):
			for a in range(1,b):
				if (a**2+b**2 == c**2) and (a + b+ c == n):
					return a*b*c

print trip_sum(1000)
