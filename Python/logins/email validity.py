z=input()
email=z.lower()
if "@gmail.com" in z:
    if email[0].isalpha():
        print('valid email',email)
    else:
        print('invalid it contains int at first')
else:
    print('invalid input')