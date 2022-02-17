# random
from random import randrange
import re

import globals

# manejo el estado trabajo con documentos, archivos, multimedias


def documents(text, lang='es'):

    last_messages = ['Seleccione el servicio que desee',
                     'Cuál de estos servicios necesita', 'Dígame qué servicio necesita']

    p = re.compile(
        r'\b(documentos?|archivos?|multimedias?|ficheros?)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('decontamination')

        if lang == 'es':
            result_message = "Los servicios de nuestros profesionales para ayudarle con sus documentos y multimedias son: descontaminación de dispositivos, recuperación de información, digitalización y restauración de imágenes y documentos y postproducción de audiovisuales. {}".\
                format(last_messages[randrange(len(last_messages))])
            body = [
                {"tag": "p", "className": "inner-text",
                    "innerText": "Los servicios de nuestros profesionales para ayudarle con sus documentos y multimedias son:"},
                {"tag": "answer", "label": "Descontaminación de dispositivos",
                    "text": "Descontaminación"},
                {"tag": "answer", "label": "Recuperación de información",
                    "text": "Recuperación"},
                {"tag": "answer", "label": "Digitalización de imágenes y documentos",
                    "text": "Digitalización"},
                {"tag": "answer", "label": "Restauración de imágenes y documentos",
                    "text": "Restauración"},
                {"tag": "answer", "label": "Postproducción de audiovisuales",
                    "text": "Postproducción"},
                {"tag": "p", "className": "inner-text",
                    "innerText": "{}".format(last_messages[randrange(len(last_messages))])}
            ]

            return result_message, body
        else:
            to_translate = ["Los servicios de nuestros profesionales para ayudarle con sus documentos y multimedias son: descontaminación de dispositivos, recuperación de información, digitalización y restauración de imágenes y documentos y postproducción de audiovisuales. {}".
                            format(
                                last_messages[randrange(len(last_messages))]),
                            "Los servicios de nuestros profesionales para ayudarle con sus documentos y multimedias son:",
                            "Descontaminación de dispositivos",
                            "Recuperación de información",
                            "Digitalización de imágenes y documentos",
                            "Restauración de imágenes y documentos",
                            "Postproducción de audiovisuales",
                            "{}".format(last_messages[randrange(len(last_messages))])]
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
                {"tag": "p", "className": "inner-text",
                    "innerText": translations[7].text}
            ]

            return result_message, body

    else:
        return None, None
