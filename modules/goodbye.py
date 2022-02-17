# random
from random import randrange
import re

import globals

# manejo el estado adios


def goodbye(text, lang='es'):
    first_messages = ['Chao', 'Adiós', 'Cuídate', 'Nos vemos', 'Hasta pronto', 'Hasta luego', 'Hasta la próxima',
                      'Hasta la vista', 'Que tenga buenos días', 'Te veo luego', 'Te veo pronto', 'Que le vaya bien']
    middle_messages = ['espero le haya servido mi ayuda', 'espero le haya podido ayudar',
                       'estoy aquí para servirle', 'si me necesita le estaré esperando']
    last_messages = ['visítenos para recibir nuestros servicios',
                     'visite nuestras instalaciones y aprenda con nosotros', 'visite Joven Club para recibir nuestros servicios']

    p = re.compile(r'\b(chao|adi[oó]s|termina(?:r|mos?)|cerrar|cu[ií]date|gracias?|nos\s+vemos?|hasta\s+(?:luego|ma[ñn]ana|pronto|nunca)|hasta\s+la\s+(?:pr[óo]xima|vista)|tengas?\b[\s*\w*]*\bbuen(?:os?)?\s+d[ií]as?|(?:te|le|lo)\s+veo\s+(?:luego|despu[eé]s|ma[nñ]ana)|(?:le|te)\s+vaya\s+(?:bien|mal))\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('course')

        result_message = "{}, {}, {}".format(first_messages[randrange(len(first_messages))], middle_messages[randrange(
            len(middle_messages))], last_messages[randrange(len(last_messages))])

        if lang == 'es':
            body = [
                {"tag": "p", "className": "inner-text",
                    "innerText": result_message},
                {"tag": "img", "src": "hand_shake.png"}
            ]
            return result_message, body
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            body = [
                {"tag": "p", "className": "inner-text", "innerText": translation},
                {"tag": "img", "src": "hand_shake.png"}
            ]
            return translation, body
    else:
        return None, None
