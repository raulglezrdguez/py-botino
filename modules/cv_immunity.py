# random
from random import randrange
import re

import globals

# manejo el estado coronavirus
# inmunidad


def cv_immunity(text, lang='es'):
    last_messages = ['Protéjase', 'Cuídese y cuide a su familia', 'Tome todas las medidas necesarias', 'No salga de casa',
                     'Manténgase alejado del contacto social', 'Cumpla las orientaciones de la dirección del país', 'Use nasobuco']

    p = re.compile(
        r'\b(?:inmune|inmunidad|invulnerable|inatacable|inmunizad[oa])[\s*\w*]*(corona *virus?|covid)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('cv_form')

        result_message = "Los datos científicos sobre el nivel y la duración de los anticuerpos inmunes protectores producidos en pacientes después de la infección del nuevo coronavirus siguen siendo escasos. En general, los anticuerpos protectores contra un virus pueden producirse aproximadamente dos semanas después de una infección, y pueden existir durante varias semanas o muchos años, evitando la reinfección del mismo virus después de la recuperación. Actualmente, se están realizando esfuerzos para evaluar personas que recientemente se recuperaron de la infección 2019-nCoV y se evalúa si portan anticuerpos protectores en la sangre. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
