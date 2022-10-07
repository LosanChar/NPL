from functions import GenerarDF
from functions import AplicarWebScrap
from functions import LimpiarTexto

print("Ingresa el url:")
url = input()
chatTxtPlain = AplicarWebScrap(url)
sentences_tokens = LimpiarTexto(chatTxtPlain)
GenerarDF(sentences_tokens)
