import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    n = 1000
    theta = np.array([0, 0])
    x = np.random.uniform(0, 1, (n, 2))
    x[:, 1] = 1
    y = x.dot(theta) + np.random.normal(0, 0.2, n)


    def f(x, theta):
        return x.dot(theta)

    def least_square_error(theta):
        return sum((y - x.dot(theta))**2)

    def least_square_error_derivative(theta):
        return -2 * sum((y - f(x, theta))[:, np.newaxis] * x)

    def sgd(theta0, n_iterations=100, step_size=0.01, precision=0.1,
            verbose=False):
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
    
    theta_estimate = sgd(np.array([0, 1]), verbose=True)
    print(f'{theta} VS {theta_estimate}')


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
