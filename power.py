base = int(input("Enter the base "))
exp = int(input("Enter the power "))
base1 = base
for a in range(1,exp):
	base = base1 * base
print("The result base raised to the given power ",base)