# random
from random import randrange
import re

import globals

# manejo el estado reflejos


def reflejos(text, lang='es'):

    last_messages = ['Cree su blog personal',
                     'Exprese sus ideas en su blog personal', 'Comparta sus ideas con nosotros']

    p = re.compile(r'\breflejos?|blogs?|opini[o|ó]n(?:es)?\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('mochila')

        result_message = "Servicio Reflejos: le damos la posibilidad de acceder a un espacio en el que puede crear su blog personal y expresar sus opiniones. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
