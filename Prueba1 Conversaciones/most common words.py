#para eliminar stopwords
from dataclasses import replace
from typing import OrderedDict
import unicodedata
from unittest import skip
from nltk.corpus import stopwords
#para tokenizar texto
from nltk.tokenize import  word_tokenize
import string

#leemos archivo
with open('./Conversation/CONV_1.csv', 'r' ,encoding="utf8") as MyFile:
    texto = MyFile.read()

texto = texto.replace(',',' ')
texto = texto.lower()
print(texto)

stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(texto, 'english')
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


with open('./Prueba1 Conversaciones/Resultados Oraciones/resultados_conversacion1.txt', 'w', encoding="utf8") as f:
    for k,v in y.items():
        f.write(f'{k} {v}\n')

'''
import matplotlib.pyplot as plt
DictionaryWords = y
myList = Counter(DictionaryWords).most_common(10)
x, y = zip(*myList) 

plt.plot(x, y)
plt.show()

'''
