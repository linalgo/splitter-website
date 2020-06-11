import numpy as np
import matplotlib.pyplot as plt
from time import time
import nltk


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
    return frequencies


def probability_y(x, y, theta):  # array of P( Y=y[k] | x[k] )
    return 1 / (1 + np.exp(-y*x.dot(theta)))


def generate_y(x, theta):
    return np.sign(2/(1 + np.exp(-x.dot(theta))) - 1)


def generate_random_x(n, theta):
    x = np.random.uniform(0, 1, (n, 2))
    x[:, 1] = 1
    return x


def generate_real_x(n, theta):
    dict_frequencies = word_frequencies_dictionary()
    n = min(n, len(dict_frequencies))
    x = np.array([[0., 1.]]*n)

    k = 0
    for word in dict_frequencies:
        x[k, 0] = dict_frequencies[word]
        k += 1
        if k == n:
            break
    return x


def logistic_error(x, y, theta):
    return - np.sum(np.log(probability_y(x, y, theta)))


def logistic_error_gradient(x, y, theta):
    return - np.sum((y*(1 - probability_y(x, y, theta)))[:, np.newaxis] * x, axis=0)


def gradient_descent(x, y, theta_0, learning_rate=0.1, n_iterations=100, history=False, verbose=False):
    if history:
        theta_history = np.array([[0., 0.]]*(n_iterations+1))
        theta_history[0] = theta_0
        error_history = np.array([0.]*(n_iterations+1))
        error_history[0] = logistic_error(x, y, theta_0)

    theta = theta_0

    for i in range(1, n_iterations+1):
        step = - learning_rate * logistic_error_gradient(x, y, theta)
        theta = theta + step
        if verbose:
            print("iteration :", i, "\t\tstep :", step, "\t\ttheta :", theta, "\t\terror :", logistic_error(x, y, theta))
        if history:
            theta_history[i] = theta
            error_history[i] = logistic_error(x, y, theta)

    if history:
        return theta_history, error_history
    else:
        return theta


def logistic_accuracy(x_test, y_test, theta_guessed, nb_tests=100):
    n = np.size(y_test)
    id_words_tested = np.random.randint(n, size=nb_tests)
    x_test = np.take(x_test, id_words_tested, axis=0)
    y_test = np.take(y_test, id_words_tested)
    y_guessed = generate_y(x_test, theta_guessed)
    return np.sum((y_test*y_guessed + 1)/(2*nb_tests))




if __name__ == '__main__':
    choose_generation_x = "real_data"

    theta_t = np.array([100, -20])

    n_t = 10000
    if choose_generation_x == "random":
        x_t = generate_random_x(n_t, theta_t)
    elif choose_generation_x == "real_data":
        x_t = generate_real_x(n_t, theta_t)
        n_t = np.size(x_t, axis=0)
    y_t = generate_y(x_t, theta_t)

    theta_0_t = np.array([200, -70])

    # print(theta_t)
    # print(x_t[:10, 0])
    # print(y_t[:10])
    # print(probability_y(x_t, y_t, theta_t+np.array([0, 85]))[:10])
    # print(logistic_error(x_t, y_t, theta_t))
    # for i in range(-10,11):
    #     print(i, logistic_error_gradient(x_t, y_t, theta_0_t+np.array([0, i])))

    theta_estimate = gradient_descent(x_t, y_t, theta_0_t, verbose=True)
    print(f'==========================================================================')
    print(f'theta VS theta_estimate : {theta_t} VS {theta_estimate}')
    print(f'Ratio alpha/beta for theta VS theta_estimate :')
    print(f'{theta_t[0]/theta_t[1]} VS {theta_estimate[0]/theta_estimate[1]}')
    print(f'Logistic_error with theta VS theta_estimate :')
    print(f'{logistic_error(x_t, y_t, theta_t)} VS {logistic_error(x_t, y_t, theta_estimate)}')
    print(f'Logistic error with theta*1000 : {logistic_error(x_t, y_t, theta_t*1000)}')
    print(f'Accuracy with theta_estimate on (x_t,y_t): {logistic_accuracy(x_t, y_t, theta_t)}')
    print(f'==========================================================================')

