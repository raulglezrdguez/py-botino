# random
from random import randrange
import re

import globals

# manejo el estado tiempo de maquina


def machine_time(text, lang='es'):
    last_messages = ['Utilice nuestra tecnología', 'Trabaje con nuestros equipos',
                     'Desarrolle sus proyectos con nosotros', 'Ejercite sus conocimientos con nosotros']

    p = re.compile(r'\btiempos?\b[\s*\w*]*\bm[a|á]quinas?\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        # globals.current_state = globals.find_handler_index('interior')
        result_message = "Servicio de tiempo de máquina: le prestamos nuestros dispositivos para que desarrolle sus proyectos personales, se dedique al ocio y ejercite sus conocimientos. En estas actividades nuestros especialistas le pueden ayudar. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
