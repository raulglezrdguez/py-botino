# random
from random import randrange
import re

import globals

# manejo el estado desarrollo e implementación de soluciones informáticas


def develop(text, lang='es'):

    last_messages = ['Consulte a nuestros profesionales',
                     'Desarrolle sus soluciones con nosotros', 'Mejore sus soluciones informáticas con nosotros']

    p = re.compile(
        r'\b(desarroll(?:o|ar?)|implementa(?:n|r|ci[o|ó]n)?)\b[\s*\w*]*(soluci[o|ó]n(?:es)?|inform[a|á]tic[a|o]s?)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        # globals.current_state = globals.find_handler_index('professional')
        result_message = "Servicio de desarrollo e implementación de soluciones informáticas: le desarrollamos, implementamos, documentamos y mantenemos las aplicaciones informáticas que necesite. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
