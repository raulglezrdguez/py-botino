# random
from random import randrange
import re

import globals

# manejo el estado coronavirus
# resistencia


def cv_resist(text, lang='es'):
    last_messages = ['Protéjase', 'Cuídese y cuide a su familia', 'Tome todas las medidas necesarias', 'No salga de casa',
                     'Manténgase alejado del contacto social', 'Cumpla las orientaciones de la dirección del país', 'Use nasobuco']

    p = re.compile(
        r'\b(?:resist|soporta|aguanta|tolera)[\s*\w*]*(corona *virus?|covid)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('cv_form')

        result_message = "Los virus generalmente pueden sobrevivir durante varias horas en superficies lisas. Si la temperatura y la humedad lo permiten, pueden sobrevivir durante varios días. El nuevo coronavirus es sensible a los rayos ultravioleta y al calor. Calor sostenido a 56 °C durante 30 minutos, el éter, alcohol al 75%, los desinfectantes que contienen cloro, el ácido peracético, el cloroformo y otros solventes lipídicos pueden inactivar eficazmente el virus. La clorhexidina (también conocida como gluconato de clorhexidina) también inactiva eficazmente el virus. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
