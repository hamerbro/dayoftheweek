import time 

# day value of None => Today
def dayOfWeek(DayNum = None): 
	# match day order to python return values
	days = ['Monday', 'Tuesday',
			'Wednesday', 'Thursday', 
			'Friday', 'Saturday', 'Sunday']

	# check for the default value 
	if DayNum == None: 
		theTime = time.localtime(time.time())
		DayNum = theTime[6] # extract the day value
		return days[DayNum]

print dayOfWeek()
print "Today is %s " % dayOfWeek() 
