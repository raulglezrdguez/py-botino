# random
from random import randrange
import re

import globals

# manejo el estado coronavirus
# transmite


def cv_transmit(text, lang='es'):
    last_messages = ['Protéjase', 'Cuídese y cuide a su familia', 'Tome todas las medidas necesarias', 'No salga de casa',
                     'Manténgase alejado del contacto social', 'Cumpla las orientaciones de la dirección del país', 'Use nasobuco']

    p = re.compile(
        r'\b(?:(?:re)?transmit[aeií]|propaga|(?:re)?transmisi[oó]n)[\s*\w*]*(corona *virus?|covid)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('cv_form')

        result_message = "En la actualidad, se cree que la transmisión a través de gotitas y contactos respiratorios es la ruta principal, pero existe el riesgo de transmisión fecal-oral. La transmisión de aerosoles, la transmisión de madre a hijo y otras rutas aún no están confirmadas. Transmisión de gotas respiratorias: este es el modo principal de transmisión de contacto directo. El virus se transmite a través de las gotitas generadas cuando los pacientes tosen, estornudan o hablan, y las personas susceptibles pueden infectarse después de la inhalación de las gotitas. Transmisión de contacto indirecto: el virus puede transmitirse a través de contactos indirectos con una persona infectada. Las gotas que contienen el virus se depositan en la superficie del objeto, que puede tocar con la mano. El virus de la mano contaminada puede pasar a la mucosa (o mucosas) de la cavidad oral, la nariz y los ojos de la persona y provocar una infección. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
