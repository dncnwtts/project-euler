#  You are given the following information, but you may prefer to do some research for yourself.
#  
#      1 Jan 1900 was a Monday.
#      Thirty days has September,
#      April, June and November.
#      All the rest have thirty-one,
#      Saving February alone,
#      Which has twenty-eight, rain or shine.
#      And on leap years, twenty-nine.
#      A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#  
#  How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

class Date():
	def __init__(self):
		self.day = 1 # monday == 1
		self.month = 0  # january == 1
		self.date = 1 # first of month
		self.year = 1900
		self.leap = False
	def increment(self):

		self.day += 1
		if self.day % 7 == 0:
			self.day = 0	

		self.date += 1
		if (self.date > 30) & (self.month in [8, 3, 5, 10]):
			self.month += 1
			self.date = 1
		elif (self.date > 31) & (self.month in [0, 2, 4, 6, 7, 9, 11]):
			self.month += 1
			self.date = 1
		elif (self.date > 29) & (self.month == 1) & self.leap:
			self.month += 1
			self.date = 1
		elif (self.date > 28) & (self.month == 1) & (not self.leap):
			self.month += 1
			self.date = 1
		else:
			pass
	

		if self.month == 12:
			self.month = 0
			self.year += 1
			if ((self.year % 4 == 0) & (self.year % 100 != 0)) | (self.year % 400 == 0):
				self.leap = True
			else:
				self.leap = False

		return
		

num_firstsuns = 0
current_date = Date()
while current_date.year < 1901:
	current_date.increment()
while current_date.year < 2001:
	current_date.increment()
	if (current_date.day == 0) & (current_date.date == 1):	
		num_firstsuns += 1
	#print '{0}/{1}/{2}'.format(current_date.month+1, current_date.date, current_date.year)

print num_firstsuns
