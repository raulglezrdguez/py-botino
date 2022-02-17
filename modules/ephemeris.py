# random
from random import randrange
import re

import globals

# manejo el estado ephemeris


def ephemeris(text, lang='es'):

    last_messages = ['Para conocer sobre las efemérides me debes decir el día y el mes', 'Si quieres conocer las efemérides dime el día y el mes',
                     'Dime el día y el mes del que quieres conocer las efemérides', 'Si me dices el día y el mes le doy las efemérides', 'Le puedo dar las efemérides del día y el mes que me diga']

    p = re.compile(r'\b(efem[eé]rides?)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('events')
        result_message = "{}".format(
            last_messages[randrange(len(last_messages))])

        if lang == 'es':
            body = [
                {"tag": "p", "className": "inner-text",
                    "innerText": result_message},
                {"tag": "form", "body": [
                    {"tag": "input", "type": "hidden",
                        "id": "ephemeris", "value": "ephemeris"},
                    {"tag": "input", "type": "number", "id": "day",
                        "placeholder": "Introduzca el día", "required": "true"},
                    {"tag": "select", "id": "month", "body": [
                        {"tag": "option", "value": "enero", "innerText": "Enero"},
                        {"tag": "option", "value": "febrero",
                            "innerText": "Febrero"},
                        {"tag": "option", "value": "marzo", "innerText": "Marzo"},
                        {"tag": "option", "value": "abril", "innerText": "Abril"},
                        {"tag": "option", "value": "mayo", "innerText": "Mayo"},
                        {"tag": "option", "value": "junio", "innerText": "Junio"},
                        {"tag": "option", "value": "julio", "innerText": "Julio"},
                        {"tag": "option", "value": "agosto", "innerText": "Agosto"},
                        {"tag": "option", "value": "septiembre",
                            "innerText": "Septiembre"},
                        {"tag": "option", "value": "octubre",
                            "innerText": "Octubre"},
                        {"tag": "option", "value": "noviembre",
                            "innerText": "Noviembre"},
                        {"tag": "option", "value": "diciembre",
                            "innerText": "Diciembre"},
                    ]}
                ]}
            ]

            return result_message, body
        else:
            to_translate = [result_message,
                            "Introduzca el día",
                            "enero",
                            "febrero",
                            "marzo",
                            "abril",
                            "mayo",
                            "junio",
                            "julio",
                            "agosto",
                            "septiembre",
                            "octubre",
                            "noviembre",
                            "diciembre",
                            ]
            translations = globals.translate_array(
                to_translate, dest=lang, src='es')

            result_message = translations[0].text
            body = [
                {"tag": "p", "className": "inner-text",
                    "innerText": result_message},
                {"tag": "form", "body": [
                    {"tag": "input", "type": "hidden",
                        "id": "ephemeris", "value": "ephemeris"},
                    {"tag": "input", "type": "number", "id": "day",
                        "placeholder": translations[1].text, "required": "true"},
                    {"tag": "select", "id": "month", "body": [
                        {"tag": "option",
                            "value": translations[2].text, "innerText": translations[2].text},
                        {"tag": "option",
                            "value": translations[3].text, "innerText": translations[3].text},
                        {"tag": "option",
                            "value": translations[4].text, "innerText": translations[4].text},
                        {"tag": "option",
                            "value": translations[5].text, "innerText": translations[5].text},
                        {"tag": "option",
                            "value": translations[6].text, "innerText": translations[6].text},
                        {"tag": "option",
                            "value": translations[7].text, "innerText": translations[7].text},
                        {"tag": "option",
                            "value": translations[8].text, "innerText": translations[8].text},
                        {"tag": "option",
                            "value": translations[9].text, "innerText": translations[9].text},
                        {"tag": "option",
                            "value": translations[10].text, "innerText": translations[10].text},
                        {"tag": "option",
                            "value": translations[11].text, "innerText": translations[11].text},
                        {"tag": "option",
                            "value": translations[12].text, "innerText": translations[12].text},
                        {"tag": "option",
                            "value": translations[13].text, "innerText": translations[13].text},
                    ]}
                ]}
            ]

            return result_message, body

    else:
        return None, None
