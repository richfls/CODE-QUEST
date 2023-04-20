import sys


cases = int(sys.stdin.readline().rstrip())
elementlist = ["Wood","Fire","Earth","Metal","Water"]
animallist = ["Rat","Ox","Tiger","Rabbit","Dragon","Snake","Horse","Goat","Monkey","Rooster","Dog","Pig"]
def elem(year):
        year -= 4
        year %= 10
        year /= 2
        return elementlist[int(year)]
def anim(year):
        year -= 4
        year %= 12
        return animallist[int(year)]
        
for num_cases in range(cases):
    year = int(sys.stdin.readline().rstrip())
    
    if year%2 ==0:
        print(year,"Yang",elem(year),anim(year))
    else:
        print(year,"Yin",elem(year),anim(year))
