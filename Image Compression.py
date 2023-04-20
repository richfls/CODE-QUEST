import sys
import math
cases = int(sys.stdin.readline().rstrip())

def compress(num):
    mmax = max(num)
    mmin = min(num)
    for i in num:
        output = ((i-mmin)/(mmax-mmin))*255
        print(round(output))
for num_cases in range(cases):
    amount = int(sys.stdin.readline().rstrip())
    listnum = []
    for i in range(amount):
        number = float(sys.stdin.readline().rstrip())
        listnum.append(number)
    compress(listnum)
