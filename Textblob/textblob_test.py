from textblob import TextBlob

wiki = TextBlob("Python is a high-level, general-purpose programming language.")
# etiquetado 
tags = wiki.tags
print (tags)
print ("--------------------")
phrases = wiki.noun_phrases
print (phrases)
print ("--------------------")
words = wiki.words
print (words)
print ("--------------------")
sentences = wiki.sentences
for sentence in sentences:
    print(sentence)
    print(sentence.sentiment)
print ("--------------------")