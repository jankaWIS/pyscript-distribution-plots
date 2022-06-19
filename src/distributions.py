# src/distributions.py

import numpy as np
import matplotlib.pyplot as plt
from scipy import special

def normal_distribution_fx(mu, sigma):
    """
    Generate samples of normal distribution, taken from numpy docs

    Parameters
    ----------
    mu: mean
    sigma: standard deviation

    Returns
    ----------
    bins (x) and y values
    """
    # sample the distribution
    s = np.random.normal(mu, sigma, 1000)

    # get the edges
    count, bins, ignored = plt.hist(s, 30, density=True)

    # evaluate the function
    y = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2))
    return bins, y


def lognormal_distribution_fx(mu, sigma):
    """
    Generate samples of lognormal distribution, taken from numpy docs
    Parameters
    ----------
    mu: mean
    sigma: standard deviation

    Returns
    ----------
    linspace of x based on bins and y values
    """
    # sample the distribution
    s = np.random.lognormal(mu, sigma, 1000)

    # get the edges
    count, bins, ignored = plt.hist(s, 100, density=True, align='mid')

    # evaluate the function
    x = np.linspace(min(bins), max(bins), 1000)
    y = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2)) / (x * sigma * np.sqrt(2 * np.pi)))
    return x, y


def cdf_normal(x, mu, sigma):
    return 0.5*(1 + special.erf((x - mu) / (sigma * np.sqrt(2))))