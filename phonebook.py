import sys
import string
cases = int(sys.stdin.readline().rstrip())
def phonecases(num,case):
    
    if case == "PARENTHESES":
        print(f"({''.join(number[0:3])}) {''.join(number[3:6])}-{''.join(number[6:])}")
        
    elif case == "DASHES":
        print(f"{''.join(number[0:3])}-{''.join(number[3:6])}-{''.join(number[6:])}")
        
    elif case == "PERIODS":
        print(f"{''.join(number[0:3])}.{''.join(number[3:6])}.{''.join(number[6:])}")
    else:
        print(f"{''.join(number[0:3])} {''.join(number[3:6])} {''.join(number[6:])}")
        
for num_cases in range(cases):
    line = sys.stdin.readline().rstrip()
    number, case = (val for val in line.split(" "))
    number = list(number)
    phonecases(number,case)
