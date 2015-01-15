import re

def novowelsort(l):
    return sorted(l, key=lambda word: re.sub("[aeiouAEIOU]","",word))
    
