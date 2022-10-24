from functions import GenerarDF
from functions import AplicarWebScrap
from functions import LimpiarTexto
from functions import ObtenerNombres

print("Ingresa el url:")
url = input()
chatTxtPlain = AplicarWebScrap(url)
#ObtenerNombres(chatTxtPlain)
sentences_tokens = LimpiarTexto(chatTxtPlain)
GenerarDF(sentences_tokens)
