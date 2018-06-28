# Computational investing with Python
# Measures of Risk Adjusted Return
# Source: http://www.turingfinance.com/computational-investing-with-python-week-one/
# Implements the following classes:
#                                       1. Volatility
#                                       2. Expected Shortfall (Errors)
# Resources:
#               1. seaborn Plots: https://seaborn.pydata.org/tutorial/distributions.html


# Imports
import numpy
import numpy.random as nrand
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy.integrate as int
import seaborn as sns
import matplotlib.pyplot as plt


# Volatility Class
class Volatility:

    # Constructor
    def __init__(self, dummy):
        self.dummy = dummy

    # Sort return values if needed
    def arrange(self, returns):
        return numpy.sort(returns)


    # Calculate mean
    def avg(self, returns):
        return numpy.mean(returns)


    # Calculate Probability Density Function
    def pdf(self, returns):
        pdf = stats.norm.pdf(returns, self.avg(returns), self.vol(returns))
        return pdf


    # Plot the Distribution Curve using MatPlotLib
    def plotdistribution(self, returns):
        plt.plot(returns, self.pdf(returns))
        plt.show()

    # Plot Distribution Curve using Seaborn - Way better!
    def snsplotdistribution(self, returns):
        sns.set(color_codes=True)
        sns.distplot(returns)
        plt.show()
        # For random returns array uncomment the following
        # numpy.random.seed(sum(map(ord, "distributions")))
        # x = numpy.random.normal(size=100)
        # sns.distplot(x)
        # plt.show()

    # Calculate standard deviation of returns
    # The standard deviation is used to express risk/ volatility
    # It measures the variance of the returns from the mean return, over a period of time
    #                   Variance: Average of the squared returns
    def vol(self, returns):
        return numpy.std(returns)


    # Calculate beta
    # Measure the relationship between the security returns and the market.
    # Higher the beta - higher the risk and V.V
    def beta(self, returns, market):
        # Create a matrix of [returns, market]
        m = numpy.matrix([returns, market])
        # Return the covariance of m divided by the standard deviation of the market returns
        return numpy.cov(m)[0][1] / numpy.std(market)


class ExpectedShortfall:

    def __init__(self, returns):
        self.returns = returns

    def var(self, alpha):
        # This method calculates the historical simulation var of the returns
        sorted_returns = numpy.sort(self.returns)
        # Calculate the index associated with alpha
        index = int(alpha * len(sorted_returns))
        # VaR should be positive
        return abs(sorted_returns[index])

    def cvar(self, alpha):
        # This method calculates the condition VaR of the returns
        sorted_returns = numpy.sort(self.returns)
        # Calculate the index associated with alpha
        index = int(alpha * len(sorted_returns))
        # Calculate the total VaR beyond alpha
        sum_var = sorted_returns[0]
        for i in range(1, index):
            sum_var += sorted_returns[i]
        # Return the average VaR
        # CVaR should be positive
        return abs(sum_var / index)


# Volatility Operations
volObj = Volatility(0)           # Volatility Object Instantiation
r = nrand.uniform(-1, 1, 50)
m = nrand.uniform(-1, 1, 50)
print("vol =", volObj.vol(r))
print("beta =", volObj.beta(r, m))
# volObj.plotdistribution(r)
volObj.snsplotdistribution(r)

# ExpectedShortfall Operations
r = nrand.uniform(-1, 1, 50)
esObj = ExpectedShortfall(r)
print("VaR(0.05) =", esObj.var(0.05))
print("CVaR(0.05) =", esObj.cvar(0.05))
