def HelloWorld():
    print("Hello World")

def getName(): 
    n1 = input("Please Enter Your Name: ")
    print("Hello %s " %n1)

def getName2():
        n1 = input("Please Enter Your Name: ")
        if n1 == 'Alice' or n1 == 'Bob':
            print("Hello %s "%n1)


def pr_n():
    n = input("Enter a number: ")
    x=0
    for z in range (1,int(n)+1):
      x=x+z
    print(x)

pr_n()