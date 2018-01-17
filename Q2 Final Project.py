# Q2 Project 
def fcn(x):
    return 3*x + 5
    
def solver(guess):
    # fcn(x) = 0
    while fcn(guess) !=0:
        fguess = fcn(guess)
        print guess
        if fguess > 0:
            guess = guess/2.0
        elif fguess < 0:
            guess = guess * 2.0
            var = raw_input("")