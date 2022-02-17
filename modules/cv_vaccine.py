# random
from random import randrange
import re

import globals

# manejo el estado coronavirus
# vacuna


def cv_vaccine(text, lang='es'):
    last_messages = ['Protéjase', 'Cuídese y cuide a su familia', 'Tome todas las medidas necesarias', 'No salga de casa',
                     'Manténgase alejado del contacto social', 'Cumpla las orientaciones de la dirección del país', 'Use nasobuco']

    p = re.compile(
        r'\b(?:vacuna|tratamiento|cura|terapia|medicamento|receta|medicaci[oó]n)[\s*\w*]*(corona *virus?|covid)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('cv_form')

        result_message = "En la actualidad, no existen tratamientos antivirales específicos contra COVID-19. Los pacientes generalmente reciben atención de apoyo para aliviar los síntomas. Evite el tratamiento antimicrobiano irresponsable o inapropiado, especialmente en combinación con antimicrobianos de amplio espectro. Actualmente no hay vacuna contra la nueva enfermedad. Desarrollar una nueva vacuna puede llevar un tiempo. {}".\
            format(last_messages[randrange(len(last_messages))])
        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
