# random
from random import randrange
import re

import globals

# manejo el estado atencion a niños talentos


def talent(text, lang='es'):
    last_messages = ['Haga que sus niños estudien con nosotros',
                     'Lleve sus niños a Joven Club', 'Ayude a sus niños a estudiar']

    p = re.compile(r'\b(talento[s]?)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('course')

        result_message = "Servicio de atención a niños talentos: los niños talentos pueden participar con nosotros en cursos especializados para que ejerciten sus capacidades en el desarrollo de tecnologías. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
