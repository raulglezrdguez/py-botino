# random
from random import randrange
import re

import globals


def course(text, lang='es'):
    # manejo el estado cursos
    last_messages = ['Participe con nosotros',
                     'Visite nuestras instalaciones', 'Estudie con nosotros']

    p = re.compile(
        r'\b(curso[s]?|cursar|capacita[n|r]?|capacitaci[o|ó]n|postgrado)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        # globals.current_state = globals.find_handler_index('training')
        result_message = "Servicio de cursos: este servicio está dirigido a la formación, capacitación y preparación de competencias en contenidos relacionados con las tecnologías de la información y la electrónica; a través de cursos regulares y de postgrado. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
