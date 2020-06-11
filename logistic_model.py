import numpy as np
import matplotlib.pyplot as plt
from math import *
from time import time
import nltk


# opinion_lexicon : dataset where each word appears only once

def word_frequencies_dictionary():
    wordlist = nltk.corpus.brown.words()
    # wordlist = nltk.corpus.opinion_lexicon.words()
    dico = {}
    for word in wordlist:
        if word in dico.keys():
            dico[word] += 1
        else:
            dico[word] = 1
    total = len(wordlist)
    frequencies = {}
    for word in dico.keys():
        frequencies[word] = dico[word] * 100 / total
    print(total)
    print(frequencies)
    return dico


def generate_random_dataset(n, alpha, beta):
    dataset = np.array([(0., 0.)] * n)

    for k in range(n):
        xk = np.random.uniform(0, 1)

        p_1 = 1 / (1 + exp(-alpha * xk - beta))
        if p_1 < 0.5:
            yk = -1
        else:
            yk = 1

        dataset[k] = (xk, yk)

    return dataset


def generate_dataset(alpha, beta):
    dict_frequencies = word_frequencies_dictionary()
    n = len(dict_frequencies)

    dataset = np.array([(0., 0.)] * n)
    k = 0

    max_xk = 0
    for word in dict_frequencies:
        xk = dict_frequencies[word]
        if xk > max_xk:
            max_xk = xk

    for word in dict_frequencies:
        xk = dict_frequencies[word] / max_xk

        p_1 = 1 / (1 + exp(-alpha * xk - beta))
        if p_1 < 0.5:
            yk = -1
        else:
            yk = 1

        dataset[k] = (xk, yk)
        k += 1

    print(dataset)
    return dataset


def f_logistic_loss(dataset, alpha, beta):
    n = np.size(dataset, 0)
    s = 0

    for k in range(n):
        xk, yk = dataset[k]
        s += log(1 + exp(-yk * (alpha * xk + beta)))

    return s


def df_logistic_loss(dataset, alpha, beta):
    n = np.size(dataset, 0)
    s = 0

    for k in range(n):
        xk, yk = dataset[k]
        s += - (yk * xk * exp(-yk * (alpha * xk + beta))) / (1 + exp(-yk * (alpha * xk + beta)))

    return s


def gradient_descent_alpha(dataset, alpha_0, beta, step_multiplier, minimal_step, nb_iter_max):
    new_alpha = alpha_0
    step = minimal_step + 1
    i = 0

    while i < nb_iter_max and abs(step) > minimal_step:
        last_alpha = new_alpha
        step = - step_multiplier * df_logistic_loss(dataset, last_alpha, beta)
        new_alpha = last_alpha + step
        i += 1
        print("iteration :", i, "\t\tstep :", step, "\t\tnew_alpha :", new_alpha)

    return new_alpha


def test_gradient_descent_alpha(n, alpha_to_guess, alpha_0, beta, step_multiplier, minimal_step, nb_iter_max,
                                is_random):
    if is_random:
        dataset = generate_random_dataset(n, alpha_to_guess, beta)
    else:
        dataset = generate_dataset(alpha_to_guess, beta)
        n = np.size(dataset, 0)

    t_begin = time()
    alpha_guessed = gradient_descent_alpha(dataset, alpha_0, beta, step_multiplier, minimal_step, nb_iter_max)
    t_end = time()
    computing_time = t_end - t_begin

    print("=========================================================================================")
    print("step_multiplier :", step_multiplier, "\tminimal_step :", minimal_step, "\tnb_iter_max :", nb_iter_max)
    print("number of (xk,yk) couples :", n, "\tbeta :", beta)
    print("alpha_to_guess :", alpha_to_guess, "\talpha_guessed :", alpha_guessed)
    print("error between alpha_guessed and alpha_to_guess :", abs(alpha_guessed - alpha_to_guess))
    print("computing_time :", computing_time)
    print("=========================================================================================")

    return 0


# Tests
# n, alpha_to_guess, alpha_0, beta, step_multiplier, minimal_step, nb_iter_max, is_random

# test_gradient_descent_alpha(10, 100, 150, -50, 0.01, 0.00001, 100, True)
test_gradient_descent_alpha(0, 100, 150, -10, 50, 0.000001, 100, False)
# test_gradient_descent_alpha(1000, 100, 150, -10, 1, 0.000001, 100, True)
