# random
from random import randrange
import re

import globals

# manejo el estado coronavirus
# forma y estructura


def cv_form(text, lang='es'):
    last_messages = ['Protéjase', 'Cuídese y cuide a su familia', 'Tome todas las medidas necesarias', 'No salga de casa',
                     'Manténgase alejado del contacto social', 'Cumpla las orientaciones de la dirección del país', 'Use nasobuco']

    p = re.compile(
        r'\b(?:formas?|estructuras?|conformaci[oó]n(?:es?)?|configuraci[oó]n(?:es?)?|siluetas?|organizaci[oó]n(?:es?)?)[\s*\w*]*(corona *virus?|covid)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        # globals.current_state = globals.find_handler_index('cv_form')
        result_message = "Los coronavirus tienen una envoltura que encierra el genoma de ARN, y los viriones (los virus completos) son redondos u ovalados, a menudo polimórficos, con un diámetro de 50 a 200 nm. El nuevo coronavirus tiene un diámetro de 60 a 140 nm. La proteína espiga se encuentra en la superficie del virus y forma una estructura en forma de barra. Como una de las principales proteínas antigénicas del virus, la proteína espiga es la estructura principal utilizada para la tipificación. La proteína de la nucleocápside encapsula el genoma viral y puede usarse como antígeno de diagnóstico. {}".format(
            last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
