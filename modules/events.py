# devuelve las efemerides del dia y el mes que le pasen como parametro
# la base de datos es sqlite: en ./dbs/efemerides.db
import sqlite3
import datetime
import re

# random
from random import randrange

import globals

# manejo el estado events


def events(text, lang='es'):
    month_names = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
                   'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

    months = {1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio",
              7: "julio", 8: "agosto", 9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"}
    last_day = {"enero": 31, "febrero": 29, "marzo": 31, "abril": 30, "mayo": 31, "junio": 30,
                "julio": 31, "agosto": 31, "septiembre": 30, "octubre": 31, "noviembre": 30, "diciembre": 31}

    first_messages = ['Los sucesos del', 'Las efemérides del',
                      'Los acontecimientos del', 'Los eventos del ']
    last_messages = ['Visite efemerides.cuba.cu para saber más', 'Si desea saber más visite efemerides.cuba.cu',
                     'Para saber más visite efemerides.cuba.cu', 'Visite efemerides.cuba.cu si desea saber más']

    p = re.compile(
        r'\b(?P<dia>\d{1,2})\b[\s*\w*]*\b(?P<mes>enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        day = m.group('dia')
        month = m.group('mes')
    else:
        p = re.compile(
            r'\b(?P<dia>primer[oa]*)\b[\s*\w*]*\b(?P<mes>enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)\b', re.IGNORECASE)
        m = p.search(text)

        if m:
            day = 1
            month = m.group('mes')
        else:
            p = re.compile(
                r'\b(?P<mes>enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)\b[\s*\w*]*\b(?P<dia>\d{1,2})\b', re.IGNORECASE)
            m = p.search(text)

            if m:
                day = m.group('dia')
                month = m.group('mes')
            else:
                p = re.compile(
                    r'\b(?P<mes>enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)\b[\s*\w*]*\b(?P<dia>primer[oa]*)\b', re.IGNORECASE)
                m = p.search(text)

                if m:
                    day = 1
                    month = m.group('mes')
                else:
                    p = re.compile(
                        r'\b(acontecimientos?|aconteci[oó]|sucesos?|sucedi[oó]|efem[eé]rides?|ocurri(?:o|ó|dos?|eron)|hechos?|eventos?)\b[\s*\w*]*\b(hoy|ahora)\b', re.IGNORECASE)
                    m = p.search(text)

                    if m:
                        today = datetime.date.today()
                        day = today.day
                        month = months.get(today.month)
                    else:
                        return None, None

    day_value = int(str(day))
    if day_value > 0 and day_value <= last_day.get(str(month)):
        # create connection
        conn = sqlite3.connect('./dbs/efemerides.db')
        # create cursor
        c = conn.cursor()
        e = ""
        select = "SELECT year, event FROM efemerides WHERE month='{}' AND day={}".format(
            month, day)
        rows = c.execute(select)
        for row in rows:
            e = e + " En " + str(row[0]) + ": " + row[1] + '.'

        # close connection
        conn.close()

        # globals.current_state = globals.find_handler_index('disability')
        result_message = "{} {} de {} son: {} {}".format(first_messages[randrange(len(
            first_messages))], day, month, e, last_messages[randrange(len(last_messages))])
        if (e == ""):
            result_message = "No tengo registradas las efémerides del {} de {}, por favor consulte otra fecha.".format(
                day, month)
    else:
        result_message = "La fecha {} de {}, no es correcta, por favor dígame una fecha correcta.".format(
            day, month)

    if lang == 'es':
        body = [
            {"tag": "p", "className": "inner-text", "innerText": result_message},
            {"tag": "form", "body": [
                {"tag": "input", "type": "hidden",
                    "id": "ephemeris", "value": "ephemeris"},
                {"tag": "input", "type": "number", "id": "day",
                    "placeholder": "Introduzca el día", "required": "true"},
                {"tag": "select", "id": "month", "body": [
                    {"tag": "option", "value": "enero", "innerText": "Enero"},
                    {"tag": "option", "value": "febrero", "innerText": "Febrero"},
                    {"tag": "option", "value": "marzo", "innerText": "Marzo"},
                    {"tag": "option", "value": "abril", "innerText": "Abril"},
                    {"tag": "option", "value": "mayo", "innerText": "Mayo"},
                    {"tag": "option", "value": "junio", "innerText": "Junio"},
                    {"tag": "option", "value": "julio", "innerText": "Julio"},
                    {"tag": "option", "value": "agosto", "innerText": "Agosto"},
                    {"tag": "option", "value": "septiembre",
                        "innerText": "Septiembre"},
                    {"tag": "option", "value": "octubre", "innerText": "Octubre"},
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
            {"tag": "p", "className": "inner-text", "innerText": result_message},
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
                            "value": translations[13].text, "innerText": translations[13].text}, ]}
            ]}
        ]

        return result_message, body
