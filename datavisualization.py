# Molly Tran
# CS 87B
# Assignment 4 - Data Visualization
# 10/15/2023

import matplotlib.pyplot as plt
import numpy as np


# Function to create a bar chart
def bar_chart(city, rainfall_set1, rainfall_set2):
    # Create an array with the number of cities
    x = np.arange(len(city))

    # Plot the bars, offset one dataset 0.2 to the left and the second dataset 0.2 to the right
    plt.bar(x - 0.2, rainfall_set1, 0.4, label='Rainfall Set 1')
    plt.bar(x + 0.2, rainfall_set2, 0.4, label='Rainfall Set 2')

    # Label and title the chart, rotate x-ticks 90 degree
    plt.xticks(x, city, rotation='vertical', fontsize=7)
    plt.xlabel('City')
    plt.ylabel('Precipitation (Inches)')
    plt.title('Precipitation Between a 10-year Span (Bar Chart)')

    # Add legend, save, and display the chart
    plt.legend()
    plt.tight_layout()
    plt.savefig('bar_chart.jpg')
    plt.show()


# Function to create a line subplot
def line_subplot(city, rainfall_set1, rainfall_set2):
    # Create two subplots in a 2X1 grid
    fig, ax = plt.subplots(2)

    # Subplot 1
    ax[0].set_xlabel('City')
    ax[0].set_ylabel('Precipitation (Inches)')
    ax[0].set_title('Rainfall Set 1')
    ax[0].set_xticks(range(len(city)))
    ax[0].set_xticklabels(city, rotation=45, fontsize=5)
    ax[0].plot(city, rainfall_set1)

    # Find the max and min of dataset
    max_set1 = max(rainfall_set1)
    min_set1 = min(rainfall_set1)

    # Highlight the max and min of dataset using an annotation, with an arrow that points to that specific point
    ax[0].annotate(f'Max ({city[rainfall_set1.index(max_set1)]}, {max_set1:.2f})',
                   xy=(city[rainfall_set1.index(max_set1)], max_set1),
                   xytext=(city[rainfall_set1.index(max_set1)], max_set1 - 20),
                   arrowprops=dict(facecolor='red', shrink=0.1, width=0.1))
    ax[0].annotate(f'Min ({city[rainfall_set1.index(min_set1)]}, {min_set1:.2f})',
                   xy=(city[rainfall_set1.index(min_set1)], min_set1),
                   xytext=(city.index(city[5]), min_set1 + 10),
                   arrowprops=dict(facecolor='green', shrink=0.1, width=0.1))

    # Subplot 2
    ax[1].set_xlabel('City')
    ax[1].set_ylabel('Precipitation (Inches)')
    ax[1].set_title('Rainfall Set 2')
    ax[1].set_xticks(range(len(city)))
    ax[1].set_xticklabels(city, rotation=45, fontsize=5)
    ax[1].plot(city, rainfall_set2)

    # Find the max and min of dataset
    max_set2 = max(rainfall_set2)
    min_set2 = min(rainfall_set2)

    # Highlight the max and min of dataset using an annotation, with an arrow that points to that specific point
    ax[1].annotate(f'Max ({city[rainfall_set2.index(max_set2)]}, {max_set2:.2f})',
                   xy=(city[rainfall_set2.index(max_set2)], max_set2),
                   xytext=(city[rainfall_set2.index(max_set2)], max_set2 - 10),
                   arrowprops=dict(facecolor='red', shrink=0.1, width=0.2))
    ax[1].annotate(f'Min ({city[rainfall_set2.index(min_set2)]}, {min_set2:.2f})',
                   xy=(city[rainfall_set2.index(min_set2)], min_set2),
                   xytext=(city.index(city[7]), min_set2 + 5),
                   arrowprops=dict(facecolor='green', shrink=0.1, width=0.2))

    plt.tight_layout()
    plt.savefig('line_subplot.jpg')
    plt.show()


# Function to create a histogram chart
def histogram_chart(rainfall_set1, rainfall_set2):
    # Create two subplots in a 2X1 grid, share the same y-axis
    fig, ax = plt.subplots(2, sharey=True)

    # Create histogram with dataset and 5 bins, label and set title of chart
    ax[0].hist(rainfall_set1, bins=5, edgecolor='black')
    ax[0].set_xlabel('Precipitation (Inches)')
    ax[0].set_ylabel('Number of Cities')
    ax[0].set_title('Rainfall Set 1 (Histogram)')

    # Create histogram with dataset and 5 bins, label and set title of chart
    ax[1].hist(rainfall_set2, bins=5, edgecolor='black')
    ax[1].set_xlabel('Precipitation (Inches)')
    ax[1].set_ylabel('Number of Cities')
    ax[1].set_title('Rainfall Set 2 (Histogram)')

    plt.tight_layout()
    plt.savefig('histogram_chart.jpg')
    plt.show()


# Main function to read data from files and create visualizations
def main():
    # Open data files
    file_set1 = open('rainfallSet1.txt')
    file_set2 = open('rainfallSet2.txt')

    city = []
    rainfall_set1 = []
    rainfall_set2 = []

    # Parse data from files
    for row1 in file_set1:
        row1 = row1.split(' ')
        city.append(row1[0])
        rainfall_set1.append(float(row1[1]))

    for row2 in file_set2:
        row2 = row2.split(' ')
        rainfall_set2.append(float(row2[1]))

    # Create and save visualizations
    bar_chart(city, rainfall_set1, rainfall_set2)
    line_subplot(city, rainfall_set1, rainfall_set2)
    histogram_chart(rainfall_set1, rainfall_set2)


main()
