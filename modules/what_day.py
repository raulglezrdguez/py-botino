# devuelve el dia de hoy
import datetime
import re

# random
from random import randrange

import globals

# manejo el estado what_day


def what_day(text, lang='es'):
    months = {1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio",
              7: "julio", 8: "agosto", 9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"}
    week_day = {0: "lunes", 1: "martes", 2: "miércoles",
                3: "jueves", 4: "viernes", 5: "sábado", 6: "domingo"}

    first_messages = ['En mi calendario hoy es',
                      'En mi calendario tengo que hoy es', 'Mi calendario tiene que hoy es']

    p = re.compile(
        r'\b(qu[ée]\s*d[íi]as?\s*es(?:tamos?)?)\b|\b(a\s*cu[áa]nto\s*estamos?)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = 0
        today = datetime.datetime.today()

        result_message = "{}: {} {} de {} de {}".format(first_messages[randrange(len(
            first_messages))], week_day.get(today.weekday()), today.day, months.get(today.month), today.year)

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
