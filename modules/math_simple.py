# from math import *
import re
import parser

import globals


def math_simple(text, lang='es'):
    # manejo el estado math_simple
    # respondo a ecuaciones con parentesis, con las operaciones básicas [+-*/]

    text = re.sub(r'\buno\b', '1', text, flags=re.IGNORECASE)
    text = re.sub(r'\bdos?\b', '2', text, flags=re.IGNORECASE)
    text = re.sub(r'\btres?\b', '3', text, flags=re.IGNORECASE)
    text = re.sub(r'\bcuatro\b', '4', text, flags=re.IGNORECASE)
    text = re.sub(r'\b[cs]inco\b', '5', text, flags=re.IGNORECASE)
    text = re.sub(r'\b[sc]eis\b', '6', text, flags=re.IGNORECASE)
    text = re.sub(r'\bsiete\b', '7', text, flags=re.IGNORECASE)
    text = re.sub(r'\bocho\b', '8', text, flags=re.IGNORECASE)
    text = re.sub(r'\bnueve\b', '9', text, flags=re.IGNORECASE)
    text = re.sub(r'\bcero\b', '0', text, flags=re.IGNORECASE)
    text = re.sub(r'\bdie[zs]\b', '10', text, flags=re.IGNORECASE)
    text = re.sub(r'\s*puntos?\s*|\s*comas?\s*',
                  '.', text, flags=re.IGNORECASE)
    text = re.sub(r'\s*\.\s*|\s*,\s*', '.', text, flags=re.IGNORECASE)

    p = re.compile(
        r'(?P<head>(\(|(abr(ir|e)\s*par[eé]ntesis?|abr(ir|e)))*\s*(-|menos?)?(\(|(abr(ir|e)\s*par[eé]ntesis?|abr(ir|e)))*\s*(\(|(abr(ir|e)\s*par[eé]ntesis?|abr(ir|e)))*\d+\.?\d*(\(|(abr(ir|e)\s*par[eé]ntesis?|abr(ir|e)))*)\s*(?P<tail>.+)', re.IGNORECASE)
    m = p.search(text)

    if m:
        head = m.group('head')
        head = re.sub(
            r'\b(abr(ir|e)\s*par[eé]ntesis?|abr(ir|e))\b', '(', head, flags=re.IGNORECASE)
        head = re.sub(r'menos?', '-', head, flags=re.IGNORECASE)
        # print('head', head)

        tail = m.group('tail')
        tail = re.sub(
            r'\b(abr(ir|e)\s*par[eé]ntesis?|abr(ir|e))\b', '(', tail, flags=re.IGNORECASE)
        tail = re.sub(
            r'\b((cerrar|[cs]ierras?)\s*par[eé]ntesis?|(cerrar|[cs]ierras?))\b', ')', tail, flags=re.IGNORECASE)
        tail = re.sub(r'\b(di[vb]idido\s+por|di[vb]idido)\b',
                      '/', tail, flags=re.IGNORECASE)
        tail = re.sub(r'\bpor\b', '*', tail, flags=re.IGNORECASE)
        tail = re.sub(r'\b[xX]\b', '*', tail, flags=re.IGNORECASE)
        tail = re.sub(r'\bm[aá]s\b', '+', tail, flags=re.IGNORECASE)
        tail = re.sub(r'\bmenos?\b', '-', tail, flags=re.IGNORECASE)

        p1 = re.compile(r'[-+*\/\.]\(*\s*\(*-?\(*\s*\(*\d+\.?\d*(?:\s*\)*)*')
        # print('tail: ', tail)
        m1 = p1.findall(tail)
        if m1:
            expression = head
            for t in m1:
                expression = (expression + ' ' + t).strip()
            print('expression: ', expression)
            try:
                code = parser.expr(expression).compile()
                result_message = str(round(eval(code), 2))
            except SyntaxError:
                result_message = 'Error de sintaxis'
            except SystemError:
                result_message = 'Error del sistema'
            except MemoryError:
                result_message = 'Error de memoria'
            except OverflowError:
                result_message = 'Error de overflow'
            except:
                return None, None

            if isinstance(result_message, str):
                if lang == 'es':
                    return result_message, None
                else:
                    translation = globals.translate_text(
                        result_message, dest=lang, src='es')
                    return translation, None
            else:
                return result_message, None
        else:
            return None, None
    else:
        return None, None
