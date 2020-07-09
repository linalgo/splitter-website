import spacy
from spacy import displacy

nlp = spacy.load("fr_core_news_sm")
doc_present = nlp("Van Gogh s'aventure dans le delta et découvre le fameux village. "
                  "Ce peintre dessine la violence des flots et le reflet des voiles des bateaux."
                  "Vive le soleil qui donne une si belle lumière."
                  "La montagne se dresse, grise, bleue ou beige, mais toujours majestueuse comme au bout du ciel."
                  "Il part chercher le soleil à Arles."
                  "On ne sait toujours pas si c'est vert ou violet."
                  "Il peint le fameux tableau.")

doc_passe_compose = nlp("Je suis resté longtemps à regarder le ciel."
                        "Encore une fois, tu t'es trompée."
                        "J'ai retourné ma chaise et je l'ai placée comme celle du marchand de tabac, parce que j'ai "
                        "trouvé que c'était plus commode. "
                        "Ils ont fumé deux cigarettes ensemble."
                        "Le ciel s'est assombri et j'ai cru que nous allions avoir un orage d'été."
                        "Je suis resté longtemps à regarder la porte d'entrée."
                        "A cinq heures, des tramways sont arrivés dans le bruit.")

doc_imparfait = nlp("Il y avait un jeune dromadaire qui n'était pas content du tout."
                    "Voilà qu'il n'était pas d'accord parce que la conférence n'était pas du tout ce qu'il avait "
                    "imaginé. "
                    "Depuis une heure, un gros monsieur parlait."
                    "Nous ne nous lavions jamais les dents."
                    "Sa bosse le gênait beaucoup, elle frottait contre le dossier du fauteuil ; il était très mal "
                    "assis. "
                    "Toutes les cinq minutes, le conférencier répétait les mêmes paroles : c'était un beau discours.")

doc_plus_que_parfait = nlp("L'ingénieur s'était présenté en juin 1889 au concours de l'Ecole Polytechnique, "
                           "qu'il avait préparé pendant deux ans, à Paris. "
                           "Il n'avait pas été admis."
                           "Quand il avait annoncé son échec à sa mère, Eugénie Favart, elle l'avait giflé."
                           "Plutôt que d'y renoncer une deuxième fois, il s'était présenté, quasiment en cachette, "
                           "à un concours du ministère de l'agriculture et y avait participé.")

doc_passe_simple = nlp("Je cherai Arezki."
                       "Arezki fut là, tout à coup."
                       "Un grand Algérien de la chaîne qui s'appelait Lakhdar passa près de nous."
                       "Il tendit la main vers Arezki."
                       "Nous montâmes enfin et nous nous retrouvâmes écrasés l'un contre l'autre sur la plate-forme "
                       "de l'autobus. "
                       "Certains nous dévisagèrent."
                       "Nous nous faufilâmes vers l'angle à gauche où quelques chaises restaient vides.")

doc_futur_simple = nlp("Un vent violent de sud-ouest puis d'ouest soufflera du Finistère à la baie de Seine."
                       "Les rafales maximales atteindront 120 km/h sur le littoral nord."
                       "Ce vent sera plus contenu et ne dépassera pas 80 km/h."
                       "Tu feras bien attention, hein ?"
                       "Vous me ferez ce devoir pour demain."
                       "Si tu viens me chercher, on ira au cinéma.")

doc_futur_anterieur = nlp("Lorsqu'ils auront bien crié, ils iront souper avec plus d'appétit."
                          "C'est promis, j'aurai tapé ce document avant la fin de la semaine."
                          "Elle aura fini son travail plus tôt que de coutume."
                          "Nous aurons attendu 20 ans pour que ce talent soit enfin reconnu."
                          "On partira dès que vous aurez fini la vaisselle."
                          "Vous aurez une meilleure idée quand vous aurez lu le rapport.")

doc_cond_present = nlp("L'automobile arriverait dans l'avenue par une étroite rue perpendiculaire."
                       "Il fallait donc que celui qui surveillerait la petite rue, dès qu'il verrait l'auto, "
                       "fit signe aux deux autres. "
                       "Mon ami préviendrait et lancerait la première bombe."
                       "Puis, son compagnon attendrait qu'il soit sorti pour passer à l'action.")

doc_cond_passe = nlp("Je me serais suicidée sur commande, étant enfant d'une secte."
                     "J'ai réalisé que j'aurais, moi aussi, pu arriver à l'heure si je n'étais pas si happé par ma "
                     "lecture. "
                     "Cela aurait très bien pu être le cas."
                     "Ceux qui auraient lancé les fusées n'ont pas eu le droit de se défendre au tribunal."
                     "S'il avait eu assez d'argent, il nous aurait acheté une glace.")

doc_subj_present = nlp("Bien que de multiples raisons puissent justifier la présence ici de cet enfant, je m'étonne "
                       "qu'il traîne ainsi, dans la rue. "
                       "J'ai peur que mon indiscrétion ne lui paraisse étrange, qu'il ne s'en alarme."
                       "C'est impossible que le même nom soit utilisé pour deux rues différentes de la même vile."
                       "Il faut donc que je confonde avec un autre nom de rue.")

doc_subj_passe = nlp("Je suis content qu'il ait fini sa thèse."
                     "Il est possible qu'elle soit déjà arrivée."
                     "Je regrette que nous n'ayons pas pu assister à la réunion d'hier."
                     "Voulez-vous que je vous ait dit cela plus tôt ?"
                     "A moins qu'ils ne soient déjà partis, je crains d'avoir été obligé de les inviter ce soir.")

for token in doc_futur_simple:
    if (token.pos_ == 'VERB') or (token.pos_ == 'AUX'):
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_)
    # print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_)
