import sys
import string
cases = int(sys.stdin.readline().rstrip())
Nato = {'A' : "Aplha",'B' : "Bravo",'C' : "Charlie",
        'D' : "Delta",'E' : "Echo",'F' : "Foxtrot",
        'G' : "Golf",'H' : "Hotel",'I' : "India",
        'J' : "Juliet",'K' : "Kilo",'L' : "Lima",
        'M' : "Mike",'N' : "November",'O' : "Oscar",
        'P' : "Papa",'Q' : "Quebec",'R' : "Romeo",
        'S' : "Sierra",'T' : "Tango",'U' : "Uniform",
        'V' : "Victor",'W' : "Whiskey",'X' : "Xray",
        'Y' : "Yankee",'Z' : "Zulu",
        }

for num_cases in range(cases):
    line = sys.stdin.readline().rstrip().upper()
