# random
from random import randrange
import re

import globals

# manejo el estado actividades a geroclub


def geroclub(text, lang='es'):
    last_messages = ['Ayude a los adultos mayores',
                     'Lleve a los adultos mayores a Joven Club', 'Anime a los adultos mayores a superarse']

    p = re.compile(
        r'\b(\bgeroclub\b|\badult[a|o]s?\b[\s*\w*]*\bmayor(?:es)?\b)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('disability')

        result_message = "Servicio de actividades a Geroclub: participamos con los adultos mayores en un grupo de  actividades que ofrecemos para que se actualicen en el uso de las tecnologías de la información. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
