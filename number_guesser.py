import random
def guess(x):
    rand_num=random.randint(1,x)
    guess=0
    while guess!=rand_num:
        guess=int(input(f"guess a number bw 1 and {x}:"))
        if guess<rand_num:
            print("guessed no is too low!")
        elif guess>rand_num:
            print("guessed no is too high!")    
        else:
            print("yayyyy you guessed it correct!!!") 
guess(10)               

def comp_guess(x):
    low=1
    high=x
    feedback=""
    while feedback !="c":
        if low!=high:
         guess=random.randint(low,high)
        else:
         guess=low 
        feedback=input(f"enter if {guess} is too high(h), too low(l), or correct(c)")        
        if feedback == "h":
          high = guess - 1
        elif feedback == "l":
         low = guess + 1
        elif feedback == "c":
         print(f"Yay! I guessed your number, {guess}, correctly!")
        else:
         print("Invalid input. Please enter 'H', 'L', or 'C'.")
    print(f"yayyy comp guessed {guess} rightttt!!!!!")     
comp_guess(33)       
