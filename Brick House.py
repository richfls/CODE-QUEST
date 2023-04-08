import sys


cases = int(sys.stdin.readline().rstrip()) #reads lines and strips spaces

for caseNum in range(cases):#runs a for loop for test cases
        line = sys.stdin.readline().rstrip()
        data = line.split(" ")#creates spaces
        for i in range (len(data)):
            data[i] = int(data[i])
       
       
        #while n3 is bigger than 0, keep subtracting 5 n2 number of times and stay above 0
        #then check if what's left over is less than or EQUAL n2
        one = data[0]
        five = data[1]*5
        numsum = data[2]
        while(five > numsum):
            five -= 5
            if five <= numsum:
                break
        if one + five >= numsum:
            print("true")
        else:
            print("false")
