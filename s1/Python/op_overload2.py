class Time:
	def __init__(self,hour,minute,second):
		self._hour = hour
		self._minute = minute
		self._second = second
	
	def __add__(self,other):
		total_seconds = self._hour * 3600 + self._minute * 60 + self._second + other._hour * 3600 + other._minute * 60 + other._second
		
		new_hour = total_seconds // 3600
		total_seconds %= 3600
		new_minute = total_seconds // 60
		new_second = total_seconds % 60
	
		return Time(new_hour,new_minute, new_second)
	
	def display_time(self):
		print(f"{self._hour:02d}:{self._minute:02d}:{self._second:02d}")
		
		
time1 = Time(3,45,30)
time2 = Time(1,30,15)

sum_time = time1 + time2

print("Time 1:")
time1.display_time()

print("\nTime 2:")
time2.display_time()

print("\nSum of Time 1 and Time 2:")
sum_time.display_time()

'''
output:

Time 1:
03:45:30

Time 2:
01:30:15

Sum of Time 1 and Time 2:
05:15:45

'''
