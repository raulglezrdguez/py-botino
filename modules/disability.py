# random
from random import randrange
import re

import globals


def disability(text, lang='es'):
    # manejo el estado actividades a personas con discapacidad
    last_messages = ['Ayude a las personas con incapacidad',
                     'Lleve las personas con impedimentos a Joven Club', 'Anime a los minusválidos a superarse']

    p = re.compile(
        r'\b(discapacidad(?:es)?|discapacitad[o|a]s?|incapacitad[o|a]s?|incapacidad|invalidez|inv[a|á]lid[o|a]s?|impedimentos?|impedid[o|a]s?|minusvalidez|minusv[a|á]lid[o|a]s?)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        # globals.current_state = globals.find_handler_index('activities')
        result_message = "Servicio de actividades a personas con discapacidad: le brindamos actividades a las personas con discapacidad para que participen en los procesos sociales a través de la utilización de las tecnologías. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
