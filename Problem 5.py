import time

divList=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#divList=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

i=1
z=0
while True:
    if z==1:
        break
    for nr in divList:
        if i%nr==0:
            print(f'Iter {i}, confirming {nr}')
            if nr==divList[-1]:
                z=1
                print('The answer is ' +str(i))
        else:
            break
    i+=1
