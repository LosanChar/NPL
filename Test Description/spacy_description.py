import string
from spacy.lang.es import Spanish
from spacy.lang.es.stop_words import STOP_WORDS
from typing import OrderedDict
from collections import Counter

# Load Spanish tokenizer, tagger, parser, NER and word vectors
nlp = Spanish()

with open('./Test Description/file.txt', 'r', encoding="utf8") as MyFile:
    texto = MyFile.read()

#  "nlp" Object is used to create documents with linguistic annotations.
my_doc = nlp(texto)
# Create list of word tokens
token_list = []
for token in my_doc:
    token_list.append(token.text)

token_list = list(filter(lambda token: token not in string.punctuation, token_list))


# Create list of word tokens after removing stopwords
filtered_sentence =[] 

for word in token_list:
    lexeme = nlp.vocab[word]
    if lexeme.is_stop == False:
        filtered_sentence.append(word) 

c = Counter(filtered_sentence)
print(c.most_common(4))
y = OrderedDict(c.most_common())

with open('./Test Description/resultados_spacy.txt', 'w', encoding="utf8") as f:
    for k,v in y.items():
        f.write(f'{k} {v}\n')