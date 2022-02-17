# random
from random import randrange
import re

import globals

# manejo el estado coronavirus
# susceptible


def cv_susceptible(text, lang='es'):
    last_messages = ['Protéjase', 'Cuídese y cuide a su familia', 'Tome todas las medidas necesarias', 'No salga de casa',
                     'Manténgase alejado del contacto social', 'Cumpla las orientaciones de la dirección del país', 'Use nasobuco']

    p = re.compile(
        r'\b(?:susceptible|sensible|propens[oa]|proclive|predispuest[oa])[\s*\w*]*(corona *virus?|covid)\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        globals.current_state = globals.find_handler_index('cv_form')

        result_message = "El nuevo coronavirus es recientemente emergente en humanos. Por lo tanto, la población general es susceptible porque carecen de inmunidad contra ella. 2019-nCoV puede infectar a las personas con inmunidad normal o comprometida. La cantidad de exposición al virus también determina si se infecta o no. Si está expuesto a una gran cantidad de virus, puede enfermarse incluso si su función inmunológica es normal. Para las personas con una función inmune deficiente, como los ancianos, las mujeres embarazadas o las personas con disfunción hepática o renal, la enfermedad progresa relativamente rápido y los síntomas son más graves. El factor dominante que determina si uno se infecta o no es la posibilidad de exposición. Por lo tanto, no se puede concluir simplemente que una mejor inmunidad reducirá el riesgo de infección. Los niños tienen menos posibilidades de exposición y, por lo tanto, una menor probabilidad de infección. Sin embargo, con la misma exposición, las personas mayores, las personas con enfermedades crónicas o inmunidad comprometida tienen más probabilidades de infectarse. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
