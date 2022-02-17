# random
from random import randrange
import re

import globals

# manejo el estado desde la red


def red(text, lang='es'):
    patterns = [
        {'name': 'p1', 'pattern': [
            {'LOWER': {'IN': ['web', 'red', 'intranet']}}]},
    ]
    first_messages = ['Los servicios en la web que brinda Joven Club son', 'Joven Club brinda los siguientes servicios en la red',
                      'Los servicios en la intranet que brindamos son', 'Los servicios que brindamos desde la web son']
    last_messages = ['Dígame cuál le interesa', 'Cuál de ellos le interesa',
                     'De qué servicio necesita saber', 'Cuál de éstos servicios necesita']

    p = re.compile(r'\bweb\b|\bred\b|\bintranet\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('mochila')

        result_message = "{}: mochila, tendedera, reflejos, estanquillo, ecured, revista tino, ludox y el visor. {}".\
            format(first_messages[randrange(len(first_messages))],
                   last_messages[randrange(len(last_messages))])

        if lang == 'es':
            body = [
                {"tag": "p", "className": "inner-text",
                    "innerText": "{}".format(first_messages[randrange(len(first_messages))])},
                {"tag": "answer", "label": "La Mochila", "text": "Mochila"},
                {"tag": "answer", "label": "La Tendedera", "text": "Tendedera"},
                {"tag": "answer", "label": "Blog Reflejos", "text": "Reflejos"},
                {"tag": "answer", "label": "El Estanquillo", "text": "Estanquillo"},
                {"tag": "answer", "label": "Ecured", "text": "Ecured"},
                {"tag": "answer", "label": "Revista Tino", "text": "Revista Tino"},
                {"tag": "answer", "label": "Ludox", "text": "Ludox"},
                {"tag": "answer", "label": "El Visor", "text": "Visor"},
                {"tag": "p", "className": "inner-text",
                    "innerText": "{}".format(last_messages[randrange(len(last_messages))])}
            ]

            return result_message, body
        else:
            to_translate = [result_message,
                            "{}".format(
                                first_messages[randrange(len(first_messages))]),
                            "La Mochila",
                            "La Tendedera",
                            "Blog Reflejos",
                            "El Estanquillo",
                            "Ecured",
                            "Revista Tino",
                            "Ludox",
                            "El Visor",
                            "{}".format(
                                last_messages[randrange(len(last_messages))])
                            ]
            translations = globals.translate_array(
                to_translate, dest=lang, src='es')

            result_message = translations[0].text
            body = [
                {"tag": "p", "className": "inner-text",
                    "innerText": translations[1].text},
                {"tag": "answer",
                    "label": translations[2].text, "text": translations[2].text},
                {"tag": "answer",
                    "label": translations[3].text, "text": translations[3].text},
                {"tag": "answer",
                    "label": translations[4].text, "text": translations[4].text},
                {"tag": "answer",
                    "label": translations[5].text, "text": translations[5].text},
                {"tag": "answer",
                    "label": translations[6].text, "text": translations[6].text},
                {"tag": "answer",
                    "label": translations[7].text, "text": translations[7].text},
                {"tag": "answer",
                    "label": translations[8].text, "text": translations[8].text},
                {"tag": "answer",
                    "label": translations[9].text, "text": translations[9].text},
                {"tag": "p", "className": "inner-text",
                    "innerText": translations[10].text}
            ]

            return result_message, body

    else:
        return None, None
