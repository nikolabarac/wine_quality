# Wine Quality Prediction Project

## Overview

This project focuses on predicting the quality of wines on a scale from 0 to 10. The main objectives include exploring the dataset, performing exploratory data analysis (EDA), splitting the dataset into train and test sets in a stratified manner, and building a predictive model.

## Project Steps

### Experimentation and Dataset Exploration:

- An experiment Python file was created to try various operations on the dataset.
- Initial exploration included understanding the features, data types, and distribution of the wine quality scores.
  
### Stratified Train-Test Split:

- Split the dataset into training and testing sets in a stratified way.
- Ensured that every quality score had the same percentage representation in both sets.

### Exploratory Data Analysis (EDA):

- Conducted EDA to gain insights into the dataset.
- Explored correlations, plotted histograms, boxplots, and feature distributions.
- Identified patterns and relationships among features.

### Best Model Identification:

- Explored various regression models to identify the best-performing one.
- Evaluated models such as Random Forest, Gradient Boosting, SVR, Linear Regression, Ridge Regression, Lasso Regression, Elastic Net, K-Nearest Neighbors, Decision Tree, AdaBoost, Bagging, Extra Trees, and XGBoost.
- Identified Extra Trees as the best-performing algorithm based on cross-validated mean negative mean squared error.

### Results Visualization:

- Visualized the mean negative mean squared error for each regressor using a bar chart.

### Hyperparameter Tuning:

- Performed hyperparameter tuning on the best model (Extra Trees) using cross-validated grid search.
- Found the optimal hyperparameters for the Extra Trees regressor.

### Model Testing:

- Tested model on test set get RMSE result: 0.5171

### Model Export:

- Exported the best model (Extra Trees) using the joblib library for future use.
