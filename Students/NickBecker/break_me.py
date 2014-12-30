# Four Codes that break Python

# Name Error
def fun1(things):
	print things
fun1(games)
#games is an undefined function

# Syntax Error
def fun2(thing1):
	thing1 $ 2
fun2("Nick")
# "$" isn't an operator

# Type Error
def fun3(this):
	for i in 42:
		print i
fun3(4)
# Not able to loop through an int as a string

# Attribute Error
def fun4(thing):
	42 == None.lower()
fun4(42)
# None has no attribute to lower
