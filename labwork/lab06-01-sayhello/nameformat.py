# This is where you will code your three functions 
# Be sure to write documentation for this module. Refer to your book chapter for instructions on how to do this.
"""
The NameFormat Module
Has three functions for formatting names:
1. sayHello(firstName) : returns a greeting using the first name.
2. fullName(firstName, lastName) : returns the full name in First Last format.
3. lastNameFirst(firstName, lastName) : returns the name in Last, First format.
"""

# sayHello() Hello Tony!
def sayHello(firstName):
    """
    Return a greeting using the first name.
    Example: Hello Tony!
    """
    return f"Hello {firstName}!"

# fullName() ex: Tony Stark
def fullName(firstName, lastName):
    """
    Return the full name in First Last format.
    Example: Tony Stark
    """
    return f"{firstName} {lastName}"

# lastNameFirst() ex: Stark, Tony
def lastNameFirst(firstName, lastName):
    """
    Return the name in Last, First format.
    Example: Stark, Tony
    """
    return f"{lastName}, {firstName}"










