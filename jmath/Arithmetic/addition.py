'''
Information:
            Use this function to add number no matter how many.

Syntax:
        add([...])

Example:
        add([1, 2, 3, 4, 5])
        add([142, 32532, 523, 25325])

Note:
    - You need to add this inside the print statement so as to get the result printed in the terminal.
'''

def add(numberlist):
    result = 0
    for number in numberlist:
        result += number
    return result

"""
Made by:
        Bhavyadeep31
"""