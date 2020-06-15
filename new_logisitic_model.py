import numpy as np
import matplotlib.pyplot as plt
from time import time
import nltk
from linalgo.client import LinalgoClient


def word_frequencies_dictionary():
    wordlist = nltk.corpus.brown.words()
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
    return frequencies


def probability_y(x, y, theta):  # array of P( Y=y[k] | x[k] )
    return 1 / (1 + np.exp(-y*x.dot(theta)))


def generate_y(x, theta):
    return np.sign(2/(1 + np.exp(-x.dot(theta))) - 1)


def generate_random_x(n):
    x = np.random.uniform(0, 1, (n, 2))
    x[:, 1] = 1
    return x


def generate_real_x(n):
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


def get_task_from_linhub(user_token,task_token):
    api_url = 'https://api.linalgo.com/hub'
    linalgo_client = LinalgoClient(token=user_token, api_url=api_url)
    task = linalgo_client.get_task(task_token)
    return task


def generate_dataset_from_linhub():
    user_token = 'de5ad853895399f71319da06dfaf4bd1165b47e5'
    task_token = '4a2c20e3-64af-4a9f-9fc8-5e703dd7a835'
    task = get_task_from_linhub(user_token, task_token)

    dict_frequencies = word_frequencies_dictionary()

    documents = task.documents
    n = len(documents)
    x = []
    y = []

    for k in range(n):
        annotations_list = documents[k].annotations

        if len(annotations_list) == 0:
            break

        word = documents[k].content
        if word in dict_frequencies:
            xk = dict_frequencies[word]
        else:
            xk = 0.
        x.append(xk)

        label = task.get_name(str(annotations_list[0]))
        if label == "I know this word":
            yk = 1
        else:
            yk = -1
        y.append(yk)

    n = len(x)
    x = np.array([[x[k], 1.] for k in range(n)])
    y = np.array([y[k] for k in range(n)])
    return x, y




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


def logistic_accuracy(x_test, y_test, theta_guessed, nb_tests=100, verbose=False):
    n = np.size(y_test)
    id_words_tested = np.random.randint(n, size=nb_tests)
    x_test = np.take(x_test, id_words_tested, axis=0)
    y_test = np.take(y_test, id_words_tested)
    y_guessed = generate_y(x_test, theta_guessed)

    if verbose:
        print("#test - real y - guessed y")
        for k in range(nb_tests):
            print(f'{k}\t{y_test[k]}\t{y_guessed[k]}')

    return np.sum((y_test*y_guessed + 1)/(2*nb_tests))




if __name__ == '__main__':
    choose_generation_x = "linhub_data"

    # theta = np.array([100, -20])
    # theta_0 = np.array([50, -50])
    theta = np.array([100, 1])
    theta_0 = np.array([100, 1])

    n = 10000
    if choose_generation_x == "random":
        x = generate_random_x(n)
        y = generate_y(x, theta)
    elif choose_generation_x == "dummy_data":
        x = generate_real_x(n)
        n = np.size(x, axis=0)
        y = generate_y(x, theta)
    elif choose_generation_x == "linhub_data":
        x, y = generate_dataset_from_linhub()
        n = np.size(x, axis=0)

    # print(theta)
    print(x[:100, 0])
    # print(y[:10])
    # print(probability_y(x, y, theta+np.array([0, 85]))[:10])
    # print(logistic_error(x, y, theta))
    # for i in range(-10,11):
    #     print(i, logistic_error_gradient(x, y, theta_0+np.array([0, i])))

    theta_estimate = gradient_descent(x, y, theta_0, verbose=True)

    if choose_generation_x == "random" or choose_generation_x == "dummy_data":
        print(f'==============================================================================')
        print(f'y is generated with (x,theta) then the model guesses theta_estimate from (x,y)')
        print(f'dataset size : {n}   initial theta : {theta_0}')
        print(f'theta VS theta_estimate : {theta} VS {theta_estimate}')
        print(f'Ratio alpha/beta for theta VS theta_estimate :')
        print(f'{theta[0]/theta[1]} VS {theta_estimate[0]/theta_estimate[1]}')
        print(f'Logistic_error with theta VS theta_estimate :')
        print(f'{logistic_error(x, y, theta)} VS {logistic_error(x, y, theta_estimate)}')
        print(f'Logistic error with theta*1000 : {logistic_error(x, y, theta*1000)}')
        print(f'Accuracy with theta_estimate on (x,y): {logistic_accuracy(x, y, theta, verbose=False)}')
        print(f'==============================================================================')

    elif choose_generation_x == "linhub_data":
        print(f'==============================================================================')
        print(f'(x,y) is extracted from linhub and the model guesses theta_estimate from (x,y)')
        print(f'dataset size : {n}   initial theta : {theta_0}')
        print(f'theta_estimate : {theta_estimate}')
        print(f'Accuracy with theta_estimate on (x,y): {logistic_accuracy(x, y, theta, verbose=False)}')
        print(f'==============================================================================')

        # Note: For now the only words that have been labelled unknown on linhub
        #       are those not appearing in the nltk corpus used. This means the
        #       optimal model is the one always saying "I know the word"


