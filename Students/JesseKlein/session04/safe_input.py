"""Use this module to access the 'safe_input' function.
"""

def safe_input(prompt):
    """Use raw_input() while catching exceptions for EOFError and
    KeyboardInterrupt.
    """
    print(prompt),
    
    try:
        user_input = raw_input()
    except (EOFError, KeyboardInterrupt):
        user_input = None
    
    return user_input

