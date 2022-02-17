# random
from random import randrange, choice
import sqlite3
import re
import globals

# importo spacy
import spacy
# creo el objeto nlp
nlp = spacy.load('es_core_news_md')


def free_speech(text, lang='es'):
    # def free_speech(doc, matcher, nlp, lang='es'):
    # manejo el estado free_speech

    # busco el listado de los sustantivios (noun) y verbos (verb) y sus lemas
    # hago las busquedas en el diccionario
    # y respondo a esas palabras

    # lista de sustantivos y verbos
    words = []

    # documento de spacy
    doc = nlp(text)

    # recorro todas las tokens
    for token in doc:
        # print(f'tag: {token.lemma_} {token.tag_}***')
        tags = token.tag_.split('|')
        if len(tags) > 0:
            poe = tags[0].split('__')
            if poe[0] == 'NOUN':
                words.insert(
                    0, {'tag': 'NOUN', 'text': token.text, 'lemma': token.lemma_})
            elif poe[0] == 'VERB' or poe[0] == 'ADJ':
                words.append(
                    {'tag': poe[0], 'text': token.text, 'lemma': token.lemma_})

        # if len(tags) == 2:
        #     poe = tags[0].split('__')
        #     if poe[0] == 'NOUN' and len(poe) == 2:
        #         genders = poe[1].split('=')
        #         if len(genders) == 2 and genders[0] == 'Gender':
        #             gender = genders[1]
        #             numbers = tags[1].split('=')
        #             if len(numbers) == 2 and numbers[0] == 'Number':
        #                 number = numbers[1]
        #                 words.insert(
        #                     0, {'tag': 'noun', 'text': token.text, 'lemma': token.lemma_, 'gender': gender, 'number': number})
        # elif len(tags) == 1:
        #     verbs = tags[0].split('__')
        #     if len(verbs) == 2 and verbs[0] == 'VERB':
        #         verb_forms = verbs[1].split('=')
        #         if len(verb_forms) == 2 and verb_forms[0] == 'VerbForm':
        #             verb_form = verb_forms[1]
        #             words.append(
        #                 {'tag': 'verb', 'text': token.text, 'lemma': token.lemma_, 'verbForm': verb_form})

    if len(words) > 0:
        result = ''

        # abro el diccionario
        conn = sqlite3.connect('./dbs/dictionary.db')
        # create cursor
        c = conn.cursor()

        # recorro todas las palabras
        for w in words:
            # busco la palabra en el dicionario
            word_find = re.sub(r'[áéíóúÁÉÍÓÚaeiou]', '_', w['lemma'])
            select = f"SELECT word, definition FROM dict WHERE word like '{word_find}'"
            rows = c.execute(select)
            for row in rows:
                defs = row[1].split('|')
                result = defs[0]
                for i in range(1, len(defs)):
                    others = [' También es ', ' Asimismo es ',
                              ' Igualmente es ', ' Además es ', ' Incluso es ']
                    result += choice(others) + defs[i][0].lower() + defs[i][1:]

                break

            if result != '':
                result = f"{w['lemma'].capitalize()} es {result[0].lower() + result[1:]}"
                # if w['tag'] == 'noun':
                #     if w['gender'] == 'Masc':
                #         result = f"El {w['lemma']} es {result[0].lower() + result[1:]}"
                #     else:
                #         result = f"La {w['lemma']} es {result[0].lower() + result[1:]}"
                # elif w['tag'] == 'verb':
                #     result = f"{w['lemma']} es {result}"
                break

        # cierro el diccionario
        conn.close()

        # respondo el resultado
        if result != '':
            if lang != 'es':
                result = globals.translate_text(result, lang, 'es')

            return result
        else:
            return None
    return None
