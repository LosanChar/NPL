from lib2to3.pgen2 import token
import re
import pandas as pd
import numpy as np
import collections

def calculateBOW(wordset, l_doc):
    tf_diz = dict.fromkeys(wordset, 0)
    for word in l_doc:
        tf_diz[word] = l_doc.count(word)
    return tf_diz

doc1 = 'Game of Thrones is an amazing tv series!'
doc2 = 'Game of Thrones is the best tv series!'
doc3 = 'Game of Thrones is so great'

sentences = [doc1, doc2, doc3]

token_sentence = []

for sentence in sentences:
    token_sentence.append(re.sub(r"[^a-zA-Z0-9]", " ", sentence.lower()).split())

bows = []
for Token in token_sentence:
    bows = calculateBOW(wordset,Token)

df_bow = pd.DataFrame([bow1,bow2,bow3])
df_bow.head()