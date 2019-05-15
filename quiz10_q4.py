def PrintBoxByWidth(wd):
    #print out 4 lines of width wd

#line 1
    for x in range(0,wd):
        print("x", end='')
    
#line 2
    print()
    for x in range(0,wd):
        if(x==0):
            print("x", end='')
        elif(x==wd-1):
            print("x", end='')
        else:   
            print(" ",end='')

#line 3
    print()
    for x in range(0,wd):
        if(x==0):
            print("x", end='')
        elif(x==wd-1):
            print("x", end='')
        else:   
            print("o",end='')
#line 4
    print()
    for x in range(0,wd):
        if(x==0):
            print("x", end='')
        elif(x==wd-1):
            print("x", end='')
        else:   
            print(" ",end='')
#line 5
    print()
    for x in range(0,wd):
        print("x", end='')


def PrintBoxByWidth2(ch,n):
    if(ch=='x'):
        for x in range(0,n):
            print('x', end='')
    elif(ch=='o'):
         for x in range(0,n):
            print('o', end='')
    elif(ch==''):
        for x in range(0,n):
            print(' ', end='')
    return

PrintBoxByWidth2('x',50)
print()
PrintBoxByWidth2('o',50)
print()
PrintBoxByWidth2('x',50)
print()
