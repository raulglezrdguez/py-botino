# # de https://pypi.org/project/translate/
# from translate import Translator

# translator = Translator(to_lang="zh")
# translation = translator.translate("This is a pen.")
# print(translation)

# translator = Translator(to_lang="es")
# translation = translator.translate("这是一支笔")
# print(translation)


# de: https://pypi.org/project/googletrans/
# ejemplos en: https://stackabuse.com/text-translation-with-google-translate-api-in-python/
from googletrans import Translator
import googletrans

translator = Translator(service_urls=[
    'translate.google.com',
    'translate.google.com.cu',
    'translate.google.com.mx',
])
translations = translator.translate(
    ['Biography of José Martí Pérez', 'and another text with'], dest='es', src='en')
for translation in translations:
    print(translation.text)
translations = translator.translate(
    ['Biography of Juan Pérez', 'and another text with more content'], dest='es', src='en')
for translation in translations:
    print(translation.text)
translations = translator.translate(
    ['Biography of Juan Martí Pérez', 'and another text with a pencil'], dest='es', src='en')
for translation in translations:
    print(translation.text)
translations = translator.translate(
    ['No entiendo, recuerde que puedo ayudarle con los servicios que brindamos en Joven Club, las biografías y las efemérides. Por favor sea más explícito',
     '¿Qué servicios brindan?',
     'Quiero las efemérides',
     'Quiero las biografías',
     'Biografía de José Martí Pérez',
     'No me interesa',
     'Chao'], dest='zh-cn', src='es')
for translation in translations:
    print(translation.text)
translation = translator.translate('这是一支笔', dest='es')
print(translation.text)

# print(googletrans.LANGUAGES)
