# random
from random import randrange
import re

import globals

# manejo el estado mochila


def mochila(text, lang='es'):

    last_messages = ['Descargue documentos con el servicio de la mochila', 'Disfrute de audiovisuales desde nuestro servicio la mochila',
                     'Estudie con los libros y manuales de la mochila', 'Utilice las aplicaciones que le proponemos en la mochila']

    p = re.compile(r'\bmochilas?\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        # globals.current_state = globals.find_handler_index('red')
        result_message = "Servicio de La Mochila: usted puede disfrutar de audiovisuales, aplicaciones, libros y otros de forma gratuita en nuestras instalaciones. {}".\
            format(last_messages[randrange(len(last_messages))])

        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation, None
    else:
        return None, None
