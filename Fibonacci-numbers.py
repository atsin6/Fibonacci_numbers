#fibonacci Numbers : 0,1,1,2,3,5,8,13,21,34,55,........
x = 0
y = 1
a = int(input('Enter how many numbers you want :',))
for i in range(a):
    print(x)
    print(y)
    x = x + y
    y = y + x
