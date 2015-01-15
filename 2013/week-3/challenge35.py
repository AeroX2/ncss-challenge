import string
from math import sqrt

def sim(a,b):
    while (len(a) != len(b)):
        if (len(a) > len(b)):
            b.append(0)
        else:
            a.append(0)
    sum = 0
    sumA = 0
    sumB = 0
    for i in range(len(a)):
        sum += a[i] * b[i]
        sumA += a[i]**2
        sumB += b[i]**2
    return sum / (sqrt(sumA) * sqrt(sumB))

def biggest_word(file_text):
    i = 0
    for word in file_text:
        word = word.strip(string.punctuation)
        if (len(word) > i):
            i = len(word)
    return i

def find_freq(file_text):
    freqs = [0] * biggest_word(file_text)
    for word in file_text:
        word = word.strip(string.punctuation)
        if (word != ""):
            freqs[len(word)-1] += 1
    return freqs

file = open("texts.txt")
file2 = open("unknown.txt")

freq1 = find_freq(file2.read().split())
blub = []
new = []

for line in file:
    if (line.strip() != ""):
        file3 = open(line.strip())
        freq2 = find_freq(file3.read().split())
    new.append((float(sim(freq1,freq2)),line.strip()))
blub = sorted(new, key=lambda x:(-x[0], x[1]))
for i in blub:
    print("{:.3f} {}".format(i[0],i[1]))
