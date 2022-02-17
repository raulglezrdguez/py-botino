# random
from random import randrange
import re

import globals

# manejo el estado navegación y correo nacional


def navigation(text, lang='es'):

    last_messages = ['Disfrute de la navegación nacional en nuestras instalaciones',
                     'Utilice el servicio de correo nacional con nosotros', 'Utilice la navegación nacional con nosotros']

    p = re.compile(
        r'\b(navega(?:r|ci[ó|o]n)|nautas?|emails?|correos?|mensaje(?:s|r[i|í]as?)?)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('machine_time')

        result_message = "Servicio de navegación y correo electrónico nacional: le brindamos la posibilidad de acceder a los servicios de navegación y mensajería de la red de Joven Club y de la intranet cubana. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
