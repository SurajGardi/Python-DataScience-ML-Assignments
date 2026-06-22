"""
Q6. Write a program to display:
• Data type
• Memory address
• Size in bytes
  of a variable entered by the user.
"""

import sys

print("Enter the number : ")

No = int(input())

print("Type is : ",type(No))
print("Memory address is",id(No))
print("Size is : ",sys.getsizeof(No))