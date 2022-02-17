# devuelve los articulos de la revista tino  que se obtengan de la busqueda por titulo o autor
# la base de datos es sqlite: en ./dbs/revista_tino.db
import sqlite3
import re

# random
from random import randrange

import json

import globals


def change_letter(letter):
    switcher = {
        'a': '[a|á]',
        'e': '[e|é]',
        'i': '[i|í]',
        'o': '[o|ó]',
        'u': '[u|ú]',
        'á': '[a|á]',
        'é': '[e|é]',
        'í': '[i|í]',
        'ó': '[o|ó]',
        'ú': '[u|ú]',
        'n': '[n|ñ]',
        'ñ': '[n|ñ]',
    }
    return switcher.get(letter, letter)


def change_word(word):
    result = ''
    for c in word:
        result = result + change_letter(c)
    return result

# manejo el estado biography_body


def biography_body(body, lang='es'):

    if (len(body) == 2):
        identifier = json.loads(body[0].replace("'", '"'))
        if (identifier["id"] == "biography" and identifier["value"] == "biography"):
            last_messages = ['Para saber más, visite',
                             'Si desea conocer más, visite', 'Busque más información visitando']
            martir = json.loads(body[1].replace("'", '"'))["value"].strip()

            if martir and martir != '':

                martir_find = re.sub(r'[áéíóúñÑÁÉÍÓÚaeiou]', '_', martir)
                # print(martir)
                # result = ''
                # create connection
                conn = sqlite3.connect('./dbs/martires.db')
                # create cursor
                c = conn.cursor()
                select = "SELECT * FROM martires WHERE name like '%{}%' order by name".format(
                    martir_find)
                rows = c.execute(select)
                fields = rows.fetchall()
                count = len(fields)
                if count > 1:
                    pattern = change_word(martir)
                    p1 = re.compile(rf"\b{pattern}\b", re.IGNORECASE)
                    result_array = []
                    result_bio = ''
                    for f in fields:
                        m1 = p1.search(f[0])
                        if m1:
                            result_array.append(f[0])
                            result_bio = f[1]
                            if len(f[0]) == len(martir):
                                break

                    count = len(result_array)

                    if count > 1:
                        result_message = "Encontré {} biografias: ".format(
                            count)
                        for f in result_array:
                            result_message = result_message + f + ', '
                        if len(result_message) > 2000:
                            result_message = result_message[:2000]
                        result_message = result_message + ' seleccione una por favor'
                    elif count == 1:
                        if len(result_bio) > 2000:
                            result_message = "{}: {} ... {} www.ecured.cu".format(
                                result_array[0], result_bio[:2000], last_messages[randrange(len(last_messages))])
                        else:
                            result_message = "{}: {} {} www.ecured.cu".format(
                                result_array[0], result_bio, last_messages[randrange(len(last_messages))])
                    else:
                        result_message = "No encuentro biografías con el nombre: {}".format(
                            martir)

                elif count == 1:
                    bio = fields[0][1]
                    if len(bio) > 2000:
                        result_message = "{}: {} ... {} www.ecured.cu".format(
                            fields[0][0], bio[:2000], last_messages[randrange(len(last_messages))])
                    else:
                        result_message = "{}: {} {} www.ecured.cu".format(
                            fields[0][0], bio, last_messages[randrange(len(last_messages))])
                else:
                    result_message = "No encuentro la biografía de {}".format(
                        martir)

                if lang == 'es':
                    bd = [
                        {"tag": "p", "className": "inner-text",
                            "innerText": result_message},
                        {"tag": "form", "body": [
                            {"tag": "input", "type": "hidden",
                                "id": "biography", "value": "biography"},
                            {"tag": "input", "type": "text", "id": "martir",
                                "placeholder": "Introduzca el nombre del mártir a buscar"},
                        ]}
                    ]

                    return result_message, bd
                else:
                    to_translate = [result_message,
                                    "Introduzca el nombre del mártir a buscar"]
                    translations = globals.translate_array(
                        to_translate, dest=lang, src='es')

                    result_message = translations[0].text
                    bd = [
                        {"tag": "p", "className": "inner-text",
                            "innerText": result_message},
                        {"tag": "form", "body": [
                            {"tag": "input", "type": "hidden",
                                "id": "biography", "value": "biography"},
                            {"tag": "input", "type": "text", "id": "martir",
                                "placeholder": translations[1].text},
                        ]}
                    ]

                    return result_message, bd
            else:
                result_message = "Nombre incorrecto, por favor introduzca correctamente el nombre"

                if lang == 'es':
                    bd = [
                        {"tag": "p", "className": "inner-text",
                            "innerText": result_message},
                        {"tag": "form", "body": [
                            {"tag": "input", "type": "hidden",
                                "id": "biography", "value": "biography"},
                            {"tag": "input", "type": "text", "id": "martir",
                                "placeholder": "Introduzca el nombre del mártir a buscar"},
                        ]}
                    ]

                    return result_message, bd
                else:
                    to_translate = [result_message,
                                    "Introduzca el nombre del mártir a buscar"]
                    translations = globals.translate_array(
                        to_translate, dest=lang, src='es')

                    result_message = translations[0].text
                    bd = [
                        {"tag": "p", "className": "inner-text",
                            "innerText": result_message},
                        {"tag": "form", "body": [
                            {"tag": "input", "type": "hidden",
                                "id": "biography", "value": "biography"},
                            {"tag": "input", "type": "text", "id": "martir",
                                "placeholder": translations[1].text},
                        ]}
                    ]

                    return result_message, bd
        else:
            return None, None
    else:
        return None, None
