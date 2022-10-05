from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from nltk.tokenize import sent_tokenize

with open('./Conversation/CONV3.txt', 'r' ,encoding="utf8") as MyFile:
    texto = MyFile.read()

texto = texto.replace('\n','.\n')
print(texto)
sent_tokens = sent_tokenize(texto, 'english')
print(sent_tokens)

vectorizer = CountVectorizer(stop_words='english', ngram_range=(2,2))
X = vectorizer.fit_transform(sent_tokens)

df_bow_sklearn = pd.DataFrame(X.toarray(), columns = vectorizer.get_feature_names_out())
df_bow_sklearn.head()

df_bow_sklearn.to_csv("./Bag of Words/df.csv")
