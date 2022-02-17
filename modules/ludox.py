# random
from random import randrange
import re

import globals


def ludox(text, lang='es'):
    # manejo el estado ludox
    last_messages = ['Juegue en nuestra red', 'Disfrute de los videojuegos que le ofertamos',
                     'Cree sus videojuegos y publíquelos con nosotros']

    p = re.compile(
        r'\bludox\b|\bdistra(?:er(?:nos)?|cci[o|ó]n(?:es)?)\b|\bdiver(?:tir(?:nos)?|si[o|ó]n(?:es)?)\b|\brecrea(?:r(?:se)?|ci[o|ó]n(?:es)?)?\b|\bocios?\b|\bvideojuegos?\b|\bjugar\b|\bjueg[a|o]s?\b|\bentreten(?:er(?:nos|l[o|a]s?|me|se)?)?\b|\bentretenimientos?\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('mochila')

        result_message = "Servicio de Ludox: le presentamos una amplia gama de videojuegos que puede disfrutar desconectado o desde la red. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
