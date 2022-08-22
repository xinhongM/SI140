import numpy as np

theta_hat = [0, 0, 0]
count = [0, 0, 0]
N = 6000
Theta_j = [0.8, 0.6, 0.5]
c = 0#
Cs = [2, 6, 9]
for c in Cs:
    experiment_result = [0]
    for i in range(1, 200):
        total = 0
        for t in {1, 2, 3}:
            I_t = t
            count[I_t - 1] = 1
            ## sampling
            r = np.random.choice([1, 0], p=[Theta_j[I_t - 1], 1 - Theta_j[I_t - 1]])
            total = total + r
            theta_hat[I_t - 1] = r
        for t in range(4, N):
            I_t = np.argmax(theta_hat + c * np.sqrt(2 * np.log(t)/count)) + 1
            count[I_t - 1] = count[I_t - 1] + 1
            ## sampling
            r = np.random.choice([1, 0], p=[Theta_j[I_t - 1], 1 - Theta_j[I_t - 1]])
            total = total + r

            theta_hat[I_t - 1] = theta_hat[I_t - 1] + (1/count[I_t - 1]) * (r - theta_hat[I_t-1])
        experiment_result.append(total)
    experiment_result.pop(0)
    expectation = np.mean(experiment_result)
    print("c = ", c, "   Expectation = ", expectation)