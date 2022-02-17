# random
from random import randrange
import re
import json

import globals

# importo datetime
from datetime import datetime


def hello(text, lang='es'):
    # manejo el estado hola

    last_messages = ['soy su asistente personal para los servicios de Joven Club, las biografías y las efemérides, quiere conocer de nuestros servicios, las biografías y de las efemérides', 'le puedo ayudar con los servicios que brinda Joven Club, las biografías y las efemérides, quiere saber más sobre nuestros servicios, las biografías y las efemérides',
                     'si quiere aclarar sus dudas sobre los servicios que brinda Joven Club, las biografías y las efemérides, le puedo ayudar', 'conozco acerca de los servicios que brinda Joven Club, las biografías y las efemérides, le puedo dar más información']

    p = re.compile(
        r'\b(buenas?|saludos?|hola|buen(?:[oa]s?)?\b\s*(?:d[ií]as?|tardes?|noches?)|c[óo]mo\b\s*estas?|todo\b\s*bien|qu[eé]\b\s*(?:pasa|hay|tal))\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('course')
        hour = datetime.now().hour
        result = ''
        if (hour < 12):
            result = 'Buenos días'
        elif hour < 18:
            result = 'Buenas tardes'
        else:
            result = 'Buenas noches'

        if lang == 'es':
            result_message = "{}, {}".format(
                result, last_messages[randrange(len(last_messages))])
            body = [
                {"tag": "p", "className": "inner-text",
                    "innerText": result_message},
                {"tag": "answer", "label": "Si, quiero saber de los servicios",
                    "text": "servicios"},
                {"tag": "answer", "label": "Si, quiero saber de las biografías",
                    "text": "biografía de José Martí Pérez"},
                {"tag": "answer", "label": "Si, quiero saber de las efemérides",
                    "text": "efemérides"},
                {"tag": "answer", "label": "No, gracias", "text": "chao"},
                # {"tag": "form", "body": [
                #     {"tag": "input", "type": "hidden", "id": "hello", "value": "hello"},
                #     {"tag": "input", "type": "text", "id": "name", "placeholder": "introduzca el nombre"},
                #     {"tag": "input", "type": "text", "id": "lastname", "placeholder": "introduzca los apellidos", "required": "true"}
                # ]}
            ]

            return result_message, body
        else:
            to_translate = ["{}, {}".format(result, last_messages[randrange(len(
                last_messages))]),
                "Quiero saber de los servicios", "los servicios que brindan",
                "Quiero saber de las biografías", "biografía de José Martí Pérez",
                "Quiero saber de las efemérides", "las efemérides",
                "No, gracias", "chao"]
            translations = globals.translate_array(
                to_translate, dest=lang, src='es')

            result_message = translations[0].text
            body = [
                {"tag": "p", "className": "inner-text",
                 "innerText": result_message},
                {"tag": "answer", "label": translations[1].text,
                    "text": translations[2].text},
                {"tag": "answer", "label": translations[3].text,
                    "text": translations[4].text},
                {"tag": "answer", "label": translations[5].text,
                    "text": translations[6].text},
                {"tag": "answer",
                    "label": translations[7].text, "text": translations[8].text},
            ]

            return result_message, body
    else:
        return None, None
