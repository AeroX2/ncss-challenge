import re

f = open("sentences.txt")
amount_of_lines = 0
amount_of_TLA = 0
for line in f:
    amount_of_lines+=1
    if (re.search(r"(?:\A|[^A-Z])+[A-Z]{3}(?:\Z|[^A-Z])+",line)):
        amount_of_TLA+=1
print("{:.1f}% of sentences contain a TLA".format((amount_of_TLA / amount_of_lines) * 100))
    
