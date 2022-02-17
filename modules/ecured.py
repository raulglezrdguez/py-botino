# random
from random import randrange
import re

import globals

# manejo el estado ecured


def ecured(text, lang='es'):

    last_messages = ['Aprenda con nuestra enciclopedia',
                     'Participe con nosotros en la enciclopedia Ecured', 'Colabore con nuestra enciclopedia']

    p = re.compile(
        r'\becured\b|\benciclopedias?\b|\bcolabora(?:r|ci[o|ó]n(?:es)?|tiv[o|a]s?)?\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('mochila')

        result_message = "Servicio de Ecured: ponemos a su disposición la enciclopedia colaborativa en la red cubana, en la que puede colaborar y utilizar todo el material creado. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
