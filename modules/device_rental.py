# random
from random import randrange
import re

import globals

# manejo el estado alquiler de computadoras y dispositivos


def device_rental(text, lang='es'):

    last_messages = ['Utilice nuestra tecnología', 'Trabaje con nuestros equipos',
                     'Desarrolle sus proyectos con nosotros', 'Ejercite sus conocimientos con nosotros']

    p = re.compile(r'\b(?:alquil[e|a]r|rentar?|arriend[o|a])\b[\s*\w*]*(?:m[a|á]quinas?|computador(?:as?)?|ordenador(?:es)?|microcomputador(?:as?)?|microo?rdenador(?:es)?|dispositivos?|m[o|ó]vil(?:es)?|tel[e|é]fonos?|tabletas?|pc)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('machine_time')

        result_message = "Servicio de alquiler de computadoras y dispositivos móviles: puede alquilar nuestras computadoras, tabletas y teléfonos móviles para desarrollar sus ideas. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
