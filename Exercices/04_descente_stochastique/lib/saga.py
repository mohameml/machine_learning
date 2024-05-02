"""
Functions specific to SAGA
TODO (5)
"""

from typing import Optional, Tuple, Callable
import numpy as np


def initialize_gradients_buffer(n: int, d: int) -> np.ndarray:
    # ####### TODO (5) ########
    return np.zeros((n ,d))


def saga_stepsize_start(
    n: int,
    mu: float,
    L: float
) -> float:
    """
    A function to choose the starting step-size of the algorithm, i.e. its step-size for the first iteration.

    Parameters
    ----------
    n: int
        number of samples of the data distribution
    mu: float
        strong-convexity constant of the objective function
    L: float
        (Approximate ?) Lipschitz constant of the gradient of the objective.
    """
    # ####### TODO (5) ########

    return 1/(2*(mu*n + L))


def saga_stepsize(it: int, start: float) -> float:
    """
    A function to choose the step-size of the algorithm depending on the current iteration number.

    Parameters
    ----------
    it: int
        current iteration number
    start: float
        first-iteration step-size chosen
    """
    # ####### TODO (5) ########
    return start /(1+ np.sqrt(it))
    

def saga_step(
    x: np.ndarray,
    grad: Callable[[np.ndarray, Optional[int]], np.ndarray],
    prox: Callable[[np.ndarray, float], np.ndarray],
    stepsize: float,
    gradients_buffer: np.ndarray
) -> Tuple[np.ndarray, np.ndarray]:
    """
    This function performs the step of this SAGA algorithm.
    Starting at ``x`` with a buffer ``gradients_buffer`` containing n past gradients, it outputs the next state of the algorithm as a 2-uple containing the next state and the updated buffer.
    """
    # ####### TODO (5) ########
    n = gradients_buffer.shape[0]
    i_rand =  np.random.randint(1 , n)
    grad_f_i = grad(x , i_rand)
    mean_grad = sum([alpha for alpha in gradients_buffer])/n
    x_suiv  = prox(x - stepsize*(grad_f_i - gradients_buffer[i_rand] + mean_grad) , stepsize)
    gradients_buffer[i_rand] = grad_f_i 
    return (x_suiv , gradients_buffer)
