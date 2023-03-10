import sys

cases = int(sys.stdin.readline().rstrip()) 

for num_cases in range(cases):
    datastring = sys.stdin.readline()
    data = datastring.split(" ")

    x = int(data[0])
    y = int(data[1])
    xdata = []
    ydata = []

    for i in range(x):
        xdata.append(sys.stdin.readline())
    for i in range(y):
        ydata.append(sys.stdin.readline())
    
    for i in range(x):
            for j in range(y):
                if xdata[i] == ydata[j]:
                    xdata.remove[i]
                    ydata.remove[y]
                elif xdata[i] != ydata[j]:
                    print(xdata[i])
