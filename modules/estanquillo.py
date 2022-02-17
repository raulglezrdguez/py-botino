# random
from random import randrange
import re

import globals

# manejo el estado estanquillo


def estanquillo(text, lang='es'):

    last_messages = ['Lea las revistas que tenemos en el estanquillo',
                     'Revise las publicaciones que ponemos a su alcance', 'Descargue las publicaciones y mantengase al día']

    p = re.compile(
        r'\bestanquillos?\b|\bpublicaci[o|ó]n(?:es)?\b|\blibros?\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('mochila')

        result_message = "Servicio Estanquillo: le brindamos la posibilidad de leer y descargar publicaciones seriadas nacionales e internacionales. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
