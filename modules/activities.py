# random
from random import randrange
import re

import globals

# manejo el estado actividades


def activities(text, lang='es'):
    first_messages = ['Los tipos de servicios de actividades que brindamos son',
                      'Brindamos los siguientes servicios de actividades', 'Los servicios de actividades que brindamos son']
    last_messages = ['Dígame cuál le interesa', 'Cuál de ellos le interesa',
                     'De qué servicio necesita saber', 'Cuál de éstos servicios necesita']

    p = re.compile(r'\bactividad(?:es)?\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('disability')

        if lang == 'es':

            result_message = "{}: actividades para personas con discapacidad y actividades para Geroclub. {}".\
                format(first_messages[randrange(len(first_messages))],
                       last_messages[randrange(len(last_messages))])
            body = [
                {"tag": "p", "className": "inner-text",
                    "innerText": "{}".format(first_messages[randrange(len(first_messages))])},
                {"tag": "answer", "label": "Actividades para personas con discapacidad",
                    "text": "personas con discapacidad"},
                {"tag": "answer", "label": "Actividades para Geroclub",
                    "text": "Geroclub"},
                {"tag": "p", "className": "inner-text",
                    "innerText": "{}".format(last_messages[randrange(len(last_messages))])}
            ]

            return result_message, body
        else:
            to_translate = ["{}: actividades para personas con discapacidad y actividades para Geroclub. {}".
                            format(first_messages[randrange(len(first_messages))],
                                   last_messages[randrange(len(last_messages))]),
                            "{}".format(
                                first_messages[randrange(len(first_messages))]),
                            "Actividades para personas con discapacidad", "personas con discapacidad",
                            "Actividades para Geroclub",
                            "{}".format(
                                last_messages[randrange(len(last_messages))])
                            ]
            translations = globals.translate_array(
                to_translate, dest=lang, src='es')

            result_message = translations[0].text
            body = [
                {"tag": "p", "className": "inner-text",
                    "innerText": translations[1].text},
                {"tag": "answer", "label": translations[2].text,
                    "text": translations[3].text},
                {"tag": "answer",
                    "label": translations[4].text, "text": "Geroclub"},
                {"tag": "p", "className": "inner-text",
                    "innerText": translations[5].text}
            ]

            return result_message, body

    else:
        return None, None
