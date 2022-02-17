# random
from random import randrange
import re

import globals

# manejo el estado coronavirus
# clasificación


def cv_classification(text, lang='es'):
    last_messages = ['Protéjase', 'Cuídese y cuide a su familia', 'Tome todas las medidas necesarias', 'No salga de casa',
                     'Manténgase alejado del contacto social', 'Cumpla las orientaciones de la dirección del país', 'Use nasobuco']

    p = re.compile(
        r'\b(?:clasifica|cataloga)[\s*\w*]*(corona *virus?|covid)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('cv_form')

        result_message = "La mayoría de los coronavirus infectan a los animales. Actualmente, se han aislado tres tipos de coronavirus de los humanos: coronavirus humanos 229E, OC43 y coronavirus del SARS (SARS-CoV). Hay 6 tipos de coronavirus previamente conocidos por infectar a los humanos. 229E y NL63 (de alfacoronavirus), OC43 (de betacoronavirus), HKU1, coronavirus del síndrome respiratorio de Oriente Medio (MERS-CoV) y coronavirus del síndrome respiratorio agudo severo (SARS-CoV). {}".format(
            last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
