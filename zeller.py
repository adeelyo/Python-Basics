print("Enter the birth date ")
A = int(input("Enter the month "))
Year = int(input("Enter the year "))
if(A == 11 or A == 12):
	Year = Year -1
C = Year % 100
D = int(Year / 100)
E = C/100
B = int(input("Enter the day "))
W = (13*A - 1) / 5
X = C / 4
Y = D / 4
Z = int(W + X + Y + B + C - (2*D))
R = (Z % 7)
R = R + 2
if R == 1:
	print("The day is MONDAY")
elif R == 2:
	print("The day is TUESDAY")
elif R == 3:
	print("The day is WEDNESDAY")
elif R == 4:
	print("The day is THURSDAY")
elif R == 5:
	print("The day is FRIDAY")
elif R == 6:
	print("The day is SATURDAY")
elif R == 0:
	print("The day is SUNDAY")
