import sys
import math
cases = int(sys.stdin.readline().rstrip())

def eastersunday(year):
    y = year
    a = y%19
    b = y%4
    c = y%7
    k = y//100
    p = (13+(8*k))//25
    q = k//4
    m = (15-p+k-q)%30
    n = (4+k-q)%7
    d = (19*a+m)%30
    e = (2*b+4*c+6*d+n)%7
    f = (11*m +11)%30
    date = 22+d+e
    
    if date <=31:
        month = 3
    else:
        date -= 31
        month = 4
        
    if month == 4 and date == 25 and d == 28 and e == 6 and f < 19:
        date = 18
    elif month == 4 and date == 26 and d == 29 and e == 6:
        date = 19
    
    if date >9:
        print(f"{year}/0{month}/{date}")
    else:
        print(f"{year}/0{month}/0{date}")
        
for num_cases in range(cases):
    year = int(sys.stdin.readline().rstrip())
    eastersunday(year)
