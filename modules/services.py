# random
from random import randrange
import re

import globals

# manejo el estado servicios


def services(text, lang='es'):

    first_messages = ['Los tipos de servicios que brinda Joven Club son', 'Joven Club brinda los siguientes tipos de servicios',
                      'Los tipos de servicios que brindamos son', 'Los servicios que brindamos desde Joven Club son']
    last_messages = ['Dígame cuál le interesa', 'Cuál de ellos le interesa',
                     'De qué servicio necesita saber', 'Cuál de éstos servicios necesita']

    p = re.compile(
        r'\b(servicios?|s[i|í]|ok|correcto|de +acuerdo)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('course')

        result_message = "{}: servicios de capacitación y actividades, servicios en Joven Club, servicios desde la red, servicios de segurmática antivirus y servicios de nuestros profesionales. {}".\
            format(first_messages[randrange(len(first_messages))],
                   last_messages[randrange(len(last_messages))])

        if lang == 'es':
            body = [
                {"tag": "p", "className": "inner-text",
                    "innerText": "{}:".format(first_messages[randrange(len(first_messages))])},
                {"tag": "answer", "label": "Servicios de Instrucción",
                    "text": "Instrucción"},
                {"tag": "answer", "label": "Servicios de Actividades",
                    "text": "Actividades"},
                {"tag": "answer", "label": "Dentro de Joven Club",
                    "text": "En Joven Club"},
                {"tag": "answer", "label": "En nuestra red", "text": "En la red"},
                {"tag": "answer", "label": "Servicios de segurmática antivirus",
                    "text": "Segurmática antivirus"},
                {"tag": "answer", "label": "Servicios de nuestros Profesionales",
                    "text": "Servicios profesionales"},
                {"tag": "p", "className": "inner-text",
                    "innerText": "{}".format(last_messages[randrange(len(last_messages))])}
            ]

            return result_message, body
        else:
            to_translate = [result_message,
                            "{}:".format(
                                first_messages[randrange(len(first_messages))]),
                            "Servicios de Instrucción",
                            "Servicios de Actividades",
                            "Dentro de Joven Club",
                            "En nuestra red",
                            "Servicios de segurmática antivirus",
                            "Servicios de nuestros Profesionales",
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
                {"tag": "p", "className": "inner-text",
                    "innerText": translations[8].text}
            ]

            return result_message, body
    else:
        return None, None
