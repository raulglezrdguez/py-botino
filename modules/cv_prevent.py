# random
from random import randrange
import re

import globals

# manejo el estado coronavirus
# prevenir


def cv_prevent(text, lang='es'):
    last_messages = ['Protéjase', 'Cuídese y cuide a su familia', 'Tome todas las medidas necesarias', 'No salga de casa',
                     'Manténgase alejado del contacto social', 'Cumpla las orientaciones de la dirección del país', 'Use nasobuco']

    p = re.compile(
        r'\b(?:preven(?:ir|go|ci[oó]n)|precauci[oó]n|preve[roae]|precaver|evit[a|o]|elud(?:e|ir)|evad(?:e|ir)|protecci[oó]n|prote[jg][oea])[\s*\w*]*(corona *virus?|covid)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('cv_form')

        result_message = "Lávese las manos frecuentemente con jabón simple o antimicrobiano y enjuague con agua corriente. Asegúrese de secarse las manos con toallas limpias. Lávese las manos inmediatamente después del contacto con secreciones respiratorias (por ejemplo, después de estornudar). Practique buenas prácticas de higiene respiratoria. Cubra la boca y la nariz al toser o estornudar con pañuelos desechables, toallas, etc. y evite tocarse los ojos, la nariz o la boca antes de lavarse bien las manos. Fortalecer la salud general y la inmunidad. Mantenga una dieta equilibrada, duerma lo suficiente y haga ejercicio regularmente, y también evite trabajar en exceso. Mantener una buena higiene y una ventilación adecuada. Abra las ventanas regularmente durante todo el día para dejar entrar aire fresco. Evite lugares con mucha gente o contacto con personas con infecciones respiratorias. Busque atención médica si aparecen fiebre, tos, estornudos, secreción nasal u otros síntomas respiratorios. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
