# devuelve la hora que tiene
import datetime
import re

# random
from random import randrange

import globals


def what_time(text, lang='es'):
    # manejo el estado que hora es
    first_messages = ['Tengo las', 'En mi reloj tengo las',
                      'Mi reloj tiene las', 'Mi reloj marca las']

    p = re.compile(
        r'\b(qu[ée]\s*h?ora\s*(?:es|tienes?))\b|\b((d[a|i]me|tienes?)\s*(?:la\s*)?h?ora)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = 0
        now = datetime.datetime.now()

        result_message = "{}: {} horas y {} minutos".format(
            first_messages[randrange(len(first_messages))], now.hour, now.minute)

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
