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
        month = "03"
    elif date > 31:
        date -= 31
        month = "04"
        if date == 25 and d == 28 and 3 == 6 and f < 19:
            date = 18
        elif date == 26 and d == 29 and e == 6:
            date = 19
        else:
            if date <=9:
                date = '0' + str(date)
    print(f"{year}/{month}/{date}")
        
for num_cases in range(cases):
    year = int(sys.stdin.readline().rstrip())
    eastersunday(year)
