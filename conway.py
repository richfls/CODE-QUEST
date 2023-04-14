import sys

cases = int(sys.stdin.readline().rstrip())
col = 10
row = 10


for num_cases in range(cases):
    map1 = []
    runtime = int(sys.stdin.readline().rstrip())
    for i in range(10):
        map1.append(list(sys.stdin.readline().rstrip()))
    for x in map1:
        print(*x, sep = "")
    
    map2 = map1[:]
    counter = 0
   # for x in map2:
   #     print(*x, sep = "")
    #update section--------------------------------------
    while runtime > 0:
        
        
        for i in range (col):
            for j in range(row):
                map1 = map2[:]
                counter = 0 #reset counter for each cell
                if i<9 and map1[i+1] [j] == '1': #check above
                    counter+=1
                    print("above is 1")
                if i>0 and map1[i-1] [j] == '1': #check down
                    counter+=1
                    print("below is 1")
                if j<9 and map1[i][j+1] == '1': #check right
                    counter+=1
                    print("right is 1")
                if j>0 and map1[i][j-1] == '1': #check checks left
                    counter+=1
                    print("left is 1")
                if i<9 and j<9 and map1[i+1][j+1]=='1': #check top right corner
                    counter+=1
                    print("bottomright is 1")
                if i>=0 and j<9 and map1[i-1][j+1]=='1': #check bottom right corner
                    counter+=1
                    print("bottom left is 1")
                if i<9 and j>=0 and map1[i+1][j-1]=='1': #check top left corner
                    counter+=1
                    print("staying alive")

        runtime -= 1
    for i in range (col):
        for j in range(row):
            if map2[i][j]=='0':
                map2[i][j] = 0
            
            if map2[i][j]=='1':
                map2[i][j] = 1
                
    
    for x in map2:
        print(*x, sep = "")

    
    
    
#end game loop--------------------------------------------------rint("topright is 1")
                if i>=0 and j>=0 and map1[i-1][j-1]=='1': #check bottom left corner
                    counter+=1
                    print("topleft is 1")
                
                #kill, live, or grow cells
                print("looking at cell", i, j, "and counter is", counter) 
                if map1[i][j]=='1' and counter <=1:
                     map2[i][j]='0' #cell dies from lonliness :'(
                     print("cell", i, j, "died from lonliness")
                elif map1[i][j]=='1' and counter >=4:
                    map2[i][j]='0'
                    print("cell", i, j, "died from over crowding")
                elif map1[i][j]=='0' and counter ==3:
                    map2[i][j]='1'
                    print("cell", i, j, "came alive")
                elif map1[i][j]=='1' and counter ==2:
                    print("staying alive")

        runtime -= 1
    for i in range (col):
        for j in range(row):
            if map2[i][j]=='0':
                map2[i][j] = 0
            
            if map2[i][j]=='1':
                map2[i][j] = 1
                
    
    for x in map2:
        print(*x, sep = "")

    
    
    
#end game loop--------------------------------------------------
