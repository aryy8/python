import random 

def play():
    user=input("shoot rock(r) or paper(p) or scissor(s):")
    comp=random.choice(['r','p','s'])
    print(f"comp chose {comp}")
    if user==comp:
        return 'its a tieeeeee'
    if is_win(user,comp):
        return 'you wonnnnn'
    return 'you lostttt'
    

def is_win(user, comp):
    if(user=='r' and comp=='s') or (user=='s' and comp=='p') or (user=='p' and comp=='r'):
        return True
    
print(play())    

