import random 

def play():
    user=input("shoot rock(r) or paper(p) or scissor(s)")
    comp=random.choice(['r','p','s'])
    if user==comp:
        return 'its a tieeeeee'
    if win(user,comp):
        return 'you wonnnnn'
    if win(comp,user):
        return 'you lostttt'
    

def win(user, comp):
    if(user=='r' and comp=='s') or (user=='s' and comp=='p') or (user=='p' and comp=='r'):
        return True
