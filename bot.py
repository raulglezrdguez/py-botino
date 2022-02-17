# este es el bot para manejar las peticiones de los usuarios
# es un servicio restfull que recibe un json {'text': 'texto del cliente'}
# y responde {'text': 'respuesta del bot'}

# utilizar sus funciones
import globals
from random import randrange
import os
import socket

# para guardar los logs
import sqlite3
import datetime

# flask para trabajar el servidor api restfull
from flask import Flask, jsonify, render_template, make_response, send_from_directory, request
from flask_restful import reqparse, Api, Resource
from flask_cors import CORS

# para trabajar con el reconocimiento facial
import cv2
import numpy as np

from modules.free_speech import free_speech

# random

# importo las variables globales

# servidor api
app = Flask(__name__, static_url_path='')
app.config['MAX_CONTENT_LENGTH'] = 16 * 500 * 500

api = Api(app)
CORS(app, resources={r"/getResponse/*": {"origins": "*"}})

# parser para obtener la pregunta del cliente
parser = reqparse.RequestParser()
parser.add_argument('text', default=None)
parser.add_argument('lang', default='es')
parser.add_argument('body', action='append')

# ip del servidor
RetMyIP = 'localhost'


def default(text, lang):  # envio un mensaje por defecto
    first_messages = ['No entiendo', 'No comprendo',
                      'No puedo entenderle', 'No sé qué ha dicho']
    middle_messages = ['soy su asistente para los servicios de Joven Club, las biografías y las efemérides',
                       'soy experto en los servicios que brinda Joven Club, biografías y efemérides', 'puedo ayudarle con los servicios que brindamos en Joven Club, las biografías y las efemérides']
    last_messages = ['sea más explícito', 'inténtelo de nuevo',
                     'deme más detalles', 'sea más preciso']

    if lang == 'es':

        result_message = "{}, recuerde que {}. Por favor {}".format(first_messages[randrange(len(
            first_messages))], middle_messages[randrange(len(middle_messages))], last_messages[randrange(len(last_messages))])

        body = [
            {"tag": "p", "innerText": result_message},
            {"tag": "answer", "label": "¿Qué servicios brindan?", "text": "Servicios"},
            {"tag": "answer", "label": "Quiero las efemérides", "text": "Efemérides"},
            {"tag": "answer", "label": "Quiero las biografías",
                "text": "Biografía de José Martí Pérez"},
            {"tag": "answer", "label": "No me interesa", "text": "Chao"},
        ]

    else:
        to_translate = ["{}, recuerde que {}. Por favor {}".format(first_messages[randrange(len(
            first_messages))], middle_messages[randrange(len(middle_messages))], last_messages[randrange(len(last_messages))]),
            "¿Qué servicios brindan?",
            "Quiero las efemérides",
            "Quiero las biografías", "Biografía de José Martí Pérez",
            "No me interesa", "Chao"]
        translations = globals.translate_array(
            to_translate, dest=lang, src='es')

        result_message = translations[0].text

        body = [
            {"tag": "p", "innerText": result_message},
            {"tag": "answer",
                "label": translations[1].text, "text": translations[1].text},
            {"tag": "answer",
                "label": translations[2].text, "text": translations[2].text},
            {"tag": "answer", "label": translations[3].text,
                "text": translations[4].text},
            {"tag": "answer",
                "label": translations[5].text, "text": translations[6].text},
        ]

    return result_message, body


def idle(text, lang):
    # función que maneja los estados y devuelve una respuesta

    # create logs connection
    logs_conn = sqlite3.connect('./dbs/logs.db')
    # create cursor
    logs_cursor = logs_conn.cursor()

    original_text = text
    result_ok = '1'
    # traduzco siempre al español
    if lang != 'es':
        text = globals.translate_text(text, dest='es', src=lang)

    first_state = globals.current_state
    result, body = globals.handlers[globals.current_state](text, lang)
    while result is None:
        globals.current_state = (
            globals.current_state + 1) % len(globals.handlers)
        if (globals.current_state == first_state):
            result = free_speech(text, lang)
            if result != None:
                body = None
            else:
                result_ok = '0'
                result, body = default(text, lang)
        else:
            result, body = globals.handlers[globals.current_state](text, lang)

    logs_cursor.execute("INSERT INTO logs VALUES ('{}','{}', '{}')".format(
        original_text, result_ok, datetime.datetime.now()))
    # Save (commit) the changes and close connection
    logs_conn.commit()
    logs_conn.close()

    if body is None:
        return result, None
    else:
        return result, str(body)


def idle_body(body, lang):
    # función que maneja los estados y devuelve una respuesta segun el body

    first_state = globals.current_state_body
    result, bd = globals.handlers_body[globals.current_state_body](body, lang)
    while result is None:
        globals.current_state_body = \
            (globals.current_state_body + 1) % len(globals.handlers_body)
        if (globals.current_state_body == first_state):
            result, bd = default(body, lang)
        else:
            result, bd = \
                globals.handlers_body[globals.current_state_body](body, lang)

    return result, str(bd)


class Root(Resource):  # clase que manejan las peticiones de la ruta /
    def get(self):
        # return jsonify(text= 'Haga una petición POST pasando en el body {"text": "Texto a enviar"}')
        headers = {'Content-Type': 'text/html'}
        # RetMyIP = os.popen("hostname -I").read().strip()
        RetMyIP = getIP()
        return make_response(render_template('index.html', ip=RetMyIP), 200, headers)
        # return make_response(render_template('index.html', ip='192.168.43.178'), 200, headers)

    def post(self):
        args = parser.parse_args()
        # print(args)
        input_text = args['text']
        input_lang = args['lang']
        input_body = args['body']
        if (input_text != None):
            text, body = idle(input_text, input_lang)
            return jsonify(input_text=input_text, text=text, body=body)
        elif (input_body != None):
            text, body = idle_body(input_body, input_lang)
            return jsonify(input_text='', text=text, body=body)
        else:
            return jsonify(input_text='', text='', body='')


class Response(Resource):  # clase que manejan las peticiones de la ruta /getResponse
    def get(self):
        return jsonify(text='Haga una petición POST pasando en el body {"text": "Texto a enviar"}', body='')

    def post(self):
        args = parser.parse_args()
        # print(args)
        input_text = args['text']
        input_lang = args['lang']
        input_body = args['body']

        # print(input_body)
        if (input_text != None):
            text, body = idle(input_text, input_lang)
            return jsonify(input_text=input_text, text=text, body=body)
        elif (input_body != None):
            text, body = idle_body(input_body, input_lang)
            return jsonify(input_text='', text=text, body=body)
        else:
            return jsonify(input_text='', text='', body='')


class FaceDetect(Resource):
    def get(self):
        return jsonify(text='Haga una petición POST pasando en el body {"image": "Image"}', body='')

    def post(self):
        # args = parser.parse_args()
        if 'image' not in request.files:
            print("without image")
            return jsonify(input_text='', text='', body='')
        else:
            # img = cv2.imdecode(np.fromstring(
            #     request.files['image'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
            img = cv2.imdecode(np.frombuffer(
                request.files['image'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
            face_cascade = cv2.CascadeClassifier(
                './face/haarcascade_frontalface_default.xml')
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            res = ""
            for (x, y, w, h) in faces:
                res = f"{res}{x},{y},{w},{h};"

            print(f"res: {res}")

            return jsonify(input_text='', text=res, body='')

        return jsonify(input_text='', text='', body='')


@app.route('/templates/<path:path>')
def send_template(path):
    return send_from_directory('templates', path)


@app.route('/<path:path>')
def send_resource(path):
    return send_from_directory('templates', path)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'templates'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/favicon-32x32.png')
def favicon_png():
    return send_from_directory(os.path.join(app.root_path, 'templates'), 'botino.png', mimetype='image/vnd.microsoft.icon')


# adiciono las rutas
api.add_resource(Root, '/')
api.add_resource(Response, '/getResponse/')
api.add_resource(FaceDetect, '/face/')


def getIP():
    # nombre del sistema operativo
    os_name = os.name
    if os_name == 'posix':
        # esta corriendo en linux
        RetMyIP = os.popen("hostname -I").read().strip()
    elif os_name == 'nt':
        # corriendo en windows
        try:
            host_name = socket.gethostname()
            RetMyIP = socket.gethostbyname(host_name)
        except:
            RetMyIP = 'localhost'

    return RetMyIP


# corro el servidor
if __name__ == '__main__':
    RetMyIP = getIP()

    # print(RetMyIP)
    if RetMyIP != '':
        # app.run(host=RetMyIP, port=8080, debug=True)
        # pc ubuntu del joven club
        app.run(host='10.5.44.66', port=8088, debug=True)
        # laptop conectada al movil
        # app.run(host='192.168.43.178', port=8088, debug=True)
        # laptop en la casa conectada por el nano
        # app.run(host='192.168.137.1', port=8088, debug=True)
    else:
        app.run(host='localhost', port=8080, debug=True)
        # app.run(host='192.168.43.178', port=8088, debug=True)
