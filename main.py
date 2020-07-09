import numpy as np
import matplotlib.pyplot as plt
from nltk.corpus import brown
from linalgo.client import LinalgoClient

token = "e5a30d4fa8b0b52a0513363c5582a214deb255b4"

api_url = 'https://api.linalgo.com/hub'
linalgo_client = LinalgoClient(token=token, api_url=api_url)
task = linalgo_client.get_task('4a2c20e3-64af-4a9f-9fc8-5e703dd7a835')

if __name__ == '__main__':

    # n = 1000
    theta = np.array([1, -0.5])


    # x = np.random.uniform(0, 1, (n, 2))
    # x[:, 1] = 1
    # y = x.dot(theta) + np.random.normal(0, 0.2, n)

    # To create a dictionary with the words as keys and the frequencies as definitions
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
        return frequencies


    # To gather documents and annotations from LinHub
    dataset = []
    n = len(task.documents)

    for word in range(n):
        # print(word)
        annotations_list = task.documents[word].annotations
        if len(annotations_list) != 0:
            # print(word,type(annotations_list))
            x = task.documents[word].content
            y_raw = task.documents[word].annotations[0]
            y = task.get_name(str(y_raw))
            dataset.append((x, y))
    # print(dataset)

    # Remplacement des X par les fréquences et des Y par les -1 ou 1
    x_formatted = []
    y_formatted = []
    brown_dict = create_dico()

    IK = 'I know this word'
    IDK = "I don't know this word"

    for couple in dataset:
        x, y = couple[0], couple[1]
        if x in brown_dict.keys():
            x_freq = brown_dict[x]
            if y == IK:
                y_bool = 1
            else:
                y_bool = -1
            x_formatted.append(x_freq)
            y_formatted.append(y_bool)

    n_effectif = len(x_formatted)
    print(n_effectif)
    x = np.zeros((n_effectif, 2))
    print(x_formatted)
    x[:, 0] = x_formatted
    x[:, 1] = 1
    y = y_formatted


    def f(x, theta):
        return x.dot(theta)


    # computes the MRS of y and x
    def least_square_error(theta):
        return sum((y - x.dot(theta)) ** 2) / n


    # computes the derivative of the MRS
    def least_square_error_derivative(theta):
        return -2 * sum((y - f(x, theta))[:, np.newaxis] * x) / n


    def gradient_descent(theta0, n_iterations=100, step_size=0.000001,
                         precision=0, verbose=False):
        current_theta = theta0
        for i in range(n_iterations):
            derivative = least_square_error_derivative(current_theta)
            next_theta = current_theta - step_size * derivative
            if verbose:
                print(f'iter #{i} - error = {least_square_error(next_theta)}')
            step = next_theta - current_theta
            if np.sqrt(step.dot(step)) < precision:
                break
            current_theta = next_theta
        return current_theta


    theta_estimate = gradient_descent(np.array([0.5, 1]), verbose=True)
    #print(f'{theta} VS {theta_estimate}')
    print(theta_estimate)

    # n = 1000
    # alpha = 3
    # mu = 0
    # sigma = 0.01

    # for _ in range(max_iters):
    #     current_alpha = next_alpha
    #     next_alpha = current_alpha - gamma * depsilon(current_alpha, beta, data_base, n)

    #     step = next_alpha - current_alpha
    #     if abs(step) <= precision:
    #         break

    # def depsilon(alpha,beta,data_base,data_size):
    #     sum = 0
    #     for j in range(data_size) :
    #         iteration = alpha*(data_base[j][0])**2 + data_base[j][0]*(beta - data_base[j][1])
    #         sum += iteration
    #     sum = 2 * sum
    #     return sum / data_size

    # def err_fun(alpha, beta, data_base, data_size):
    #     sum = 0
    #     for i in range(data_size):
    #         iteration = (data_base[i][1]-alpha*data_base[i][0]-beta)**2
    #         sum += iteration
    #     return sum

    # error = np.random.normal(mu,sigma)
    # y = alpha * x + beta + error
    # # y_float = alpha * x_values + beta + error
    # # for idx in range(len(y_float)) :
    # #     y_float[idx] = np.sign(y_float[idx])
    # # y = y_float

    # data_base = []
    # for idx in range(n):
    #     data_base.append((x[idx], y[idx]))
    # #print(data_base)

    # next_alpha = 0  # We start the search at x=0
    # gamma = 1  # Step size multiplier
    # precision = 0.000001  # Desired precision of result
    # max_iters = 10000  # Maximum number of iterations

    # def err_fun(alpha, beta, data_base, data_size):
    #     sum = 0
    #     for i in range(data_size):
    #         iteration = (data_base[i][1]-alpha*data_base[i][0]-beta)**2
    #         sum += iteration
    #     return sum

    # # Derivative function
    # def depsilon(alpha,beta,data_base,data_size):
    #     sum = 0
    #     for j in range(data_size) :
    #         iteration = alpha*(data_base[j][0])**2 + data_base[j][0]*(beta - data_base[j][1])
    #         sum += iteration
    #     sum = 2 * sum
    #     return sum / data_size

    # for _ in range(max_iters):
    #     current_alpha = next_alpha
    #     next_alpha = current_alpha - gamma * depsilon(current_alpha, beta, data_base, n)

    #     step = next_alpha - current_alpha
    #     if abs(step) <= precision:
    #         break

    # alpha_list = np.arange(0,6,0.01)
    # error_list = []
    # for k in alpha_list:
    #     error_list.append(err_fun(k, beta, data_base, n))

    # print("Minimum at ", next_alpha)

    # plt.plot(alpha_list,error_list)
    # plt.show()
