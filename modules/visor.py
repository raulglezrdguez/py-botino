# random
from random import randrange
import re

import globals


def visor(text, lang='es'):
    # manejo el estado visor
    last_messages = ['Comparta sus vídeos', 'Comparta sus fotos']

    p = re.compile(r'\bvisor\b|\bv[i|í]deos?\b|\bfotos?\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('mochila')

        result_message = "Servicio el Visor: le damos la posibilidad de tener su propio canal para compartir videos, fotos y documentos con todos los usuarios de la red. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
