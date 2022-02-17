from modules.hello import hello
from modules.goodbye import goodbye
from modules.services import services
from modules.training import training
from modules.activities import activities
from modules.course import course
from modules.sufficiency import sufficiency
from modules.interest import interest
from modules.talent import talent
from modules.disability import disability
from modules.geroclub import geroclub
from modules.interior import interior
from modules.machine_time import machine_time
from modules.device_rental import device_rental
from modules.locals_rental import locals_rental
from modules.projection import projection
from modules.games import games
from modules.navigation import navigation
from modules.printer import printer
from modules.red import red
from modules.mochila import mochila
from modules.tendedera import tendedera
from modules.reflejos import reflejos
from modules.estanquillo import estanquillo
from modules.ecured import ecured
from modules.revista_title import revista_title
from modules.revista_author import revista_author
from modules.revista_body import revista_body
from modules.revista import revista
from modules.ludox import ludox
from modules.visor import visor
from modules.segurmatica import segurmatica
from modules.professional import professional
from modules.documents import documents
from modules.decontamination import decontamination
from modules.recovery import recovery
from modules.digitization import digitization
from modules.restore import restore
from modules.postproduction import postproduction
from modules.assistance import assistance
from modules.advisory import advisory
from modules.it_assistance import it_assistance
from modules.installation import installation
from modules.security import security
from modules.develop import develop
from modules.events import events
from modules.events_body import events_body
from modules.ephemeris import ephemeris
from modules.what_time import what_time
from modules.what_day import what_day
from modules.weather import weather
from modules.biography import biography
from modules.biography_body import biography_body
from modules.cv import cv
from modules.cv_classification import cv_classification
from modules.cv_contagion import cv_contagion
from modules.cv_epidemic import cv_epidemic
from modules.cv_form import cv_form
from modules.cv_immunity import cv_immunity
from modules.cv_manifest import cv_manifest
from modules.cv_mask import cv_mask
from modules.cv_prevent import cv_prevent
from modules.cv_resist import cv_resist
from modules.cv_susceptible import cv_susceptible
from modules.cv_transmit import cv_transmit
from modules.cv_vaccine import cv_vaccine
from modules.math_simple import math_simple

from googletrans import Translator  # traductor de google
translator = Translator(service_urls=[
    'translate.google.com',
    'translate.google.com.cu',
    'translate.google.com.mx',
])


# importo las funciones que manejan los estados
handlers_map = [{'label': 'hello', 'fn': hello},
                {'label': 'goodbye', 'fn': goodbye},
                {'label': 'services', 'fn': services},
                {'label': 'training', 'fn': training},
                {'label': 'activities', 'fn': activities},
                {'label': 'course', 'fn': course},
                {'label': 'sufficiency', 'fn': sufficiency},
                {'label': 'interest', 'fn': interest},
                {'label': 'talent', 'fn': talent},
                {'label': 'disability', 'fn': disability},
                {'label': 'geroclub', 'fn': geroclub},
                {'label': 'interior', 'fn': interior},
                {'label': 'machine_time', 'fn': machine_time},
                {'label': 'device_rental', 'fn': device_rental},
                {'label': 'locals_rental', 'fn': locals_rental},
                {'label': 'projection', 'fn': projection},
                {'label': 'games', 'fn': games},
                {'label': 'navigation', 'fn': navigation},
                {'label': 'printer', 'fn': printer},
                {'label': 'red', 'fn': red},
                {'label': 'mochila', 'fn': mochila},
                {'label': 'tendedera', 'fn': tendedera},
                {'label': 'reflejos', 'fn': reflejos},
                {'label': 'estanquillo', 'fn': estanquillo},
                {'label': 'ecured', 'fn': ecured},
                {'label': 'revista_title', 'fn': revista_title},
                {'label': 'revista_author', 'fn': revista_author},
                {'label': 'revista', 'fn': revista},
                {'label': 'ludox', 'fn': ludox},
                {'label': 'visor', 'fn': visor},
                {'label': 'segurmatica', 'fn': segurmatica},
                {'label': 'professional', 'fn': professional},
                {'label': 'documents', 'fn': documents},
                {'label': 'decontamination', 'fn': decontamination},
                {'label': 'recovery', 'fn': recovery},
                {'label': 'digitization', 'fn': digitization},
                {'label': 'restore', 'fn': restore},
                {'label': 'postproduction', 'fn': postproduction},
                {'label': 'assistance', 'fn': assistance},
                {'label': 'advisory', 'fn': advisory},
                {'label': 'it_assistance', 'fn': it_assistance},
                {'label': 'installation', 'fn': installation},
                {'label': 'security', 'fn': security},
                {'label': 'develop', 'fn': develop},
                {'label': 'events', 'fn': events},
                {'label': 'ephemeris', 'fn': ephemeris},
                {'label': 'what_time', 'fn': what_time},
                {'label': 'what_day', 'fn': what_day},
                {'label': 'weather', 'fn': weather},
                {'label': 'biography', 'fn': biography},
                {'label': 'cv', 'fn': cv},
                {'label': 'cv_classification', 'fn': cv_classification},
                {'label': 'cv_contagion', 'fn': cv_contagion},
                {'label': 'cv_epidemic', 'fn': cv_epidemic},
                {'label': 'cv_form', 'fn': cv_form},
                {'label': 'cv_immunity', 'fn': cv_immunity},
                {'label': 'cv_manifest', 'fn': cv_manifest},
                {'label': 'cv_mask', 'fn': cv_mask},
                {'label': 'cv_prevent', 'fn': cv_prevent},
                {'label': 'cv_resist', 'fn': cv_resist},
                {'label': 'cv_susceptible', 'fn': cv_susceptible},
                {'label': 'cv_transmit', 'fn': cv_transmit},
                {'label': 'cv_vaccine', 'fn': cv_vaccine},
                {'label': 'math_simple', 'fn': math_simple}, ]

handlers_map_body = [
    {'label': 'events_body', 'fn': events_body},
    {'label': 'revista_body', 'fn': revista_body},
    {'label': 'biography_body', 'fn': biography_body}]

handlers = [
    course, sufficiency, interest, talent,
    training,
    disability, geroclub,
    activities,
    segurmatica,
    decontamination, recovery, digitization, restore, postproduction,
    documents,
    advisory, it_assistance, installation, security,
    assistance,
    develop,
    professional,
    mochila, tendedera, reflejos, estanquillo, ecured,
    revista_title, revista_author,
    revista, ludox, visor,
    red,
    machine_time, device_rental, locals_rental, projection, games, navigation, printer,
    interior,
    services,
    events,
    ephemeris,
    what_time, what_day, weather,
    biography,
    cv_form,
    cv_classification,
    cv_contagion,
    cv_epidemic,
    cv_immunity,
    cv_manifest,
    cv_mask,
    cv_prevent,
    cv_resist,
    cv_susceptible,
    cv_transmit,
    cv_vaccine,
    cv,
    math_simple,
    hello, goodbye]

handlers_body = [events_body, revista_body, biography_body]

# estado actual de la máquina de estados
current_state = 0
current_state_body = 0


def find_handler_fn(label):  # devuelve la función de un label
    for v in handlers_map:
        if v['label'] == label:
            return v['fn']
    return None


# devuelve el indice de una función de un label en el arreglo handler
def find_handler_index(label):
    fn = find_handler_fn(label)
    if fn != None:
        return handlers.index(fn)
    else:
        return None


def find_handler_fn_body(label):  # devuelve la función de un label para body
    for v in handlers_map_body:
        if v['label'] == label:
            return v['fn']
    return None

# devuelve el indice de una función de un label en el arreglo handler body


def find_handler_index_body(label):
    fn = find_handler_fn_body(label)
    if fn != None:
        return handlers_body.index(fn)
    else:
        return None

# print(find_handler_index('talent'))


def translate_text(text, dest, src):
    # devuelve el resultado de traducir una frase del src al dest

    # esto es para el chino, porque no encontré otra forma de hacerlo
    # siempre le pongo traducir al chino simplificado
    if dest == 'zh':
        dest = 'zh-CN'
    if src == 'zh':
        src = 'zh-CN'

    try:
        translation = translator.translate(text, dest, src)
    except:
        return "No puedo traducir:'{}'".format(text)

    return translation.text


def translate_array(text, dest, src):
    # devuelve el resultado de traducir un arreglo de frases del src al dest

    # clase es que devuelvo de la traduccion, si hay error
    class Traduccion:
        def __init__(self, texto, origen):
            self.text = texto
            self.origin = origen

    # esto es para el chino, porque no encontré otra forma de hacerlo
    # siempre le pongo traducir al chino simplificado
    if dest == 'zh':
        dest = 'zh-CN'
    if src == 'zh':
        src = 'zh-CN'

    print(text, dest, src)

    try:
        translation = translator.translate(text, dest, src)
    except:
        results = [Traduccion('I cant translate', x) for x in text]
        return results

    return translation
