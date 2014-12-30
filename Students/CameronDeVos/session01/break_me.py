# Explore Errors Task

# Create a NameError
# nameerrors value is not referenced before being called

def createNameError():
	return nameerrors

# Create a TypeError
# Cannot add a int and str together because they are different types

def createTypeError():
	a = 5
	b = "foo"
	return a + b

# Create a SyntaxError
# return is spelled incorrectly

def createSyntaxError():
	c = 5555
	reurn c

# Create a AttributeError
# Float object does not have a length attribute

def createAttributeError():
	a = 5.3
	return a.length


# Function Testing

# createNameError()
# createTypeError()
# createSyntaxError()
# createAttributeError()
