import sys
cases = int(sys.stdin.readline().rstrip())
for num_cases in range(cases):
    yearamount = int(sys.stdin.readline().rstrip())
    for years in range(yearamount):
        year = int(sys.stdin.readline().rstrip())
        if year < 1582:
            print("No")
        elif year%4 != 0:
            print("No")
        elif year%100 != 0:
            print("Yes")
        elif year%400 != 0:
            print("No")
        else:
            print("Yes")
