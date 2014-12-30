
# This Python file contains four functions that cause these errors when called:
# NameError, TypeError, SyntaxError, AttributeError

def GenerateNameError():
    ThisShouldCauseANameError

def GenerateTypeError():
    a = "One"
    b = 2
    print(a + b)

def GenerateSyntaxError():
    This is a bad symbol = 1


#This function causes an AttributeError when it is defined, not when it is called.
def GenerateAttributeError():
    i = 4
    j = i.length()

GenerateNameError()
GenerateTypeError()
GenerateSyntaxError()
GenerateAttributeError()





