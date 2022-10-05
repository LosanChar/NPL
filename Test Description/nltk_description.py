#para eliminar stopwords
from typing import OrderedDict
import unicodedata
from nltk.corpus import stopwords
#para tokenizar texto
from nltk.tokenize import  word_tokenize
import string

#leemos archivo
with open('./Test Description/file.txt', 'r', encoding="utf8") as MyFile:
    texto = MyFile.read()

stop_words = set(stopwords.words('spanish'))
word_tokens = word_tokenize(texto, 'spanish')
#filtro para reitrar signos de puntuacion
word_tokens = list(filter(lambda token: token not in string.punctuation, word_tokens))

filtro = []
for token in word_tokens:
    if token not in stop_words:
        filtro.append(token)

from collections import Counter
c = Counter(filtro)
print(c.most_common(4))
y = OrderedDict(c.most_common())

with open('./Test Description/resultados_nltk.txt', 'w', encoding="utf8") as f:
    for k,v in y.items():
        f.write(f'{k} {v}\n')



