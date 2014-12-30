#name error, foo not defined
def name_error():
	print(foo)

#type error, cannot add to a string
def type_error():
	foo = "bar"
	foo = foo + 5

#attribute error, cannot slice an int
def attr_error():
	bar = 2
	bar.slice(1,3)

#syntax error, open string inside print function
def syntax_error():
	print('test = 'bad syntax")

