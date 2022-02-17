# random
from random import randrange
import re

import globals

# manejo el estado asesoría e implementación


def advisory(text, lang='es'):

    last_messages = ['Reciba la asesoría de nuestros profesionales',
                     'Consulte a nuestros profesionales']

    p = re.compile(
        r'\b(asesor(?:[i|í]a|[a|e]r?|amientos?)|consult(?:or[i|í]a|ar?))\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('assistance')

        result_message = "Servicio de asesoría e implementación: le brindamos asistencia especializada en temas relacionados al procesamiento de información digital, redes informáticas y configuración de software. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
