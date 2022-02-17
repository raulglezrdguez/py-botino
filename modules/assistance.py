# random
from random import randrange
import re

import globals

# manejo el estado asistencia técnica


def assistance(text, lang='es'):

    last_messages = ['Seleccione el servicio que desee',
                     'Cuál de estos servicios necesita', 'Dígame qué servicio necesita']

    p = re.compile(
        r'\b(asist(?:[e|a]n?|ir|encias?|ente)|ayuda(?:n|r|ntes?)?)\b[\s*\w*]*(t[e|é]cnic[a|o]s?)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('advisory')

        if lang == 'es':
            result_message = "Nuestros profesionales brindan su asistencia técnica en: asesoría e implementación, asistencia informática, instalación de aplicaciones y periféricos y elaboración de planes de seguridad informática. {}".\
                format(last_messages[randrange(len(last_messages))])
            body = [
                {"tag": "p", "className": "inner-text",
                    "innerText": "Nuestros profesionales brindan su asistencia técnica en:"},
                {"tag": "answer", "label": "Asesoría e implementación",
                    "text": "Asesoría"},
                {"tag": "answer", "label": "Asistencia informática",
                    "text": "Asistencia informática"},
                {"tag": "answer", "label": "Instalación de aplicaciones y periféricos",
                    "text": "Instalación de aplicaciones"},
                {"tag": "answer", "label": "Elaboración de planes de seguridad informática",
                    "text": "Planes de seguridad"},
                {"tag": "p", "className": "inner-text",
                    "innerText": "{}".format(last_messages[randrange(len(last_messages))])}
            ]

            return result_message, body
        else:
            to_translate = ["Nuestros profesionales brindan su asistencia técnica en: asesoría e implementación, asistencia informática, instalación de aplicaciones y periféricos y elaboración de planes de seguridad informática. {}".
                            format(
                                last_messages[randrange(len(last_messages))]),
                            "Nuestros profesionales brindan su asistencia técnica en:",
                            "Asesoría e implementación",
                            "Asistencia informática",
                            "Instalación de aplicaciones y periféricos",
                            "Elaboración de planes de seguridad informática",
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
                {"tag": "p", "className": "inner-text",
                    "innerText": translations[6].text}
            ]

            return result_message, body
    else:
        return None, None
