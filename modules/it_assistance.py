# random
from random import randrange
import re

import globals

# manejo el estado asistencia informática


def it_assistance(text, lang='es'):

    last_messages = ['Reciba la asistencia de nuestros profesionales',
                     'Consulte a nuestros profesionales']

    p = re.compile(
        r'\b((?:asist(?:en?|an?|ir|encias?|entes?)|ayudan(?:te)?|ayudar?)|ayudan(?:te)?|ayudar?)[\s*\w*]*(?:inform[a|á]tic[o|a]s?|m[o|ó]vil(?:es)?|tel[e|é]fonos?|tabletas?|domicilios?|casas?|hogar(?:es)?)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('advisory')

        result_message = "Servicio de asistencia informática: disponemos de personal capacitado en redes de comunicación, sistemas operativos, bases de datos y dispositivos móviles para ayudarle en su domicilio. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
