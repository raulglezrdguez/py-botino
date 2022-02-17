# random
from random import randrange
import re

import globals

# manejo el estado revista tino


def revista(text, lang='es'):

    last_messages = ['Aprenda con nuestra revista Tino',
                     'Participe con publicaciones en nuestra revista', 'Colabore con nuestra revista Tino']

    p = re.compile(r'\brevistas?\b|\btino\b|\bpublicar\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('mochila')

        result_message = "Servicio de la Revista Tino: puede revisar y publicar sus artículos en nuestra revista con ISSN, en temas de la informática y la electrónica. Si lo desea puedo buscarle artículos por título o autor. {}. Para saber más visite: revista.jovenclub.cu".format(
            last_messages[randrange(len(last_messages))])

        if lang == 'es':
            body = [
                {"tag": "p", "className": "inner-text",
                    "innerText": result_message},
                {"tag": "form", "body": [
                    {"tag": "input", "type": "hidden",
                        "id": "magazine", "value": "magazine"},
                    {"tag": "input", "type": "text", "id": "title",
                        "placeholder": "Introduzca el título a buscar"},
                    {"tag": "input", "type": "text", "id": "author",
                        "placeholder": "Introduzca el nombre del autor a buscar"},
                ]}
            ]

            return result_message, body
        else:
            to_translate = [result_message, "Introduzca el título a buscar",
                            "Introduzca el nombre del autor a buscar"]
            translations = globals.translate_array(
                to_translate, dest=lang, src='es')

            result_message = translations[0].text
            body = [
                {"tag": "p", "className": "inner-text",
                    "innerText": result_message},
                {"tag": "form", "body": [
                    {"tag": "input", "type": "hidden",
                        "id": "magazine", "value": "magazine"},
                    {"tag": "input", "type": "text", "id": "title",
                        "placeholder": translations[1].text},
                    {"tag": "input", "type": "text", "id": "author",
                        "placeholder": translations[2].text},
                ]}
            ]

            return result_message, body

    else:
        return None, None
