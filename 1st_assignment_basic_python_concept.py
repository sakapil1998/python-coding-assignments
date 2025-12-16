###Task 1:

"""
program to perform basic arithmetic operations

"""
a= int(input("Enter first number(a):"))
b=int(input("Enter second number(b):"))
add = int(a+b)
sub = int(a-b)
multi = int(a*b)
div = float(a/b)
print("addition is",add)
print("subtraction is",sub)
print("multiplication is", multi)
print("division is", div)


"""Expected output:"""

    #Enter first number(a):5
    #Enter second number(b):10
    #addition is 15
    #subtraction is -5
    #multiplication is 50
    #division is 0.5

###Task 2:
"""
program to print a welcome message with first name and last name

"""

first_name = input("Enter first_name:")
last_name = input("Enter last_name:")

print("hello", first_name, last_name+"!","Welcome to the Python programe.")

"""Expected output:"""
     #Enter first_name:john 
     #Enter last_name:doe
     #hello john doe! Welcome to the Python programe.
