from array import array
from cProfile import label
from bs4 import BeautifulSoup
import requests

def AplicarWebScrap(URL):
    #url = 'http://www.perverted-justice.com/?archive=mg0942'
    #estableemos conexion con la url
    url = URL
    result = requests.get(url)

    #usamos libreria para generar un parser html y analizar el codigo fuente
    content = result.text
    soup = BeautifulSoup(content, 'html.parser')
    
    #buscamos la etiqueta que contiene la conversacion
    chatTxtPlain = soup.body.find('div',attrs={'class':'chatLog'}).text
    #test = soup.body.find('span',attrs={'class':'code_chat'}).b.text
    return chatTxtPlain


from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
import numpy as np

def LimpiarTexto(texto):
    texto = texto.replace('\r\n','\n')
    texto = texto.replace('\n\n','\n')
    texto = texto.replace('\n','. ')
    #print(texto)
    sent_tokens = sent_tokenize(texto, 'english')
    '''
    i = 0
    for itm in sent_tokens:
        print(str(i)+" - "+itm+" \n")
        i = i+1
    '''
    return sent_tokens

def GenerarDF(tokens):
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(tokens)
    
    filas = X.toarray()
    columnas = vectorizer.get_feature_names_out()

    subfila = []
    subcolumnas = []
    i = 0
    j = 0
    row = 0
    escrito = pd.ExcelWriter('./Analisis de conversaciones/resultados.xlsx')

    for fila in filas:
        for itm in fila:
            if(itm != 0):
                subfila.append(itm)
                subcolumnas.append(columnas[i])
            i = i+1
        arreglo = np.array(subfila)
        df_tmp = pd.DataFrame(arreglo, subcolumnas)
        df_trans = df_tmp.transpose()        
        df_trans.to_excel(escrito, startrow= row)
        
        row = row + 3
        i = 0
        j = j+1
        subfila = []
        subcolumnas = []
        print(df_trans.to_markdown())
        print("\n")

    escrito.save()
    escrito.close()  

    '''
    print(filas[0][0])
    print("\n ----------------------------------------------- \n")
    print(vectorizer.get_feature_names_out())

    df_bow_sklearn = pd.DataFrame(filas, columnas)
    df_bow_sklearn.head()

    df_bow_sklearn.to_csv("./Analisis de conversaciones/df.csv")
    '''

from spacy.tokens import Span
import spacy
from spacy.symbols import nsubj, VERB

def ObtenerNombresYVerbos(doc):
    nlp = spacy.load('en_core_web_sm')
    sents = nlp(doc)

    names = set()
    for ent in sents.ents:
        if(ent.label_ == 'PERSON' or ent.label_ == 'GPE'):
            names.add(ent.text)
            #print(ent.text, ent.label_)

    CreateBagOfWords(names,"BoW-names.csv")

    verbs = []
    for possible_subject in sents:
        if possible_subject.dep == nsubj and possible_subject.head.pos == VERB:
            verbs.append(possible_subject.head.text)
    
    CreateBagOfWords(verbs, "Bow-verbs.csv")

    #print(verbs)

from spacy.matcher import Matcher
def ObtenerAdjetivos(txt):
    nlp = spacy.load('en_core_web_sm')
    matcher = Matcher(nlp.vocab)

    patterns = [
        [{'POS':'ADJ'}, {'POS':'NOUN'}],
        ]
    matcher.add("chat", patterns)

    doc = nlp(txt)
    matches = matcher(doc)

    adjetives = []

    for match_id, start, end in matches:
        span = doc[start:end]  # The matched span
        adjetives.append(span.text)

    CreateBagOfWords(adjetives, "BoW-adjetives.csv")

def CreateBagOfWords(token_list, name_file):
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(token_list)

    df_bow_sklearn = pd.DataFrame(X.toarray(), columns = vectorizer.get_feature_names_out())
    df_bow_sklearn.head()

    df_bow_sklearn.to_csv("./Analisis de conversaciones/"+name_file)

    


