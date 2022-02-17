# random
from random import randrange
import re

import globals

# manejo el estado licencias de antivirus segurmatica


def segurmatica(text, lang='es'):
    patterns = [
        {'name': 'p1', 'pattern': [{'LOWER': {
            'IN': ['licencia', 'licencias', 'segurmatica', 'segurmática', 'antivirus']}}]},
    ]
    last_messages = ['Adquiera la licencia para segurmática',
                     'Proteja sus dispositivos con segurmática antivirus', 'Utilice el antivirus segurmática para Cuba']

    p = re.compile(
        r'\b(licencias?|segurm[a|á]tica|antivirus?)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('course')

        result_message = "Servicio de Venta de Licencia del antivirus Segurmática: le damos la oportunidad de adquirir licencias para el uso del antivirus Segurmática para computadoras y dispositivos móviles. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
