# para recoger datos de http://www.insmet.cu/asp/genesis.asp?TB0=PLANTILLAS&TB1=INICIAL
import requests
# import urllib.request
import time
from bs4 import BeautifulSoup
import re

import re

# random
from random import randrange

import globals

# recojo los datos de "http://www.insmet.cu/asp/genesis.asp?TB0=PLANTILLAS&TB1=INICIAL"

def getData():
    proxies = {
        "http": "http://raul:todoporlaurita*01@127.0.0.1:8888",
        "https": "http://raul:todoporlaurita*01@127.0.0.1:8888",
    }
    url = "http://www.insmet.cu/asp/genesis.asp?TB0=PLANTILLAS&TB1=INICIAL"

    # visito la publicacion
    response = requests.get(url, proxies=proxies)
    doc = BeautifulSoup(response.text, 'html.parser')
    # print(doc)
    if doc:
        result = ''
        # estado del tiempo
        for time_state in doc.findAll('td', {'class': 'tituloPaginas'}):
            if time_state.text.strip() == 'Pronóstico del Tiempo':
                parent = time_state.parent.parent
                if parent != None:
                    parent = parent.find('td', {'class': 'contenidoPagina'})
                    if parent != None:
                        parent = parent.find('p')
                        if parent != None:
                            result = parent.text.strip()
        return result

    return ''

# manejo el estado weather: estado del tiempo
def weather(text, lang='es'):

    first_messages = ['El estado del tiempo es', 'El estado del tiempo que encontré es',
                      'El estado del tiempo en Cuba es', 'El estado del tiempo encontrado es']

    p = re.compile(
        r'\b(?:estado|condici[óo]n(?:es)?)\b\s*del\b\s*tiempo\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = 0

        estado = getData()

        result_message = "Me ha sido imposible acceder al estado del tiempo, inténtelo más tarde, o visite www.insmet.cu"
        if estado != '':
            result_message = "{}: {} Para más información visite http://www.insmet.cu/".format(first_messages[randrange(len(first_messages))], estado)

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
