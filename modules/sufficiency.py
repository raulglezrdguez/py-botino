# random
from random import randrange
import re

import globals

# manejo el estado exámenes de suficiencia


def sufficiency(text, lang='es'):
    last_messages = ['Pruebe sus conocimientos',
                     'Reciba su diploma', 'Estudie con nosotros']

    p = re.compile(r'\b(suficiencia[s]?|suficiente[s]?)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('course')
        result_message = "Servicio de exámenes de suficiencia: le ofrecemos la facilidad de validar sus conocimientos en temas relacionados con la informática y la electrónica a partir de las materias que se imparten en Joven Club, para así obtener el título correspondiente sin vincularse al proceso docente que impartimos. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
