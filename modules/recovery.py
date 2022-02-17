# random
from random import randrange
import re

import globals

# manejo el estado recuperación de información


def recovery(text, lang='es'):
    last_messages = ['Recupere sus informaciones perdidas con nosotros',
                     'Recupere las informaciones que ha perdido']

    p = re.compile(
        r'\b(recupera(?:r|ci[o|ó]n)|restablec(?:er|imiento)|rescat(?:e|ar)|perder|p[e|é]rdida)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('decontamination')

        result_message = "Servicio de recuperación de información digital: garantizamos, si es posible, la recuperación de información dañada o perdida en el dispositivo del cliente, empleamos diferentes herramientas de software y aplicaciones informáticas. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
