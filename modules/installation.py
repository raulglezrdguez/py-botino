# random
from random import randrange
import re

import globals

# manejo el estado instalación de aplicaciones y periféricos


def installation(text, lang='es'):

    last_messages = ['Reciba la asistencia de nuestros profesionales',
                     'Consulte a nuestros profesionales']

    p = re.compile(
        r'\b(instal(?:ar?|aci[o|ó]n|en))\b[\s*\w*]*(aplicaci[o|ó]n(?:es)?|perif[e|é]ricos?)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('advisory')
        result_message = "Servicio de instalación de aplicaciones y periféricos: le instalamos antivirus, controladores, paquetes de ofimática y periféricos en sus computadoras y dispositivos. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
