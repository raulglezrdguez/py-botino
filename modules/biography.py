# random
from random import randrange
import re
import sqlite3

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

# manejo el estado de busqueda en los martires
# · el mensaje es de la forma:
# biografia del martir revolucionario "nombre del martir"


def biography(text, lang='es'):

    last_messages = ['Para saber más, visite',
                     'Si desea conocer más, visite', 'Busque más información visitando']

    p = re.compile(
        r'\b(biograf[íi]as?|historias?|trayectorias?|vidas?)\s+(?:del?\s+)?(?:combatientes?\s+)?(?:m[aá]rtir\s+(?:revolucionario\s+)?)?(?:revolucionario\s+(?:m[áa]rtir\s+)?)?(?P<martir>[\s*\w*]*)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        # print(text)
        martir = m.group('martir').strip()
        if martir and martir != '':
            martir_find = re.sub(r'[aeiou]', '_', martir)
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
                    result_message = "Encontré {} biografias: ".format(count)
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
                    result_message = "No encuentro la biografía de {}".format(
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
                            "placeholder": "Introduzca el nombre del mártir a buscar", "required": "true"},
                    ]}
                ]

                return result_message, bd
            else:
                to_translate = [result_message,
                                "Introduzca el nombre del mártir a buscar"
                                ]
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
                            "placeholder": translations[1].text, "required": "true"},
                    ]}
                ]

                return result_message, bd

        else:
            result_message = "Por favor, dígame el nombre del personaje histórico para buscarle la biografía"

            if lang == 'es':
                return result_message, None
            else:
                translation = globals.translate_text(
                    result_message, dest=lang, src='es')
                return translation, None
    else:
        return None, None
