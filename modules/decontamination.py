# random
from random import randrange
import re

# import globals

# manejo el estado descontaminación de dispositivos


def decontamination(text, lang='es'):

    last_messages = ['Adquiera la licencia para segurmática',
                     'Proteja sus dispositivos con segurmática antivirus', 'Utilice el antivirus segurmática para Cuba']
    result_message = "Servicio de descontaminación de dispositivos: le revisamos y descontaminamos sus dispositivos informáticos como memorias extraíbles y discos duros, garantizamos la eliminación de los virus de su medio. {}".format(
        last_messages[randrange(len(last_messages))])

    p = re.compile(r'\b(des *contamina(?:r|ci[o|ó]n))\b', re.IGNORECASE)
    m = p.search(text)

    if m:
        if lang == 'es':
            return result_message, None
        else:
            translation = globals.translate_text(
                result_message, dest=lang, src='es')
            return translation.text, None
    else:
        p = re.compile(
            r'\b((?:elimina(?:r|ci[o|ó]n)|borrar|quitar|limpi(?:ar|eza|esa))\b[\s*\w*]*virus?\b)', re.IGNORECASE)
        m = p.search(text)

        if m:
            if lang == 'es':
                return result_message, None
            else:
                translation = globals.translate_text(
                    result_message, dest=lang, src='es')
                return translation.text, None
        else:
            p = re.compile(
                r'\b(pasar(?:le)?\b[\s*\w*]*antivirus?\b)', re.IGNORECASE)
            m = p.search(text)

            if m:
                if lang == 'es':
                    return result_message, None
                else:
                    translation = globals.translate_text(
                        result_message, dest=lang, src='es')
                    return translation, None
            else:
                return None, None
