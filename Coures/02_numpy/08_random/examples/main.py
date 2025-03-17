import numpy as np
import matplotlib.pyplot as plt


def random_walk(n):
    res = [0]

    for _ in range(n):
        res.append(res[-1] + np.random.choice([-1, 1]))

    return res

def rep_random_walk(n, m):
    res = np.zeros((m, n + 1))

    for i in range(m):
        res[i] = random_walk(n)

    return res


def show_walks(walks , legend = False):
    for walk in walks:
        plt.plot(walk)
        plt.xlabel('Time')
        plt.ylabel('Position')
        plt.title('Random Walks')
        
    plt.show()

def main(n ,m , legend = False):
    walks = rep_random_walk(n, m )
    show_walks(walks , legend)


if __name__ == '__main__':
    n = 10
    m = 10

    # walks = rep_random_walk(n, m)
    # for walk in walks:
    #     plt.plot(walk)

    # plt.show()
    print(rep_random_walk(n, m))
