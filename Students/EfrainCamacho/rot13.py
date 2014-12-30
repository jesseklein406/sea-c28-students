import string

def ROT13(test_string):
    """Return a encrypted string offset by 13


    Encrytion does not impact spaces or special characters"""


    shifted_cypherlower = string.ascii_lowercase[13:] + string.ascii_lowercase[:13]
    shifted_cyperupper = string.ascii_uppercase[13:] + string.ascii_uppercase[:13]
    transtable_lower = string.maketrans(string.ascii_lowercase, shifted_cypherlower)
    #print transtable_lower 
    transtable_upper = string.maketrans(string.ascii_uppercase, shifted_cyperupper)
    #print transtable_upper

    
    encrypted_text = []

    for letter in test_string:
        if letter.islower():
            encrypted_text.append(letter.translate(transtable_lower))
        else:
            encrypted_text.append(letter.translate(transtable_upper))
        final_encryption =  "".join(encrypted_text)

    return final_encryption




if __name__ == '__main__':
    assert ROT13("Test Upper and Lower Case")
    print ROT13("Test Upper and Lower Case")
    assert ROT13("Test having werid   spaves   ")
    print ROT13("Test having werid   spaves   ")
    assert ROT13("Test! keeping punctation - ? ,")
    print ROT13("Test! keeping punctation - ? ,")

    print "All Tests Pass"
