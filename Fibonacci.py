import sys

cases = int(sys.stdin.readline().rstrip())

def fib(num):
    num1 , num2 = 0 , 1
    if num <= 0:
        pass
    elif num ==1:
        return num1
    else:
        for i in range(num-1):
            newnum = num1 + num2
            num1 = num2
            num2 = newnum
        else:
            return num1
        

for num_cases in range(cases):
    num = int(sys.stdin.readline().rstrip())
    print(num,"=" ,fib(num))
