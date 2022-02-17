# random
from random import randrange
import re

import globals

# manejo el estado coronavirus
# contagioso


def cv_contagion(text, lang='es'):
    last_messages = ['Protéjase', 'Cuídese y cuide a su familia', 'Tome todas las medidas necesarias', 'No salga de casa',
                     'Manténgase alejado del contacto social', 'Cumpla las orientaciones de la dirección del país', 'Use nasobuco']

    p = re.compile(
        r'\b(?:contagio|contamina|infecta|infecci[oó]n|pega)[\s*\w*]*(corona *virus?|covid)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('cv_form')

        result_message = "Los coronavirus comunes infectan principalmente a adultos o niños mayores, causando el resfriado común. Algunas cepas pueden causar diarrea en adultos. Estos virus se transmiten principalmente por gotitas y también se pueden propagar a través de la ruta fecal-oral. La incidencia de infección por el corona virus es frecuente en invierno y primavera. El período de incubación de los coronavirus suele ser de 3 a 7 días. El período de incubación del virus es tan corto como 1 día, pero generalmente se considera que no supera los 14 días. Pero debe tenerse en cuenta que algunos casos reportados tuvieron un período de incubación de hasta 24 días. El nuevo coronavirus es altamente infeccioso y puede ser fatal, pero su mortalidad no se ha determinado en la actualidad. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
