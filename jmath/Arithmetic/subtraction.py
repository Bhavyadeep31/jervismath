'''
Information:
            Use this function to subract as many number as you want from a number.

Syntax:
        subtract([...])

Example:
        subtract([1, 2, 3, 4, 5])
        sybract([142, 32532, 523, 25325])

Note:
    - You need to add this inside the print statement so as to get the result printed in the terminal.
    - The subraction is the first number getting subtracted by the numbers ahead in the queue.
        Eg:
            If we are doing -> subtract([420, 69, 96])
                Here, 420 is getting subtracted once by 69 and once by 96.
                The expression is more like:
                                            420 - (69 + 96)
'''
def subtract(numberlist: list):
    result = numberlist[0]
    for number in numberlist[1:]:
        result -= number
    return result

"""
Made By:
        Bhavyadeep31
"""