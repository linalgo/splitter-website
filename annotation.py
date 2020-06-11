import spacy
import re
import matplotlib.pyplot as plt
import numpy as np
import csv


def contains_punctuation(string):
    for symbol in ['.', ',', '?', '(', ')', '!', ':', ';', '%', '@', '"', '<', '>', '/', '--']:
        if symbol in string:
            return True
    return False


nlp = spacy.load("en_core_web_sm")

text_list = ["wlp_acad.txt", "wlp_blog.txt", "wlp_fic.txt", "wlp_mag.txt", "wlp_news.txt", "wlp_spok.txt",
             "wlp_tvm.txt", "wlp_web.txt"]

f = open(text_list[1], "r")


freq_globales = {}
lemmas = {}

file = f.read()
lines = file.split("\n")
words = []
word_counter = 0

for line in lines[1:-1]:
    new_line = line.split("\t")
    word = new_line[1]

    if not contains_punctuation(word) and re.search(r"\d", word) is None:
        words.append(word)
        word_counter += 1

        if word in freq_globales.keys():
            freq_globales[word] += 1
        else:
            freq_globales[word] = 1


# Useful to know what the word repartition is
tranches = [0] * 10
for i in freq_globales.keys():
    freq = freq_globales[i]
    floor = freq // 5
    if freq < 50:
        tranches[floor] += 1
print(tranches)
# ===============================================================================

# ==================THIS IS THE PURGEEEE========================================== #
# Now, within the [1,5] frequency (adaptable depending on the corpora), we keep only 1/100 of the words.
# Similarly, we keep 1/10 of the words in [5,10], and so on.


counter_1000 = 0
counter_100 = 0
counter_50 = 0
counter_40 = 0
counter_30 = 0
counter_30_2 = 0
counter_30_3 = 0
to_be_removed = []

for word in freq_globales.keys():

    if 0 < freq_globales[word] <= 5:
        counter_1000 += 1
        if counter_1000 != 999:
            to_be_removed.append(word)
        else:
            counter_1000 = 0

    elif 5 < freq_globales[word] <= 10:
        counter_100 += 1
        if counter_100 != 99:
            to_be_removed.append(word)
        else:
            counter_100 = 0

    elif 10 < freq_globales[word] <= 15:
        counter_50 += 1
        if counter_50 != 49:
            to_be_removed.append(word)
        else:
            counter_50 = 0

    elif 15 < freq_globales[word] <= 20:
        counter_40 += 1
        if counter_40 != 39:
            to_be_removed.append(word)
        else:
            counter_40 = 0

    elif 20 < freq_globales[word] <= 25:
        counter_30 += 1
        if counter_30 != 29:
            to_be_removed.append(word)
        else:
            counter_30 = 0

    elif 25 < freq_globales[word] <= 30:
        counter_30_2 += 1
        if counter_30_2 != 29:
            to_be_removed.append(word)
        else:
            counter_30_2 = 0

    elif 35 < freq_globales[word] <= 40:
        counter_30_3 += 1
        if counter_30_3 != 29:
            to_be_removed.append(word)
        else:
            counter_30_3 = 0

# Après avoir tag les mots à enlever, on purge tout.

for word in to_be_removed:
    del freq_globales[word]

tranches = [0] * 10
for i in freq_globales.keys():
    freq = freq_globales[i]
    floor = freq // 5
    if freq < 50:
        tranches[floor] += 1
print(tranches)

# Useful to know what the word repartition is
tranches = [0] * 10
for i in freq_globales.keys():
    freq = freq_globales[i]
    floor = freq // 50
    if freq < 500:
        tranches[floor] += 1
print(tranches)
# ============================================


longueur = len(freq_globales.keys())

lemmas = []
count = 0
for word in freq_globales.keys():
    lemma = nlp(word)[0].lemma_
    if lemma not in lemmas:
        lemmas.append(lemma)
    count += 1
    print(count, "/", longueur)

while '-PRON-' in lemmas:
    lemmas.remove('-PRON-')
print(lemmas)

################################FICHIER CSV###############################################

row_counter = 1
row_list = [["uri", "content"]]

for word in lemmas:
    row_list.append([row_counter, word])
    row_counter += 1

with open('vocab_annotation.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)
