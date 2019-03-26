print("Q1.\n")

for x in range(0, 26):
    print("%d\n" %x)

print("Q2.\n")

for x in range(0, 41, 2):
    print("%d\n" %x)

print("Q3.\n")

number = input('Pick a number: ')
for x in range (0,int(number)+1):
    print("%d\n" %x)

print("Q4.\n")

print("What happens when you throw a yellow rock in the red sea: ")
while True:
    ans = input()
    if ans == 'Y':
        break
    else: 
        print("wrong.\n")

