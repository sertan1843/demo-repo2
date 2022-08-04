password = input("Enter a password(must be at least 8 characters long!):")
upcount = 0
numcount = 0
i = 0
if len(password) < 8:
    print("The length is wrong!")
    print("END!")
elif not password.isalnum():
    print("Contains special character")
while i < len(password):
    if password[i]
    if password[i].isdecimal():
        numcount += 1
    elif password[i].isupper():
        upcount += 1
    i += 1
if numcount == 0 or upcount ==0:
    print("Password does not meet the requirements!")
        
    
    
