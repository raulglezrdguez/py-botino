# random
from random import randrange
import re

import globals

# manejo el estado circulos de interes


def interest(text, lang='es'):
    last_messages = ['Haga que sus niños estudien con nosotros',
                     'Lleve sus niños a Joven Club', 'Ayude a sus niños a estudiar']

    p = re.compile(r'\b(c[i|í]rculo[s]?|inter[e|é][s]?)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('course')
        result_message = "Servicio de círculos de interés: le brindamos la posibilidad a los estudiantes de las enseñanzas primaria, secundaria y preuniversitaria de participar en nuestros círculos de interés. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
