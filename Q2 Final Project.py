# Q2 Project 
import re
def solve_linear_equation ( equ ):
  
    match = re.match(r"(\d+)x\+(\d+)=(\d+)", equ)
    m, b, y = match.groups()
    m, b, y = float(m), float(b), float(y) # Convert from strings to numbers
    x = (y-b)/m
    print ("x = %f" % x)