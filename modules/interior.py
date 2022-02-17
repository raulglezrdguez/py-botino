# random
from random import randrange
import re

import globals

# manejo el estado servicios en nuestras instalaciones


def interior(text, lang='es'):

    first_messages = ['Los servicios que brindamos en Joven Club son',
                      'Brindamos los siguientes servicios en Joven Club', 'Los servicios en Joven Club que brindamos son']
    last_messages = ['Dígame cuál le interesa', 'Cuál de ellos le interesa',
                     'De qué servicio necesita saber', 'Cuál de éstos servicios necesita']

    p = re.compile(
        r'\b(en|a?dentro|nuestr[o|a]s)\b[\s*\w*]*\b(instalaci[o|ó]n(?:es)?|club(?:es)?|local(?:es)?|laboratorios?)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('machine_time')

        result_message = "{}: tiempo de máquina, alquiler de locales y dispositivos, proyección de audiovisuales, torneos de juego, navegación, correo e impresión de documentos. {}".\
            format(first_messages[randrange(len(first_messages))],
                   last_messages[randrange(len(last_messages))])

        if lang == 'es':
            body = [
                {"tag": "p", "className": "inner-text",
                    "innerText": "{}".format(first_messages[randrange(len(first_messages))])},
                {"tag": "answer", "label": "Tiempo de máquina",
                    "text": "Tiempo de máquina"},
                {"tag": "answer", "label": "Alquiler de locales",
                    "text": "Alquiler de locales"},
                {"tag": "answer", "label": "Alquiler de dispositivos",
                    "text": "Alquiler de dispositivos"},
                {"tag": "answer", "label": "Proyección de audiovisuales",
                    "text": "Proyección de audiovisuales"},
                {"tag": "answer", "label": "Torneo de juegos",
                    "text": "Torneo de juegos"},
                {"tag": "answer", "label": "Navegación y correo",
                    "text": "Navegación y correo"},
                {"tag": "answer", "label": "Impresión de documentos",
                    "text": "Impresión"},
                {"tag": "p", "className": "inner-text",
                    "innerText": "{}".format(last_messages[randrange(len(last_messages))])}
            ]

            return result_message, body
        else:
            to_translate = [result_message,
                            "{}".format(
                                first_messages[randrange(len(first_messages))]),
                            "Tiempo de máquina",
                            "Alquiler de locales",
                            "Alquiler de dispositivos",
                            "Proyección de audiovisuales",
                            "Torneo de juegos",
                            "Navegación y correo",
                            "Impresión de documentos",
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
                    "text": translations[2].text},
                {"tag": "answer", "label": translations[3].text,
                    "text": translations[3].text},
                {"tag": "answer", "label": translations[4].text,
                    "text": translations[4].text},
                {"tag": "answer", "label": translations[5].text,
                    "text": translations[5].text},
                {"tag": "answer", "label": translations[6].text,
                    "text": translations[6].text},
                {"tag": "answer", "label": translations[7].text,
                    "text": translations[7].text},
                {"tag": "answer", "label": translations[8].text,
                    "text": translations[8].text},
                {"tag": "p", "className": "inner-text",
                    "innerText": translations[9].text}
            ]

            return result_message, body
    else:
        return None, None
