a= input('Enter 1st number: ')
b= input('Enter 2nd number: ')
try:
    print('result: ',int(a) + int(b))
except ValueError:
    print('Enter a number not string')
    try:
        c= 13
        d= 'Dear'
        print ('result: ',(c+d))
    except TypeError:
        print('Different type of variable')
finally:
    print('Thats cool')
