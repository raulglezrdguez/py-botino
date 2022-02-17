# random
from random import randrange
import re

import globals

# manejo el estado digitalización de imágenes y documentos


def digitization(text, lang='es'):

    last_messages = ['Digitalice sus imágenes con nosotros',
                     'Digitalice sus documentos en Joven Club']

    p = re.compile(
        r'\b(digitali(?:zar|ce|zaci[o|ó]n)|e?scann?e(?:r|ar))\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('decontamination')

        result_message = "Servicio de digitalización de imágenes y documentos: le brindamos la posibilidad de convertir sus documentos, imágenes u otros en formato digital. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
