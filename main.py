print("hello world")
from scipy.stats import binom
import numpy.random as rd
import numpy
import matplotlib.pyplot as plt

data_size = 1000
alpha = 3
mu = 0
sigma = 0.01

beta = rd.uniform(-1, 1)
x_values = numpy.zeros(data_size)
for index in range(data_size):
    x_values[index] = rd.uniform(0, 1)

error = rd.normal(mu,sigma)
y = alpha * x_values + beta + error
# y_float = alpha * x_values + beta + error
# for idx in range(len(y_float)) :
#     y_float[idx] = numpy.sign(y_float[idx])
# y = y_float

data_base = []
for idx in range(data_size):
    data_base.append((x_values[idx], y[idx]))
#print(data_base)

next_alpha = 0  # We start the search at x=0
gamma = 1  # Step size multiplier
precision = 0.000001  # Desired precision of result
max_iters = 10000  # Maximum number of iterations


def err_fun(alpha,beta,data_base,data_size):
    sum = 0
    for i in range(data_size):
        iteration = (data_base[i][1]-alpha*data_base[i][0]-beta)**2
        sum += iteration
    return sum


# Derivative function
def depsilon(alpha,beta,data_base,data_size):
    sum = 0
    for j in range(data_size) :
        iteration = alpha*(data_base[j][0])**2 + data_base[j][0]*(beta - data_base[j][1])
        sum += iteration
    sum = 2 * sum
    return sum / data_size


for _ in range(max_iters):
    current_alpha = next_alpha
    next_alpha = current_alpha - gamma * depsilon(current_alpha,beta,data_base,data_size)

    step = next_alpha - current_alpha
    if abs(step) <= precision:
        break

alpha_list = numpy.arange(0,6,0.01)
error_list = []
for k in alpha_list:
    error_list.append(err_fun(k,beta,data_base,data_size))


print("Minimum at ", next_alpha)

plt.plot(alpha_list,error_list)
plt.show()
