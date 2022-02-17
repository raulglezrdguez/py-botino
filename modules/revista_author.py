# random
from random import randrange
import re
import sqlite3

import globals

# manejo el estado de busqueda en la revista tino por autor
# · el mensaje es de la forma:
# revista ... autor "a buscar"


def revista_author(text, lang='es'):

    last_messages = ['Aprenda con nuestra revista Tino',
                     'Participe con publicaciones en nuestra revista', 'Colabore con nuestra revista Tino']

    p = re.compile(
        r'\b(revistas?|tino)\b[\s*\w*]*(autor(?:es)?)\b:*\s+:*(?P<author>[\s*\w*]*)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('mochila')
        author = m.group('author').strip()
        if author:
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
                to_translate = [result_message, "Introduzca el título a buscar",
                                "Introduzca el nombre del autor a buscar"]
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
            result_message = "Nombre del Autor incorrecto, por favor introduzca correctamente el nombre del autor"

            if lang == 'es':
                return result_message, None
            else:
                translation = globals.translate_text(
                    result_message, dest=lang, src='es')
                return translation, None
    else:
        return None, None
