# random
from random import randrange
import re

import globals

# manejo el estado coronavirus
# epidemia


def cv_epidemic(text, lang='es'):
    last_messages = ['Protéjase', 'Cuídese y cuide a su familia', 'Tome todas las medidas necesarias', 'No salga de casa',
                     'Manténgase alejado del contacto social', 'Cumpla las orientaciones de la dirección del país', 'Use nasobuco']

    p = re.compile(
        r'\b(?:epidemia|peste|endemia|pandemia|plaga)[\s*\w*]*(corona *virus?|covid)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('cv_form')

        result_message = "Debido a las mutaciones antigénicas del coronavirus se considera un nuevo virus para los humanos, la población general carece de inmunidad contra la nueva cepa. Además, hay más de una ruta de transmisión para este virus. Estos factores provocaron que el nuevo coronavirus se volviera epidémico. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
