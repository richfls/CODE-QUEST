import sys

case =  int(sys.stdin.readline().rstrip()) 
def fact(num):
    if num> 1:
        return num*fact(num-1)
    else:
        return num
for num_cases in range(case):
    n = int(sys.stdin.readline().rstrip())
    print(fact(n))
