#  Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
#  containing over five-thousand first names, begin by sorting it into alphabetical
#  order. Then working out the alphabetical value for each name, multiply this
#  value by its alphabetical position in the list to obtain a name score.
#  
#  For example, when the list is sorted into alphabetical order, COLIN, which is
#  worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
#  obtain a score of 938 x 53 = 49714.
#  
#  What is the total of all the name scores in the file?
#  

def val(string):
	val = 0
	alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for s in string:
		for i, a in enumerate(alpha):
			if s.lower() == a.lower():
				val += i+1
	return val

f = open('names.txt')
lines = f.read()
f.close()

names = lines.split(',')
#print new_names[0]
for i in range(len(names)):
	names[i] = names[i].strip('"')
	#print names[i]

names.sort()

tot_score = 0
for i, name in enumerate(names):
	tot_score += (i+1)*val(name)

assert val('COLIN') == 53, "Value function is off..."

print tot_score
