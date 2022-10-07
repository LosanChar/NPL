from array import array
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
    for fila in filas:
        for itm in fila:
            if(itm != 0):
                subfila.append(itm)
                subcolumnas.append(columnas[i])
            i = i+1
        arreglo = np.array(subfila)
        df_tmp = pd.DataFrame(arreglo,subcolumnas)
        df_tmp.head()
        i = 0
        j = j+1
        subfila = []
        subcolumnas = []
        print(df_tmp.to_markdown())
        print("\n")

    '''
    print(filas[0][0])
    print("\n ----------------------------------------------- \n")
    print(vectorizer.get_feature_names_out())

    df_bow_sklearn = pd.DataFrame(filas, columnas)
    df_bow_sklearn.head()

    df_bow_sklearn.to_csv("./Analisis de conversaciones/df.csv")
    '''