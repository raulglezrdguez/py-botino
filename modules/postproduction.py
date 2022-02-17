# random
from random import randrange
import re

import globals

# manejo el estado postproducción de audiovisuales


def postproduction(text, lang='es'):

    last_messages = ['Edite sus materiales audiovisuales con nosotros',
                     'Mejore sus audiovisuales con Joven Club']

    p = re.compile(r'\bpost *producci[o|ó]n\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('decontamination')

        result_message = "Servicio de postproducción de audiovisuales: editamos sus materiales audiovisuales con el objetivo de mejorar su calidad. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
