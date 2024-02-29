

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('D:/Python_e/wine_quality/winequality-red.csv')

df['quality'].value_counts()

df.columns

column_list = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
               'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
               'pH', 'sulphates', 'alcohol', 'quality']

# Set up subplots
fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(15, 12))
fig.suptitle('Histograms for Each Column', y=1.02)

# Flatten the 2D array of subplots into a 1D array
axes = axes.flatten()

# Plot histograms for each column
for i, column in enumerate(column_list):
    axes[i].hist(df[column], bins=20, color='skyblue', edgecolor='black')
    axes[i].set_title(column)
    axes[i].set_xlabel('Value')
    axes[i].set_ylabel('Frequency')

# Adjust layout
plt.tight_layout()
plt.show()

df.info()

import seaborn as sns

correlation_matrix = df.corr()
# Create a heatmap of the correlation matrix
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()