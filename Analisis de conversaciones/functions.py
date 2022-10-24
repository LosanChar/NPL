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
    escrito = pd.ExcelWriter('resultados.xlsx')

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
import dateparser

#@Language.component ("expand_person_entities")
def expand_person_entities(doc):
    new_ents = []
    for ent in doc.ents:
        # Only check for title if it's a person and not the first token
        if ent.label_ == "PERSON":
            if ent.start != 0:
                # if person preceded by title, include title in entity
                prev_token = doc[ent.start - 1]
                if prev_token.text in ("Dr", "Dr.", "Mr", "Mr.", "Ms", "Ms."):
                    new_ent = Span(doc, ent.start - 1, ent.end, label=ent.label)
                    new_ents.append(new_ent)
                else:
                    # if entity can be parsed as a date, it's not a person
                    if dateparser.parse(ent.text) is None:
                        new_ents.append(ent) 
        else:
            new_ents.append(ent)
    doc.ents = new_ents
    return doc

import spacy
from spacy.symbols import nsubj, VERB
def ObtenerNombres(doc):
    nlp = spacy.load('en_core_web_sm')
    
    #nlp.add_pipe("expand_person_entities", after='ner')

    sents = nlp(doc)
    #names = [(ent.text, ent.label_) for ent in doc.ents if ent.label_=='PERSON']
    #names = [ee for ee in sents.ents if ee.label_ == 'PERSON']
    for ent in sents.ents:
        if(ent.label_ == 'PERSON' or ent.label_ == 'GPE'):
            print(ent.text, ent.label_)
    
    verbs = set()
    for possible_subject in sents:
        if possible_subject.dep == nsubj and possible_subject.head.pos == VERB:
            verbs.add(possible_subject.head)
    print(verbs)