# this program tells us about the function list and how the variable points to the list rather than holding the values.
x=["Hi","My name is","Adeel Masood"]
# x is a variable that is pointing to the first element in the list
y=x
# both y and x are pointing to the same element

y[2] = "John Mesh"

print("x: ",x," \ny: ",y)

z=list(y)
# z doesn't point to the location where y was pointing but rather a whole new set of list is created

z[2] = "Pyaare Laal"


print("x: ",x,"\ny: ",y,"\nz: ",z)
