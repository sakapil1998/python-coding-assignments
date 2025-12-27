## Task 1 :-
"""
Check if a Number is Even or Odd.

"""
num = int(input("enter the number" ))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

""" expected output """
    # enter the number = 7, then '7 is odd'
    # enter the number = 12, then '12 is even'



## Task 2:-

"""
Sum of Integers from 1 to 50 Using a Loop

"""
last_number = int(input("enter a positive last integer:"))
total_sum = 0
print(f"calculating sum from 1 to {last_number}")
for current_num in range(1, last_number +1):
    total_sum = total_sum + current_num
print(f"The sum of numbers from 1 to {current_num} is: {total_sum}") 

""" expected output """
    # enter a positive last integer: 50
    # The sum of numbers from 1 to {current_num} is: 1275



