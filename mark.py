#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

NUM_PORTFOLIOS = 10000000
NUM_STOCKS = 20
SHEET_NAME = 'returns'
RISK_FREE_RATE = .00119
FILE_NAME = 'mark_2.xlsx'
# Turn off progress printing
#solvers.options['show_progress'] = False


def read_returns(xl_file, sheet ):
    df = pd.read_excel(xl_file, engine='openpyxl', sheet_name=sheet)
    df = df.drop(columns=['Date'])
    return df


def rand_weights(n):
    ''' Produces n rancdom weights that sum to 1 '''
    k = np.random.rand(n)
    return k / sum(k)


def find_optimal_risky(means, stds, weights):
    sharp_return = 0
    sharp_std = 0
    sharp_rat = -1000000000
    sharp_weight = []
    for x, y, z in zip(means, stds, weights):
        if (x-RISK_FREE_RATE)/y > sharp_rat:
            sharp_return = x
            sharp_std = y
            sharp_rat = (x-RISK_FREE_RATE)/y
            sharp_weight = z
    return sharp_return, sharp_std, sharp_weight


def rand_portfolio_stats(data_frame):

    cov = np.asmatrix((data_frame.cov()).to_numpy())
    avg = np.asmatrix((data_frame.mean()).to_numpy())
    weights = np.asmatrix(rand_weights(NUM_STOCKS))
    #print(weights,file=sys.stderr)
    portfolio_avg = avg * weights.T
    sigma = np.sqrt(weights * cov * weights.T)
    # if (sigma > 5 or portfolio_avg < -1 or portfolio_avg > 1):
    #     return rand_portfolio_stats(data_frame)
    return portfolio_avg, sigma, weights


def main():
    df = read_returns(FILE_NAME, SHEET_NAME)

    means = []
    stds = []
    weights = []
    for x in range(NUM_PORTFOLIOS):
        mean, std, weight = rand_portfolio_stats(df)
        means.append(mean.item(0))
        stds.append(std.item(0))
        weights.append(weight)
        if(x%10000 == 0):
            print(x, file=sys.stderr)
    opt_mean, opt_std, opt_weights = find_optimal_risky(means, stds, weights)
    fig = plt.figure()
    plt.plot(stds, means, 'o', markersize=5)
    plt.plot(opt_std, opt_mean, 'ro')
    plt.plot()
    plt.xlabel('std')
    plt.ylabel('mean')
    plt.title('Mean and standard deviation of returns of randomly generated portfolios')
    y = 0
    sum_weights = 0
    for col in df.columns:
        print(col, ((opt_weights.item(y))*100),'%')
        sum_weights+=opt_weights.item(y)
        y+=1
    print(sum_weights)
    print("-----------------------")
    plt.show()


if __name__ == "__main__":
    main()






