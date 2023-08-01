
# Import random
import secrets
import string

def salt(length):
    alphabet = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(length))
    
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
random_letters = ""
    
n = int(input('Please tell me how many EC2 instances you want?: '))
dep = input('Please tell me the department you are in. Marketing, Accounting, or FinOps: ') #if in x apartment deny else continue )

if dep == 'Marketing' or dep == 'Accounting' or dep == 'FinOps':
    for i in range(n):
        print(str(dep)+'-'+str(salt(5)))
else:
    print('You should not be using this name generator')
