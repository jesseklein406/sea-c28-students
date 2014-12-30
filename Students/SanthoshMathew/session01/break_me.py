# let's try and break Py!

#func-1 : NameError - Raised when a local or global name is not found. 
# This applies only to unqualified names. The associated value is 
# an error message that includes the name that could not be found.

def printthis (str1):
	print str1
	return

printthis ("this will work") # this code works: Py knows the Name and will print the str passed 
printthat ("this won't") # will break with NameError: name printthat is not defined 


# func-2 Raised when an operation or function is applied to an object of inappropriate type. 
# The associated value is a string giving details about the type mismatch.

a=1.0
b=str('what type am i')
#print a,b

def TypeGoof (a,b): 
	c = a + b # However -> str (a) + b will work 
	print c 
	return 

TypeGoof (a,b) 

# func-3: Syntax error
def printthis (str1)  # this missing ":" -> is a Py SyntaxError 
	print str1
	return


