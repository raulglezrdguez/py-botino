# random
from random import randrange
import re

import globals

# manejo el estado servicios profesionales


def professional(text, lang='es'):

    first_messages = ['Los servicios profesionales que brinda Joven Club son', 'Joven Club brinda los siguientes servicios profesionales',
                      'Los servicios profesionales que brindamos son', 'Los servicios profesionales que brindamos son']
    last_messages = ['Dígame cuál le interesa', 'Cuál de ellos le interesa',
                     'De qué servicio necesita saber', 'Cuál de éstos servicios necesita']

    p = re.compile(
        r'\bservicios?\b[\s*\w*]*\bprofesional(?:es)?\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('decontamination')

        if lang == 'es':
            result_message = "{}: trabajo con documentos y multimedias, asistencia técnica y desarrollo e implementación de aplicaciones informáticas. {}".\
                format(first_messages[randrange(len(first_messages))],
                       last_messages[randrange(len(last_messages))])
            body = [
                {"tag": "p", "className": "inner-text",
                    "innerText": "{}".format(first_messages[randrange(len(first_messages))])},
                {"tag": "answer", "label": "Trabajo con documentos y multimedias",
                    "text": "Documentos y multimedias"},
                {"tag": "answer", "label": "Asistencia técnica",
                    "text": "Asistencia técnica"},
                {"tag": "answer", "label": "Desarrollo e implementación de aplicaciones informáticas",
                    "text": "Desarrollo e implementación de soluciones"},
                {"tag": "p", "className": "inner-text",
                    "innerText": "{}".format(last_messages[randrange(len(last_messages))])}
            ]

            return result_message, body
        else:
            to_translate = ["{}: trabajo con documentos y multimedias, asistencia técnica y desarrollo e implementación de aplicaciones informáticas. {}".
                            format(first_messages[randrange(
                                len(first_messages))], last_messages[randrange(len(last_messages))]),
                            "{}".format(
                                first_messages[randrange(len(first_messages))]),
                            "Trabajo con documentos y multimedias",
                            "Asistencia técnica",
                            "Desarrollo e implementación de aplicaciones informáticas",
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
                {"tag": "p", "className": "inner-text",
                    "innerText": translations[5].text}
            ]

            return result_message, body
    else:
        return None, None
