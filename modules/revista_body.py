# devuelve los articulos de la revista tino  que se obtengan de la busqueda por titulo o autor
# la base de datos es sqlite: en ./dbs/revista_tino.db
import sqlite3

# random
from random import randrange

import json

import globals

# manejo el estado revista_body


def revista_body(body, lang='es'):

    if (len(body) == 3):
        identifier = json.loads(body[0].replace("'", '"'))
        if (identifier["id"] == "magazine" and identifier["value"] == "magazine"):
            last_messages = ['Aprenda con nuestra revista Tino',
                             'Participe con publicaciones en nuestra revista', 'Colabore con nuestra revista Tino']
            title = json.loads(body[1].replace("'", '"'))["value"].strip()
            author = json.loads(body[2].replace("'", '"'))["value"].strip()

            if title != '':

                if lang != 'es':
                    translation = globals.translate_text(
                        title, dest='es', src=lang)
                    title = translation
                # buscar por titulo
                result = ''
                # create connection
                conn = sqlite3.connect('./dbs/revista_tino.db')
                # create cursor
                c = conn.cursor()
                select = "SELECT * FROM articles WHERE title like '%{}%' order by number DESC limit 5".format(
                    title)
                # print(select)
                rows = c.execute(select)
                for row in rows:
                    number = ('. Revista ' + str(row[0])) if row[0] else ''
                    tit = ('. Artículo: ' + row[1]) if row[1] else ''
                    section = ('. Sección ' + row[2]) if row[2] else ''
                    author = ('. Autor ' + row[3]) if row[3] else ''
                    description = ('. ' + row[5]) if row[5] != '' else ''
                    result = result + tit + number + section + author + description

                result_message = "Resultados de buscar en el título {} {} . {}. Para saber más visite: revista.jovenclub.cu".format(
                    title, result, last_messages[randrange(len(last_messages))])
                if result == '':
                    result_message = "No se han encontrado publicaciones con el título {}. Por favor busque otro título.".format(
                        title)

                if lang == 'es':

                    bd = [
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

                    return result_message, bd
                else:
                    to_translate = [result_message,
                                    "Introduzca el título a buscar",
                                    "Introduzca el nombre del autor a buscar"
                                    ]
                    translations = globals.translate_array(
                        to_translate, dest=lang, src='es')

                    result_message = translations.pop(0).text
                    bd = [
                        {"tag": "p", "className": "inner-text",
                            "innerText": result_message},
                        {"tag": "form", "body": [
                            {"tag": "input", "type": "hidden",
                                "id": "magazine", "value": "magazine"},
                            {"tag": "input", "type": "text", "id": "title",
                                "placeholder": translations.pop(0).text},
                            {"tag": "input", "type": "text", "id": "author",
                                "placeholder": translations.pop(0).text},
                        ]}
                    ]

                    return result_message, bd
            elif author != '':
                if lang != 'es':
                    translation = globals.translate_text(
                        author, dest='es', src=lang)
                    author = translation

                result = ''
                # create connection
                conn = sqlite3.connect('./dbs/revista_tino.db')
                # create cursor
                c = conn.cursor()
                select = "SELECT * FROM articles WHERE author like '%{}%' order by number DESC limit 5".format(
                    author)
                # print(select)
                rows = c.execute(select)
                for row in rows:
                    number = ('. Revista ' + str(row[0])) if row[0] else ''
                    tit = ('. Artículo: ' + row[1]) if row[1] else ''
                    section = ('. Sección ' + row[2]) if row[2] else ''
                    autor = ('. Autor ' + row[3]) if row[3] else ''
                    description = ('. ' + row[5]) if row[5] != '' else ''
                    result = result + tit + number + section + autor + description

                result_message = "Resultados de buscar al autor {} {} . {}. Para saber más visite: revista.jovenclub.cu".format(
                    author, result, last_messages[randrange(len(last_messages))])
                if result == '':
                    result_message = "No se han encontrado publicaciones con el autor {}. Por favor busque a otro autor.".format(
                        author)

                if lang == 'es':

                    bd = [
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

                    return result_message, bd
                else:
                    to_translate = [result_message,
                                    "Introduzca el título a buscar",
                                    "Introduzca el nombre del autor a buscar"
                                    ]
                    translations = globals.translate_array(
                        to_translate, dest=lang, src='es')

                    result_message = translations[0].text
                    bd = [
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

                    return result_message, bd
            else:
                result_message = "No ha introducido correctamente los valores para realizar las búsquedas, por favor introduzca un título o un autor para buscar en los artículos de la revista Tino."

                if lang == 'es':
                    bd = [
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

                    return result_message, bd
                else:
                    to_translate = [result_message,
                                    "Introduzca el título a buscar",
                                    "Introduzca el nombre del autor a buscar"
                                    ]
                    translations = globals.translate_array(
                        to_translate, dest=lang, src='es')

                    result_message = translations[0].text
                    bd = [
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

                    return result_message, bd
        else:
            return None, None
    else:
        return None, None
