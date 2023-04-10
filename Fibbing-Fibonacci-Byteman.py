import sys

cases = int(sys.stdin.readline().rstrip())

def fib(num):
    num1 , num2 = 0 , 1
    if num < 0:
        return False
    elif num == 0:
        return True
    elif num ==1:
        return True
    else:
        for i in range(num+10):
            newnum = num1 + num2
            num1 = num2
            num2 = newnum
            if num == num2:
                return True
                break
        

for num_cases in range(cases):
    num = int(sys.stdin.readline().rstrip())
    if fib(num) == True:
        print("TRUE")
    else:
        print("FALSE")
