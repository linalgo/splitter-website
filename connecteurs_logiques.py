import re
import string

addition = ['et', 'de plus', 'puis', 'en outre', 'non seulement@mais encore']

alternative = ['ou', 'soit@soit', 'soit@ou', 'tantôt@tantôt', 'ou@ou', 'ou bien', 'seulement@mais encore',
               "l'un@l'autre", "d'un côté@de l'autre"]

but = ['afin que', 'pour que', 'de peur que', 'en vue de', 'de façon à ce que']

cause = ['car', 'en effet', 'effectivement', 'comme', 'par', 'parce que', 'puisque', 'attendu que', 'vu que',
         'étant donné que', 'grâce à', 'par suite de', 'eu égard à', 'en raison de', 'du fait que', 'dans la mesure où',
         'sous prétexte que']

comparaison = ['comme', 'de même que', 'ainsi que', 'autant que', 'aussi@que', 'si@que', 'de la même façon que',
               'semblablement', 'pareillement', 'plus que', 'moins que', 'non moins que', 'selon que', 'suivant que',
               'comme si']

concession = ['malgré', 'en dépit de', 'quoique', 'bien que', 'alors que', 'quelque soit', 'même si',
              "ce n'est pas que", 'certes', 'bien sûr', 'évidemment', 'il est vrai que', 'toutefois']

conclusion = ['en conclusion', 'pour conclure', 'en guise de conclusion', 'en somme', 'bref', 'ainsi', 'donc',
              'en résumé', 'en un mot', 'par conséquent', 'finalement', 'enfin', 'en définitive']

condition = ['si', 'au cas où', 'à condition que', 'pourvu que', 'à moins que', 'en admettant que', 'pour peu que',
             'à supposer que', 'en supposant que', "dans l'hypothèse où", 'dans le cas où', 'probablement',
             'sans doute', 'apparemment']

consequence = ['donc', 'aussi', 'partant', 'alors', 'ainsi', 'par conséquent', 'si bien que', "d'où",
               'en conséquence', 'conséquemment', 'par suite', "c'est pourquoi", 'de sorte que', 'en sorte que',
               'de façon que', 'de manière que', 'si bien que', 'tant et']

classification = ["d'abord", "tout d'abord", 'en premier lieu', 'premièrement', 'en deuxième lieu', 'deuxièmement',
                  'après', 'ensuite', 'de plus', 'quant à', 'en troisième lieu', 'puis', 'en dernier lieu',
                  'pour conclure', 'enfin']

explication = ['savoir', 'à savoir', "c'est-à-dire", 'soit']

liaison = ['alors', 'ainsi', 'aussi', "d'ailleurs", 'en fait', 'en effet', 'de surcroît', 'de même', 'également',
           'puis', 'ensuite']

opposition = ['mais', 'cependant', 'or', 'en revanche', 'alors que', 'pourtant', 'par contre', 'tandis que',
              'néanmoins', 'au contraire', 'pour sa part', "d'un autre côté", 'en dépit de', 'malgré', 'au lieu de']

restriction = ['cependant', 'toutefois', 'néanmoins', 'pourtant', 'mis à part', 'ne@que', 'en dehors de', 'hormis',
               'à défaut de', 'excepté', 'sauf', 'uniquement', 'simplement']

temps = ['quand', 'lorsque', 'comme', 'avant que', 'après que', 'alors que', 'dès lors que', 'tandis que',
         'depuis que', 'en même temps que', 'pendant que', 'au moment où']

connecteurs = [addition, alternative, but, cause, comparaison, concession, consequence, conclusion, condition,
               classification,
               explication, liaison, opposition, restriction, temps]
connecteurs_names = ['addition', 'alternative', 'but', 'cause', 'comparaison', 'concession', 'consequence',
                     'conclusion', 'condition', 'classification', 'explication', 'liaison', 'opposition',
                     'restriction', 'temps']

doubles_starters = {'non seulement': 'mais encore', 'soit': 'soit', 'tantôt': 'tantôt', 'ou': 'ou',
                    'seulement': 'mais encore', "l'un": "l'autre", "d'un côté": "de l'autre", 'aussi': 'que',
                    'si': 'que',
                    'ne': 'que'}

phrase = "La prolifération de la culture sur brûlis a largement dégradé la forêt ivoirienne alors que le Gabon a plus à craindre de l'ouverture de son couvert forestier à l'exploitation industrielle du bois."


def sentence_to_list(sentence):
    wordList = [re.sub('^[{0}]+|[{0}]+$'.format(string.punctuation), '', w) for w in sentence.split()]
    lowercase_words = [word.lower() for word in wordList]
    return [sentence.lower(), lowercase_words]


sentence = sentence_to_list(phrase)[0]


def test_connecteur(word):
    word_categories = []
    for category_idx in range(len(connecteurs)):
        if word in connecteurs[category_idx]:
            word_categories.append(connecteurs_names[category_idx])
    return word_categories


dictionary_connecteurs = {}

# Création du dictionnaire
for category_idx in range(len(connecteurs)):

    for connecteur in connecteurs[category_idx]:

        if connecteur not in dictionary_connecteurs.keys():
            dictionary_connecteurs[connecteur] = [connecteurs_names[category_idx]]
        else:
            dictionary_connecteurs[connecteur].append(connecteurs_names[category_idx])


def detection(str):
    found_connectors = {}
    for connecteur in dictionary_connecteurs.keys():
        if connecteur in str:
            if connecteur in sentence_to_list(str)[1] or ' ' in connecteur:
                found_connectors[connecteur] = dictionary_connecteurs[connecteur]

    for starter in doubles_starters.keys():

        if starter == doubles_starters[starter]:
            new_str = str.replace(starter, '', 1)

        elif starter != doubles_starters[starter]:
            new_str = str


        if starter in str and doubles_starters[starter] in new_str:
            full_connector = starter + '@' + doubles_starters[starter]
            found_connectors[full_connector] = dictionary_connecteurs[full_connector]

        if 'ou' not in sentence_to_list(str)[1] and "ou@ou" in found_connectors.keys():
            del found_connectors["ou@ou"]

        if 'si' not in sentence_to_list(str)[1] and "si@que" in found_connectors.keys():
            del found_connectors["si@que"]

        if 'ne' not in sentence_to_list(str)[1] and "ne@que" in found_connectors.keys():
            del found_connectors["ne@que"]

    return found_connectors


print(detection(sentence))
# print(dictionary_connecteurs)
