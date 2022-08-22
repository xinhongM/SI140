import numpy as np

theta_hat = [0, 0, 0]
count = [0, 0, 0]
N = 6000
Theta_j = [0.8, 0.6, 0.5]
alpha_betaS = [[[1, 1], [1, 1], [1, 1]], [[601, 401], [401, 601], [2, 3]]]
for alpha_beta in alpha_betaS:
    experiment_result = [0]
    for i in range(1, 200):
        total = 0
        for t in range(1, N):
            for j in [1, 2, 3]:
                theta_hat[j - 1] = np.random.beta(alpha_beta[j - 1][0], alpha_beta[j - 1][1])
            I_t = np.argmax(theta_hat) + 1
            ## sampling
            r = np.random.choice([1, 0], p=[Theta_j[I_t - 1], 1 - Theta_j[I_t - 1]])
            total = total + r

            alpha_beta[I_t - 1][0] = alpha_beta[I_t - 1][0] + r
            alpha_beta[I_t - 1][1] = alpha_beta[I_t - 1][1] + 1 - r

        experiment_result.append(total)
    experiment_result.pop(0)
    expectation = np.mean(experiment_result)
    print("(alpha, beta) = ", alpha_beta, "   Expectation = ", expectation)

