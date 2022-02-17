# random
from random import randrange
import re

import globals

# manejo el estado coronavirus


def cv(text, lang='es'):
    last_messages = ['Protéjase', 'Cuídese y cuide a su familia', 'Tome todas las medidas necesarias', 'No salga de casa',
                     'Manténgase alejado del contacto social', 'Cumpla las orientaciones de la dirección del país', 'Use nasobuco']

    p = re.compile(
        r'\b(corona *virus?|covid)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('cv_form')

        result_message = "Los coronavirus son virus de ARN de cadena positiva de cadena sencilla no segmentados. Pertenecen al orden Nidovirales, la familia Coronaviridae y la subfamilia Orthocoronavirinae. Los coronavirus pertenecen al género Coronavirus de la familia Coronaviridae. Lleva el nombre de las protuberancias en forma de corona en la envoltura del virus. El coronavirus recién descubierto es un coronavirus novedoso mutado (género B), que es nombrado 2019-nCoV por la OMS y SARS-CoV-2 por la ICTV. El 10 de enero de 2020, se completó la secuenciación genómica de la primera muestra de 2019- nCoV, y posteriormente se anunciaron las secuencias genómicas virales de cinco muestras más. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, ""
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
