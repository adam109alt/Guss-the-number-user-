import random 
# make the variables

def computer_gusse(x):# I will make the high is x
    low = 1
    high = x
    feedback = '' # and this is meaning the feedback i will give it to the computer
    gusse = 0
    
    while feedback != gusse:
        gusse = random.randint(low , high)
        feedback = input(f'Is {gusse} Too high (h) or too low (l) or correct (c)?? ')
        
        if feedback == 'h':
            high = gusse - 1
        
        elif feedback == 'l':
            low = gusse + 1
            
        else:
            print(f'Yay The computer gussed right the number was {gusse}')
            break
    
computer_gusse(10) 
