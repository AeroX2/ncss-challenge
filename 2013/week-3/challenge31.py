file = open("words.txt")
blub = set()
blub2 = []
for word in file:
    for character in range(len(word)-1):
        if (word[character] == word[character+1]):
            blub.add(word[character])
    if (len(blub) > 2):
        blub2.append(word.strip())
    blub = set()
blub2.sort()
for i in blub2:
    print(i)
    
