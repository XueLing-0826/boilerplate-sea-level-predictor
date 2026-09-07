import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])
    
    # Create first line of best fit
    result = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    slope = result.slope
    intercept = result.intercept
    years = range(1880, 2051)
    prd_levels = [slope * x + intercept for x in years]
    plt.plot(years, prd_levels)

    # Create second line of best fit
    data = df[df['Year']>= 2000]
    result2 = linregress(data['Year'],data['CSIRO Adjusted Sea Level'])
    slope2 = result2.slope
    intercept2 = result2.intercept
    years2 = range(2000, 2051)
    prd_levels2 = [slope2 * x + intercept2 for x in years2]
    plt.plot(years2, prd_levels2)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()