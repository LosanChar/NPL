#para eliminar stopwords
from typing import OrderedDict
import unicodedata
from textblob import TextBlob
from nltk.corpus import stopwords
import string

#leemos archivo
with open('./Test Description/file.txt', 'r', encoding="utf8") as MyFile:
    texto = MyFile.read()

text=TextBlob(texto)
# Tokens
tokens=set(text.words)

tokens = list(filter(lambda token: token not in string.punctuation, tokens))
print(tokens)
# stopwords
stop=set(stopwords.words("spanish"))

filtro = []
for token in tokens:
    if token not in stop:
        filtro.append(token)

from collections import Counter
c = Counter(filtro)
print(c.most_common(4))
y = OrderedDict(c.most_common())

with open('./Test Description/resultados_textblob.txt', 'w', encoding="utf8") as f:
    for k,v in y.items():
        f.write(f'{k} {v}\n')

