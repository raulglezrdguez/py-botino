# random
from random import randrange
import re

import globals

# manejo el estado torneo de juegos en linea


def games(text, lang='es'):

    last_messages = ['Disfrute de videojuegos en nuestras instalaciones',
                     'Participe en campeonatos de juegos con nosotros', 'Disfrute de torneos de juegos en línea con nosotros']

    p = re.compile(
        r'\b(torneos?|juegos?|videojuegos?|campeonatos?|comp(?:et(?:ir|encias?)|it[a|e|o])|juega|jugar)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('machine_time')

        result_message = "Servicio de torneos de juegos en línea: le ofrecemos la oportunidad de competir contra otros jugadores o equipos conectados a la red de Joven Club. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
