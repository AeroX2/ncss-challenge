#!/bin/env python3
import math
import string
import re

def normalise(term):
    return term.strip(string.punctuation).lower()

def tf(t,d):
    print(re.findall("\w+",d,re.UNICODE).count(t))
    return re.findall("\w+",d,re.UNICODE).count(t)

def idf(t,D):
    number = 0
    for document in D:
        if re.findall("\w+",D[document],re.UNICODE).count(t) > 0:
            number += 1
    if number <= 0: return 0
    return math.log(len(D)/number)

file_names = input("Filenames: ")
query = input("Query: ")
documents = {}
if file_names:
    for file_name in file_names.split(" "):
        with open(file_name) as f:
            documents[file_name] = normalise(f.read().replace("\n"," "))

doc_relevance = {}
for document in documents:
    relevance = 0
    for term in query.split(" "):
        term = normalise(term)
        tf_n = tf(term,documents[document])
        idf_n = idf(term,documents)
        relevance += tf_n * idf_n
        #print(tf_n, idf_n, document)
    #print(relevance)
    doc_relevance[document] = relevance

sorted_relevance = sorted(doc_relevance, key=doc_relevance.get)[::-1]
for relevance in sorted_relevance:
    if doc_relevance[relevance] != 0:
        print(relevance)
