import sys
T = int(sys.stdin.readline())
for i in range(T):
    x, op, y = str(sys.stdin.readline())[10:].split(" ")
    x = float(x)
    y = float(y)
    
    if op == '+':
        print(x+y)
    elif op == '-':
        print(x-y)
    elif op == '*':
        print(x*y)
    elif op == '/':
        print(x/y)
        
