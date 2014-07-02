# Count out the number of words in the numberes 1 to 1000.

ones = ['','one','two','three', 'four', 'five', 'six', 'seven', 'eight',
'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
'seventeen', 'eighteen', 'nineteen']
tens = ['', 'ten','twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def numbermap(n):
	word = ''
	digs = str(n)
	if len(digs) == 4:	
		word += ones[int(digs[0])] + 'thousand'
		digs = str(int(digs[1:]))
	if len(digs) == 3:
		if int(digs) % 100 == 0:
			word += ones[int(digs[0])] + 'hundred'
			return word
		else:
			word += ones[int(digs[0])] + 'hundredand'
			digs = str(int(digs[1:]))
	if len(digs) == 2:
		if int(digs) < 20:
			word += ones[int(digs)]
		else:
			word += tens[int(digs[0])] + ones[int(digs[1])]
	if len(digs) == 1:
		word += ones[int(digs)]
	return word

def num_letters(n):
	num = 0
	for i in range(1,n+1):
		num += len(numbermap(i))
	return num

assert num_letters(5) == 19, "Only {0} letters".format(num_letters(5))
assert len(numbermap(342)) == 23, "342 is wrong"
assert len(numbermap(115)) == 20, "115 is wrong"

print num_letters(1000)
