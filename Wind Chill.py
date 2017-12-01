import sys
#not valid if t is larger than 50 in absolute value
# or if v is larger than 120 or less than 3
t = float(input('What is the temperature?'))
v = float(input('What is the wind spped?'))
if -50 < t < 50 and 3 < v < 120:
	w = (35.74 + 0.6215*t+(0.4275*t-35.75)*v**0.16)
	print(w)
else:
	print('Error! Temperature must be between -50 and 50 degrees and wind speed must be between 3 and 120.')

