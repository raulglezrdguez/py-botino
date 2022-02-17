# random
from random import randrange
import re

import globals

# manejo el estado impresion de documentos


def printer(text, lang='es'):

    last_messages = ['Imprima sus documentos en nuestras instalaciones',
                     'Saque impresos de sus imágenes con nosotros', 'Utilice nuestro servicio de impresión']

    p = re.compile(
        r'\b(imprimir(?:se)?|impresi[o|ó]n(?:es)?|impresos?)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('machine_time')

        result_message = "Servicio de impresión de documentos: usted puede imprimir sus documentos en nuestras instalaciones. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
