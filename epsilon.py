import numpy as np

theta_hat = [0, 0, 0]
count = [0, 0, 0]
N = 6000
Epsilon = [0.2, 0.4, 0.6, 0.8]
Theta_j = [0.6, 0.8, 0.5]
for epsilon in Epsilon:
    experiment_result = [0]
    for i in range(1, 200):# 200 independent runs
        total = 0
        for t in range(0, N):
            ## random choose from 1,2,3
            randomly_chosen = np.random.choice([1, 2, 3])
            ## arg max theta hat j
            arg_max = np.argmax(theta_hat) + 1

            I_t = np.random.choice([arg_max, randomly_chosen], p =[1 - epsilon, epsilon])
            count[I_t - 1] = count[I_t - 1] + 1
            ## sampling
            r = np.random.choice([1, 0], p = [Theta_j[I_t - 1], 1 - Theta_j[I_t - 1]])
            total = total + r
            ##
            theta_hat[I_t - 1] = theta_hat[I_t - 1] + (1/count[I_t - 1]) * (r - theta_hat[I_t-1])
        experiment_result.append(total)
    experiment_result.pop(0)
    expectation = np.mean(experiment_result)
    print ( "epsilon = ", epsilon, "Expectation = ", expectation)