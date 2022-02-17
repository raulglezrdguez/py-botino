# random
from random import randrange
import re

import globals

# manejo el estado instrucción


def training(text, lang='es'):

    first_messages = ['Los tipos de servicios de capacitación que brindamos son',
                      'Brindamos los siguientes servicios de instrucción', 'Los servicios de instrucción que brindamos son']
    last_messages = ['Dígame cuál le interesa', 'Cuál de ellos le interesa',
                     'De qué servicio necesita saber', 'Cuál de éstos servicios necesita']

    p = re.compile(
        r'\b(instruir|instrucci[o|ó]n|formaci[o|ó]n|formar|entrena(?:r|miento)|adiestra(?:r|miento)|preparar|preparaci[o|ó]n|educar|educaci[o|ó]n|enseñan[z|s]a|enseñar)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('course')

        if lang == 'es':
            result_message = "{}: cursos, exámenes de suficiencia, círculos de interés y atención a niños talentos. {}".\
                format(first_messages[randrange(len(first_messages))],
                       last_messages[randrange(len(last_messages))])
            body = [
                {"tag": "p", "className": "inner-text",
                    "innerText": "{}".format(first_messages[randrange(len(first_messages))])},
                {"tag": "answer", "label": "Cursos", "text": "Cursos"},
                {"tag": "answer", "label": "Exámenes de suficiencia",
                    "text": "Suficiencia"},
                {"tag": "answer", "label": "Círculos de interés",
                    "text": "Círculos de interés"},
                {"tag": "answer", "label": "Atención a niños talentos",
                    "text": "Niños talentos"},
                {"tag": "p", "className": "inner-text",
                    "innerText": "{}".format(last_messages[randrange(len(last_messages))])}
            ]

            return result_message, body
        else:
            to_translate = ["{}: cursos, exámenes de suficiencia, círculos de interés y atención a niños talentos. {}".
                            format(first_messages[randrange(len(first_messages))],
                                   last_messages[randrange(len(last_messages))]),
                            "{}".format(
                                first_messages[randrange(len(first_messages))]),
                            "Cursos",
                            "Exámenes de suficiencia",
                            "Círculos de interés",
                            "Atención a niños talentos",
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
                {"tag": "p", "className": "inner-text",
                    "innerText": translations[6].text}
            ]

            return result_message, body

    else:
        return None, None
