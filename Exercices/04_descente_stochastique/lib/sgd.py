"""
Functions specific to
Stochastic Gradient Descent
"""

from typing import Optional, Tuple, Callable
import numpy as np


def sgd_stepsize_start(
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
    # ####### TODO (4) ########
    # beta = (1/mu) + 1
    # gamma = L*(mu +1 ) / mu**2
    # return beta / gamma
    return 1/(2*(mu*n + L))


def sgd_stepsize(it: int, start: float) -> float:
    """
    A function to choose the step-size of the algorithm depending on the current iteration number.

    Parameters
    ----------
    it: int
        current iteration number
    start: float
        first-iteration step-size chosen
    """
    # ####### TODO (4) ########
    return start/(1 + np.sqrt(it))



def sgd_step(
    x: np.ndarray,
    grad: Callable[[np.ndarray, Optional[int]], np.ndarray],
    prox: Callable[[np.ndarray, float], np.ndarray],
    stepsize: float,
    n : int 
) -> Tuple[np.ndarray]:
    """
    This function performs the step of this Stochastic Gradient Descent algorithm.
    Starting at ``x``, it outputs the next state of the algorithm as a 1-uple containing the next state.
    
     # on a ajouter n : dataset-size 
    """
    # ####### TODO (4) ########
    return (x - grad(x , np.random.randint(1 , n))*stepsize , )
