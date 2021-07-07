import random
num=random.randint (1,20)
x=input('guess a number?')
x=int(x)

while x!=num:
     if x<num:
     print('sorry incorrect!type a bigger number')
      
     elif x>num:
     print('sorry incorrect!type a smaller number')
    
