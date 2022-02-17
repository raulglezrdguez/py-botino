# para recoger datos de http://www.insmet.cu/asp/genesis.asp?TB0=PLANTILLAS&TB1=INICIAL
import requests
import urllib.request
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
    "http": "http://raul:todoporlaurita*01@10.5.44.2:1080",
    "https": "http://raul:todoporlaurita*01@10.5.44.2:1080",
    }
    url = "http://www.insmet.cu/asp/genesis.asp?TB0=PLANTILLAS&TB1=INICIAL"

    # visito la publicacion
    response = requests.get(url, proxies=proxies)
    doc = BeautifulSoup(response.text, 'html.parser')
    # temperatura maxima
    t_max = doc.find('td', id="tmax").text.split(':')[1].strip()
    # print(t_max)

    # temperatura minima
    t_min = doc.find('td', id="tmin").text.split(':')[1].strip()
    # print(t_min)

    # estado del tiempo
    estado = doc.find('td', id="estado").text
    # print(estado)

    return t_max, t_min, estado

# manejo el estado time_state
def time_state(text):

    first_messages = ['El estado del tiempo es', 'El estado del tiempo que encontré es', 'El estado del tiempo en Cuba es', 'El estado deltiempo encontrado es']

    p = re.compile(r'\b(qu[ée]\b\s*h?ora\b\s*(?:es|tienes?))\b|\b(tienes?\b\s*(?:la\b\s*)?h?ora)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = 0
        
        t_max, t_min, estado = getData()

        result_message = "{}: temperatura máxima {} grados centígrados, temperatura mínima {} grados centígrados. {}".format(first_messages[randrange(len(first_messages))], t_max, t_min, estado)

        return result_message, None
    else:
        return None, None

