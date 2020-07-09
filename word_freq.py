from nltk.corpus import brown
from nltk.corpus import opinion_lexicon


# Pour opinion_lexicon, chaque mot apparaît une seule fois ; on trouve bien une fréquence identique de 0.0147% pour
# chaque mot.

def create_dico():
    wordlist = brown.words()
    # wordlist = opinion_lexicon.words()
    dico = {}
    for word in wordlist:
        word = word.lower()
        if word in dico.keys():
            dico[word] += 1
        else:
            dico[word] = 1
    total = len(wordlist)
    frequencies = {}
    for word in dico.keys():
        frequencies[word] = dico[word] * 100 / total
    return(dico)


#print(total)
#print(frequencies)
dictionnaire = create_dico()
print(dictionnaire["the"])
