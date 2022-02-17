# random
from random import randrange
import re

import globals

# manejo el estado tendedera


def tendedera(text, lang='es'):

    last_messages = ['Comparta contenidos con sus amigos',
                     'Utilice nuestra red social', 'Contacte con sus amigos']

    p = re.compile(
        r'\b(?:tendeder[ao]s?)\b|(?:red(?:es)?\b[\s*\w*]*\bsocial(?:es)?)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('mochila')

        result_message = "Servicio de La Tendedera: le brindamos la posibilidad de compartir con amigos de cualquier parte del mundo a través de nuestra red social la tendedera. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
