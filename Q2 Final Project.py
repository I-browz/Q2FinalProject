# Q2 Project 
import re #regualr expersion operations
import math

def solve_lq ( equ ):
  
    match = re.match("(\d+)x\+(\d+)=(\d+)", equ) #\d range of numbbers between 0 and 9 for the coefficent, constant and number problem consits of
    m, b, y = match.groups()
    m, b, y = float(m), float(b), float(y) # Convert from strings to numbers
    x = (y-b)/m
    print ("x = %f" % x) #%f acts as a format specifier, holds the variable.



a,b,c = input("Enter the coefficients of a, b and c separated by commas: ")

d = b**2-4*a*c # discriminant

if d < 0:
    print "This equation has no real solution"
elif d == 0:
    x = (-b+math.sqrt(b**2-4*a*c))/ (2*a)
    print "This equation has one solutions: ", x
else:
    x1 = (-b+math.sqrt(d))/ (2*a)
    x2 = (-b-math.sqrt(d))/ (2*a)
    print "This equation has two solutions: ", x1, " and", x2

''' 
    
m,b,y = input("Enter the coefficients of m, b and y separated by commas: ")
match = re.match("(\d+)x\+(\d+)=(\d+)")
m, b, y = float(m), float(b), float(y)
if y == y:
    x = (y-b)/m
    print "This equation has one solutions: ", x
'''