# src/controls.py

import numpy as np
from js import updateChart
from pyodide import create_proxy, to_js
from distributions import normal_distribution_fx, lognormal_distribution_fx
import matplotlib.pyplot as plt

# for plotly
import plotly
import plotly.express as px
import json
import js

# get selectors for the scale and for the distribution --> get all parameters
range1 = document.querySelector("#range1")
range2 = document.querySelector("#range2")
select_distribution = document.querySelector("#select-distribution")


def on_range_update(event):
    """
    Update plots if the scaler changes
    """
    label = event.currentTarget.nextElementSibling
    label.innerText = event.currentTarget.value
    plot_distribution()


def selected_distribution(event):
    """
    Update plot if the selection changes
    """
    plot_distribution()


def plot_distribution():
    """
    Based on the selection, plot the given distribution.
    Plot in all three possible ways -- using js, matplotlib and plotly

    """
    mu = float(range1.value)
    sigma = float(range2.value)

    # new - check what distribution the user chose
    choice = document.getElementById("select-distribution").value
    # print('Here we say: ', choice)
    # get the distribution
    if choice == 'normal':
        x, y = normal_distribution_fx(mu, sigma)
    elif choice == 'lognormal':
        x, y = lognormal_distribution_fx(mu, sigma)
    # print what we chose
    pyscript.write("selected-choice", choice)

    # old
    # # get the distribution
    # x, y = normal_distribution_fx(mu, sigma)

    fig, _ = plt.subplots()
    plt.plot(x, y, linewidth=2, color='r')
    # Element("panel").write(fig)
    pyscript.write("chart1", fig)

    # with js
    updateChart(to_js(x), to_js(y))

    # with plotly
    plot_plotly(x,y)


def plot_plotly(x,y):
    fig = px.line(x=x, y=y, width=800, height=400)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    js.plot(graphJSON, "chart2")


# add proxy and listener for the scale bar
proxy = create_proxy(on_range_update)
range1.addEventListener("input", proxy)
range2.addEventListener("input", proxy)

# add proxy and listener for distribution change
change_proxy = create_proxy(selected_distribution)
select_distribution.addEventListener("change", change_proxy)


# initialise the first plot
plot_distribution()


# Add the part with selecting and inserting specific values
from distributions import cdf_normal


def run(*args, **kwargs):
    entered_mu = Element("enter-mu")
    entered_sigma = Element("enter-sigma")
    mu = float(entered_mu.value)
    sigma = float(entered_sigma.value)
    pyscript.write("entered-values", f"values: mu: {mu}, sigma: {sigma}")
    plot_cdf(mu, sigma)


def plot_cdf(mu, sigma):
    x = np.linspace(0, 1, 100)
    y = cdf_normal(x, mu, sigma)

    fig, _ = plt.subplots()
    plt.plot(x, y, linewidth=2, color='k')
    # Element("panel").write(fig)
    pyscript.write("plot-error", fig)