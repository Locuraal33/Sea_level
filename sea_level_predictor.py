import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Import the data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=10, color='blue', alpha=0.5)

    # Use linregress to get the slope and y-intercept of the line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create a line of best fit
    years_extended = pd.Series([i for i in range(1880, 2051)])
    sea_levels_extended = intercept + slope * years_extended

    plt.plot(years_extended, sea_levels_extended, color='red', label='Best fit line (all data)')

    # Use data from year 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    # Create a line of best fit for recent data
    sea_levels_recent = intercept_recent + slope_recent * years_extended

    plt.plot(years_extended, sea_levels_recent, color='green', label='Best fit line (2000 onwards)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True)

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

    # Show the plot
    plt.show()

    # Save the plot to a PNG file
    plt.savefig('plot.png')
    plt.close()

draw_plot()