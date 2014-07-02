# Count out the number of words in the numberes 1 to 1000.

ones = ['zero','one','two','three', 'four', 'five', 'six', 'seven', 'eight',
'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
'ninety']

def num_letters(n):
	num = 0
	for i in range(1, n+1):
		if i < 10:
			num += len(ones[i])


assert num_letters(5) == 19, "Only {0} words".format(num_letters(5))
