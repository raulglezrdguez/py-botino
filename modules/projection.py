# random
from random import randrange
import re

import globals

# manejo el estado proyeccion de audiovisuales


def projection(text, lang='es'):

    last_messages = ['Disfrute de audiovisuales en nuestras instalaciones',
                     'Vea cinematográficos en nuestras instalaciones', 'Disfrute de documentales en nuestras instalaciones']

    p = re.compile(r'\b(proyec(?:ci[ó|o]n(?:es)?|tar)|presenta(?:r|ci[o|ó]n(?:es)?)?|expo(?:er|sici[o|ó]n(?:es)?))\b[\s*\w*]*(audiovisual(?:es)?|pel[i|í]culas?|v[í|i]deos?|documental(?:es)?|filmes?|cinematogr[á|a]ficos?)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('machine_time')

        result_message = "Servicio de proyección de audiovisuales: usted puede disfrutar de proyecciones audiovisuales tanto de interés personal como profesional. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
