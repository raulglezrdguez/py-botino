# random
from random import randrange
import re

import globals

# manejo el estado restauracion de imágenes y documentos


def restore(text, lang='es'):

    last_messages = ['Renueve sus imágenes con nosotros',
                     'Restaure sus documentos en Joven Club']

    p = re.compile(
        r'\b(restaura(?:r|ci[o|ó]n)|renova(?:r|ci[o|ó]n))\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('decontamination')

        result_message = "Servicio de restauración digital de imágenes y documentos: le aplicamos técnicas y herramientas a las imágenes y documentos, con el objetivo de mejorar su calidad y restaurar los daños ocasionados. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
