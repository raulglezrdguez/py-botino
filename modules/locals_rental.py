# random
from random import randrange
import re

import globals

# manejo el estado alquiler de locales


def locals_rental(text, lang='es'):

    last_messages = ['Utilice nuestras instalaciones', 'Trabaje en nuestras instalaciones',
                     'Desarrolle sus proyectos en nuestros laboratorios', 'Ejercite sus conocimientos en nuestros laboratorios']

    p = re.compile(
        r'\b(?:alquil[e|a]r|rentar?|arriend[o|a])\b[\s*\w*]*(?:local(?:es)?|laboratorios?|habitaci[ó|o]n(?:es)?|[á|a]reas?)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('machine_time')

        result_message = "Servicio de alquiler de locales: ponemos a su disposición los locales de Joven Club para la realización de reuniones, talleres, eventos u otras actividades similares. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
