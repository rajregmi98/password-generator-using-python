import random
print('---------------------Password Generator-------------')
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()-.,'
num = input('Enter number of password')
num = int(num)

length = input('Enter password Length')
length = int (length)

print('\n Here are your passwords :')

for pwd in range (num):
    password =''
    for c in range(length):
        password += random.choice(chars)
    print(password)