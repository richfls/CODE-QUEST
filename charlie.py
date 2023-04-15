import sys
import string
cases = int(sys.stdin.readline().rstrip())
Nato = {'A' : "Alpha",'B' : "Bravo",'C' : "Charlie",
        'D' : "Delta",'E' : "Echo",'F' : "Foxtrot",
        'G' : "Golf",'H' : "Hotel",'I' : "India",
        'J' : "Juliet",'K' : "Kilo",'L' : "Lima",
        'M' : "Mike",'N' : "November",'O' : "Oscar",
        'P' : "Papa",'Q' : "Quebec",'R' : "Romeo",
        'S' : "Sierra",'T' : "Tango",'U' : "Uniform",
        'V' : "Victor",'W' : "Whiskey",'X' : "Xray",
        'Y' : "Yankee",'Z' : "Zulu"
        }
def Word(WORDS):
    natoword = ""
    for character in WORDS:
        if character == ' ':
            natoword = natoword.rstrip(natoword[-1])
            natoword +=' '
        else:
            natoword += Nato[character]
            natoword += '-'

    natoword = natoword.rstrip(natoword[-1])
    print(natoword)
    
for num_cases in range(cases): 
    RUNS = int(sys.stdin.readline().rstrip())
    for runs in range(RUNS):
        WORDS = sys.stdin.readline().rstrip().upper()
        Word(WORDS)
