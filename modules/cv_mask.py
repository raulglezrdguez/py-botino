# random
from random import randrange
import re

import globals

# manejo el estado coronavirus
# mascara


def cv_mask(text, lang='es'):
    last_messages = ['Protéjase', 'Cuídese y cuide a su familia', 'Tome todas las medidas necesarias', 'No salga de casa',
                     'Manténgase alejado del contacto social', 'Cumpla las orientaciones de la dirección del país', 'Use nasobuco']

    p = re.compile(
        r'\b(?:m[aá]scara|careta|antifaz|mascarilla|disfraz|nasobuco|barbijo|tapa *boca)[\s*\w*]*(corona *virus?|covid)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('cv_form')

        result_message = "Las máscaras son efectivas. Porque el propósito de usar la máscara es bloquear el portador por el cual se transmite el virus, en lugar de bloquear directamente los virus. Las rutas comunes para la transmisión de virus respiratorios incluyen el contacto cercano a corta distancia y la transmisión de aerosoles a larga distancia. Los aerosoles con los que las personas generalmente entran en contacto se refieren a las gotas respiratorias de los pacientes. Usar una máscara adecuadamente puede bloquear eficazmente las gotitas respiratorias y, por lo tanto, evitar que el virus ingrese directamente al cuerpo. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
