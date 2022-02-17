# random
from random import randrange
import re

import globals

# manejo el estado coronavirus
# manifiesta


def cv_manifest(text, lang='es'):
    last_messages = ['Protéjase', 'Cuídese y cuide a su familia', 'Tome todas las medidas necesarias', 'No salga de casa',
                     'Manténgase alejado del contacto social', 'Cumpla las orientaciones de la dirección del país', 'Use nasobuco']

    p = re.compile(
        r'\b(?:manifiesta|revela|presenta|exhibe|muestra|expresa|aparece)[\s*\w*]*(corona *virus?|covid)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('cv_form')

        result_message = "El inicio de COVID-19 se manifiesta principalmente como fiebre, pero algunos pacientes tempranos pueden no tener fiebre, con solo escalofríos y síntomas respiratorios, que pueden ocurrir junto con tos seca leve, fatiga, falta de respiración, diarrea, etc. Sin embargo, secreción nasal, el esputo y otros síntomas son poco frecuentes. Los pacientes pueden desarrollar disnea gradualmente. En casos severos, la enfermedad puede progresar rápidamente, causando síndrome de dificultad respiratoria aguda, shock séptico, acidosis metabólica irreversible y trastornos de la coagulación en cuestión de días. Algunos pacientes comienzan con síntomas leves sin fiebre. La mayoría de los pacientes tienen un buen pronóstico, mientras que unos pocos se vuelven críticos y a veces fatalmente enfermos. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
