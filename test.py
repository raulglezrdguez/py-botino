from math import sin
import re
import datetime

from math import *
import parser

# ignorecase
#p = re.compile(r'[a-z]+', re.I)
#m = p.search("esTo es una prueba")

# if m:
#    print(m.group())
#    print(m.span()[0], m.span()[1])
#    print(len(m.group()))
#    for g in m.group():
#        print(g)
# else:
#    print("sin grupo")

# p = re.compile(r'\b(\bgeroclub\b|\badult[a|o]s?\b[\s*\w*]*\bmayor(?:es)?\b)\b', re.IGNORECASE)
# p = re.compile(r'\b(descontamina(?:r|ci[o|ó]n))\b', re.IGNORECASE)
# p = re.compile(r'\b((?:elimina(?:r|ci[o|ó]n)|borrar|quitar|limpi(?:ar|eza|esa))\b[\s*\w*]*virus?\b)', re.IGNORECASE)
# p = re.compile(r'\b(pasar(?:le)?\b[\s*\w*]*antivirus?\b)', re.IGNORECASE)
# p = re.compile(r'\b((?:asist(?:en?|an?|ir|encias?|entes?)|ayudan(?:te)?|ayudar?)\b[\s*\w*]*(?:inform[a|á]tic[o|a]s?|m[o|ó]vil(?:es)?|tel[e|é]fonos?|tabletas?|domicilios?|casas?|hogar(?:es)?)\b)', re.IGNORECASE)
# p = re.compile(r'\b(instal(?:ar?|aci[o|ó]n|en))\b[\s*\w*]*(aplicaci[o|ó]n(?:es)?|perif[e|é]ricos?)\b', re.IGNORECASE)
# p = re.compile(r'\b(plan(?:es)?)\b[\s*\w*]*(seguridad|inform[a|á]ticas?)\b', re.IGNORECASE)
# p = re.compile(r'\b(asist(?:[e|a]n?|ir|encias?|ente)|ayuda(?:n|r|ntes?)?)\b[\s*\w*]*(t[e|é]cnic[a|o]s?)\b', re.IGNORECASE)
# p = re.compile(r'\b(desarroll(?:o|ar?)|implementa(?:n|r|ci[o|ó]n)?)\b[\s*\w*]*(soluci[o|ó]n(?:es)?|inform[a|á]tic[a|o]s?)\b', re.IGNORECASE)
# p = re.compile(r'\bservicios?\b[\s*\w*]*\bprofesional(?:es)?\b', re.IGNORECASE)
# p = re.compile(r'\b(?:tendederas?)|(?:red(?:es)?\b[\s*\w*]*\bsocial(?:es)?)\b', re.IGNORECASE)
# p = re.compile(r'\breflejos?|blogs?|opini[o|ó]n(?:es)?\b', re.IGNORECASE)
# p = re.compile(r'\bestanquillos?\b|\bpublicaci[o|ó]n(?:es)?\b|\blibros?\b', re.IGNORECASE)
# p = re.compile(r'\becured\b|\benciclopedias?\b|\bcolabora(?:r|ci[o|ó]n(?:es)?|tiv[o|a]s?)?\b', re.IGNORECASE)
# p = re.compile(r'\brevistas?\b|\btino\b|\bpublicar\b', re.IGNORECASE)
# p = re.compile(r'\bludox\b|\bdistra(?:er(?:nos)?|cci[o|ó]n(?:es)?)\b|\bdiver(?:tir(?:nos)?|si[o|ó]n(?:es)?)\b|\brecrea(?:r(?:se)?|ci[o|ó]n(?:es)?)?\b|\bocios?\b|\bvideojuegos?\b|\bjugar\b|\bjueg[a|o]s?\b|\bentreten(?:er(?:nos|l[o|a]s?|me|se)?)?\b', re.IGNORECASE)
# p = re.compile(r'\bvisor\b|\bv[i|í]deos?\b', re.IGNORECASE)
# p = re.compile(r'\btiempos?\b[\s*\w*]*\bm[a|á]quinas?\b', re.IGNORECASE)
# p = re.compile(r'\b(?:alquil[e|a]r|rentar?|arriend[o|a])\b[\s*\w*]*(?:m[a|á]quinas?|computador(?:as?)?|ordenador(?:es)?|microcomputador(?:as?)?|microo?rdenador(?:es)?|dispositivos?|m[o|ó]vil(?:es)?|tel[e|é]fonos?|tabletas?|pc)\b', re.IGNORECASE)
# p = re.compile(r'\b(?:alquil[e|a]r|rentar?|arriend[o|a])\b[\s*\w*]*(?:local(?:es)?|laboratorios?|habitaci[ó|o]n(?:es)?|[á|a]reas?)\b', re.IGNORECASE)
# p = re.compile(r'\b(?:)\b[\s*\w*]*(?:)\b', re.IGNORECASE)
# p = re.compile(r'\b(proyec(?:ci[ó|o]n(?:es)?|tar)|presenta(?:r|ci[o|ó]n(?:es)?)?|expo(?:er|sici[o|ó]n(?:es)?))\b[\s*\w*]*(audiovisual(?:es)?|pel[i|í]culas?|v[í|i]deos?|documental(?:es)?|filmes?|cinematogr[á|a]ficos?)\b', re.IGNORECASE)
# p = re.compile(r'\b(torneos?|juegos?|videojuegos?|campeonatos?|comp(?:et(?:ir|encias?)|it[a|e|o])|juega|jugar)\b', re.IGNORECASE)
# p = re.compile(r'\b(navega(?:r|ci[ó|o]n)|nautas?|emails?|correos?|mensaje(?:s|r[i|í]as?)?)\b', re.IGNORECASE)
# p = re.compile(r'\b(imprimir(?:se)?|impresi[o|ó]n(?:es)?|impresos?)\b', re.IGNORECASE)
# p = re.compile(r'\b(en|a?dentro|nuestr[o|a]s)\b[\s*\w*]*\b(instalaci[o|ó]n(?:es)?|club(?:es)?|local(?:es)?|laboratorios?)\b', re.IGNORECASE)
# p = re.compile(r'\b(s[i|í]|ok|correcto|de +acuerdo)\b', re.IGNORECASE)
# p = re.compile(r'\b(acontecimientos?|aconteci[oó]|sucesos?|sucedi[oó]|efem[eé]rides?|ocurri(?:o|ó|dos?|eron)|hechos?|eventos?)\b[\s*\w*]*\b(hoy|ahora)\b', re.IGNORECASE)
# p = re.compile(r'\b(efem[eé]rides?)\b', re.IGNORECASE)
# p = re.compile(r'\b(buen(?:[oa]s?)?\b\s*d[ií]as?|tardes?|noches?)\b', re.IGNORECASE)
# p = re.compile(r'\b(c[óo]mo\b\s*estas?)\b', re.IGNORECASE)
# p = re.compile(r'\b(chao|adi[oó]s|termina(?:r|mos?)|cerrar|cu[ií]date|gracias?|nos\s+vemos?|hasta\s+(?:luego|ma[ñn]ana|pronto|nunca)|hasta\s+la\s+(?:pr[óo]xima|vista)|tengas?\b[\s*\w*]*\bbuen(?:os?)?\s+d[ií]as?|(?:te|le|lo)\s+veo\s+(?:luego|despu[eé]s|ma[nñ]ana)|(?:le|te)\s+vaya\s+(?:bien|mal))\b', re.IGNORECASE)
# p = re.compile(r'\b(buenas?|saludos?|hola|buen(?:[oa]s?)?\b\s*(?:d[ií]as?|tardes?|noches?)|c[óo]mo\b\s*estas?|todo\b\s*bien|qu[eé]\b\s*(?:pasa|hay|tal))\b', re.IGNORECASE)
# p = re.compile(r'\b(revistas?|tino)\b[\s*\w*]*(t[ií]tulo)\b:*\s+:*(?P<titulo>[\s*\w*]*)\b', re.IGNORECASE)
# p = re.compile(r'\b(revistas?|tino)\b[\s*\w*]*(autor(?:es)?)\b:*\s+:*(?P<author>[\s*\w*]*)\b', re.IGNORECASE)
# que hora es/tiene, tiene hora,
# p = re.compile(r'\b(qu[ée]\b\s*h?ora\b\s*(?:es|tienes?))\b|\b(tienes?\b\s*(?:la\b\s*)?h?ora)\b', re.IGNORECASE)
#  que dia es (hoy), a cuanto estamos, que dia estamos
# p = re.compile(r'\b(qu[ée]\b\s*d[íi]as?\b\s*es(?:tamos?)?)\b|\b(a\b\s*cu[áa]nto\b\s*estamos?)\b', re.IGNORECASE)
#  estado del tiempo
# p = re.compile(r'\b(?:estado|condici[óo]n(?:es)?)\b\s*del\b\s*tiempo\b', re.IGNORECASE)
# biografia del martir revolucionario fulano
# p = re.compile(r'\b(biograf[íi]as?|historias?|trayectorias?|vidas?)\s+(?:del?\s+)?(?:m[aá]rtir\s+(?:revolucionario\s+)?)?(?:revolucionario\s+(?:m[áa]rtir\s+)?)?(?P<martir>[\s*\w*]*)\b', re.IGNORECASE)
# martir = "Joséeñáéíóúu Martí"
# martir = re.sub(r'[áéíóúñÑÁÉÍÓÚ]', '_', martir)
# print(martir)
# def change_letter(letter):
#     switcher = {
#         'a': '[a|á]',
#         'e': '[e|é]',
#         'i': '[i|í]',
#         'o': '[o|ó]',
#         'u': '[u|ú]',
#         'á': '[a|á]',
#         'é': '[e|é]',
#         'í': '[i|í]',
#         'ó': '[o|ó]',
#         'ú': '[u|ú]',
#         'n': '[n|ñ]',
#         'ñ': '[n|ñ]',
#     }
#     return switcher.get(letter, letter)

# def change_word(word):
#     result = ''
#     for c in word:
#         result = result + change_letter(c)
#     return result

# pattern = change_word('josé marti')
# p = re.compile(rf"\b{pattern}\b", re.IGNORECASE)
# m = p.search('Jose martínez')
# if m:
#     print(m)

# m = p.search('biografia de fulano de tal')
# if m:
#     print(m.span())
#     print(m.groups())
#     print(m.group('martir'))
#     for g in m.groups():
#         print(g)

# today = datetime.datetime.today()
# print(today.year, today.month, today.day, today.weekday())

# now = datetime.datetime.now()
# # print('hora', now.H)
# # print('minutos', now.M)
# # current_time = now.strftime("%H con %M")
# print('time', now.hour, now.minute)

# para obtener una fecha de la forma 'dia otras palabras mes'
# p = re.compile(r'\b(?P<dia>\d{1,2})\b[\s*\w*]*\b(?P<mes>enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)\b')
# m = p.search('esto es una fecha 12 marzo')
# if m:
#     print(m.span())
#     print(m.group(1), m.group(2))
#     print(m.group('dia'), m.group('mes'))
#     print(m.groups())
#     for g in m.groups():
#         print(g)


# # para obtener una fecha de la forma 'mes otras palabras dia'
# p = re.compile(r'\b(?P<mes>enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)\b[\s*\w*]*\b(?P<dia>\d{1,2})\b')
# m = p.search('esto es una fecha 12 abril del dia  23')
# if m:
#     print(m.span())
#     print(m.group(1), m.group(2))
#     print(m.group('dia'), m.group('mes'))
#     print(m.groups())
#     for g in m.groups():
#         print(g)

# # para obtener una fecha de la forma 'primero otras palabras mes'
# p = re.compile(r'\b(?P<dia>primer[oa]*)\b[\s*\w*]*\b(?P<mes>enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)\b')
# m = p.search('el primer dia de abril que me parece')
# if m:
#     print(m.span())
#     print(m.group(1), m.group(2))
#     print(m.group('dia'), m.group('mes'))
#     print(m.groups())
#     for g in m.groups():
#         print(g)

# # para obtener una fecha de la forma 'mes otras palabras primero'
# p = re.compile(r'\b(?P<mes>enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)\b[\s*\w*]*\b(?P<dia>primer[oa]*)\b')
# m = p.search('esto es una fecha 12 abril del dia  primera')
# if m:
#     print(m.span())
#     print(m.group(1), m.group(2))
#     print(m.group('dia'), m.group('mes'))
#     print(m.groups())
#     for g in m.groups():
#         print(g)

# p = re.compile(
#     r'\b(?:m[aá]scara|careta|antifaz|mascarilla|disfraz|nasobuco|barbijo|tapa *boca)[\s*\w*]*corona *virus?\b', re.IGNORECASE)
# m = p.search('tengo tapaboca del corona  virus')
# if m:
#     print('si tienes')
# else:
#     print('no tienes')


# hay que utilizar
# from math import *
# asi podemos utilizar todas las funciones que necesitemos
# recursive regex
# https://www.rexegg.com/regex-recursion.html
# https://stackoverflow.com/questions/26385984/recursive-pattern-in-regex

# p = re.compile(
#     r'(?P<number>-?\s*\d+\.?\d*)\s*(?P<expression>[-+*\/]\s*-?\d+\.?\d*)*', re.IGNORECASE)

# p = re.compile(
#     r'(?P<head>(-|menos?)?\s*\d+\.?\d*)\s*(?P<tail>.+)')
# m = p.search(
#     'menos23.2 por menos 2.1 por menos 3  por 5 mas 2 mas 2')
# # m = p.search('calcula 123564564')
# if m:
#     head = m.group('head')
#     print(head)
#     head = re.sub(r'menos?', '-', head)
#     tail = m.group('tail')
#     print(tail)
#     tail = re.sub(r'\b(di[vb]idido\s+por|di[vb]idido)\b', '/', tail)
#     tail = re.sub(r'\bpor\b', '*', tail)
#     tail = re.sub(r'\bm[aá]s\b', '+', tail)
#     tail = re.sub(r'\bmenos?\b', '-', tail)
#     print(tail)
#     p1 = re.compile(r'[-+*\/]\s*-?\s*\d+\.?\d*')
#     m1 = p1.findall(tail)
#     if m1:
#         expression = head
#         for t in m1:
#             expression = expression + ' ' + t
#         print(round(eval(expression), 4))
#     else:
#         print('sin cola')
# else:
#     print('vacio')

# # import parser
# formula = "sin(x)*x**2"
# try:
#     code = parser.expr(formula).compile()
#     x = 10
#     print(eval(code))
# except SyntaxError:
#     print('error de sintaxis')
# except SystemError:
#     print('error del sistema')
# except MemoryError:
#     print('error de memoria')
# except OverflowError:
#     print('error de overflow')


p = re.compile(
    r'(?P<head>(\(|(abr(ir|e)\s*par[eé]ntesis?|abr(ir|e)))*\s*(-|menos?)?(\(|(abr(ir|e)\s*par[eé]ntesis?|abr(ir|e)))*\s*(\(|(abr(ir|e)\s*par[eé]ntesis?|abr(ir|e)))*\d+\.?\d*(\(|(abr(ir|e)\s*par[eé]ntesis?|abr(ir|e)))*)\s*(?P<tail>.+)', re.IGNORECASE)
# m = p.search('Abrir PAréntesis menos 23.2 por menos 2.1 por menos 3  por Abre parentesis  5 mas 2 cierra paréntesis cerrar  mas 2')
m = p.search('calcula 12 * 2')
if m:
    head = m.group('head')
    print('head:', head)
    head = re.sub(
        r'\b(abr(ir|e)\s*par[eé]ntesis?|abr(ir|e))\b', '(', head, flags=re.IGNORECASE)
    head = re.sub(r'menos?', '-', head, flags=re.IGNORECASE)
    tail = m.group('tail')
    print('tail:', tail)
    tail = re.sub(
        r'\b(abr(ir|e)\s*par[eé]ntesis?|abr(ir|e))\b', '(', tail, flags=re.IGNORECASE)
    tail = re.sub(
        r'\b((cerrar|[cs]ierras?)\s*par[eé]ntesis?|(cerrar|[cs]ierras?))\b', ')', tail, flags=re.IGNORECASE)
    tail = re.sub(r'\b(di[vb]idido\s+por|di[vb]idido)\b',
                  '/', tail, flags=re.IGNORECASE)
    tail = re.sub(r'\bpor\b', '*', tail, flags=re.IGNORECASE)
    tail = re.sub(r'\bm[aá]s\b', '+', tail, flags=re.IGNORECASE)
    tail = re.sub(r'\bmenos?\b', '-', tail, flags=re.IGNORECASE)
    print('tail:', tail)
    p1 = re.compile(r'[-+*\/]\(*\s*\(*-?\(*\s*\(*\d+\.?\d*(?:\s*\)*)*')
    m1 = p1.findall(tail)
    if m1:
        expression = head
        for t in m1:
            expression = (expression + ' ' + t).strip()
        print('expression:', expression)
        try:
            code = parser.expr(expression).compile()
            print(round(eval(code), 4))
        except SyntaxError:
            print('error de sintaxis')
        except SystemError:
            print('error del sistema')
        except MemoryError:
            print('error de memoria')
        except OverflowError:
            print('error de overflow')

    else:
        print('sin cola')
else:
    print('vacio')

# print(isinstance(12, int))
# print(isinstance('probando', str))

# p = re.compile('[-+*\/]?\s*-?\s*\d+\.?\d*')
# # m = p.search('calcula -23.2 * -2.1 * - 3')
# a = p.findall('calcula -23.2  2.1 * - 3.1')
# print('aaaaaaaaaaa', a)
# print('mmmmmmmmmmm', m)
# if m:
#     print(m.groups())
#     expression = m.group('number')  # + ' ' + m.group('expression')
#     print(expression)
#     print('OK')
#     print(eval(expression, {'sqrt': sqrt, 'pow': pow}, {}))
# else:
#     print('error')

# # clase que devuelvo de la traduccion
# class Traduccion(object):
#     def __init__(self, texto, origen):
#         self.text = texto
#         self.origin = origen


# # textos de entrada
# text = ['probando1', 'proband2']

# # arreglo resultante
# results = [Traduccion('I cant translate', x) for x in text]


# for obj in results:
#     print(obj.origin, obj.text)
