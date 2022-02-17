# random
from random import randrange
import re

import globals

# manejo el estado elaboracion de planes de seguridad informatica


def security(text, lang='es'):
    last_messages = ['Reciba la asistencia de nuestros profesionales',
                     'Consulte a nuestros profesionales']

    p = re.compile(
        r'\b(plan(?:es)?)\b[\s*\w*]*(seguridad|inform[a|á]ticas?|prote(?:ger|cci[o|ó]n))\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('advisory')
        result_message = "Servicio de elaboración de planes de seguridad informática: le ayudamos a establecer las políticas y medidas de seguridad informática para la protección de su información y sus tecnologías. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
