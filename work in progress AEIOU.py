import sys

cases = int(sys.stdin.readline().rstrip())
sentence = []
num = 0
for i in range(cases):
    sentence.append(sys.stdin.readline().rstrip())

    
for letter in sentence:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        num += 1
print (num)
