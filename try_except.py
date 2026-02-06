try:
    x=int(input('input the integer'))
    print(x)
except:
    print("not integer")


try:
    x=int(input('input the integer'))
    print(x)
except ValueError:
    print('value not integer')
finally:
    print('finished try and except')


