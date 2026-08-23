# Student Exam Score Prediction Based on Habits and Lifestyle Factors

This project applies machine learning regression techniques to predict a student's exam score using selected academic, lifestyle, and behavioral factors such as study hours, attendance, sleep duration, social-media usage, mental-health rating, and part-time employment.

# Motivation

Students' academic performance can be influenced by several factors beyond classroom learning. Understanding how measurable habits and lifestyle factors relate to exam performance can provide useful insights into academic outcomes.

The motivation of this project is to explore these relationships through data analysis and build machine learning models capable of estimating exam scores from selected student-related factors.

# Problem Definition

The objective is to develop a regression-based machine learning model that predicts a student's exam score using selected behavioral and lifestyle features.

Target variable: exam_score

Selected predictors:

Study hours per day
Attendance percentage
Sleep hours
Social media hours
Mental health rating
Part-time job status

The project also compares multiple regression algorithms and uses hyperparameter tuning to identify the better-performing model.

# Dataset

The project uses the Student Habits and Academic Performance dataset.

The dataset contains student-related academic, lifestyle, and behavioral attributes along with their examination scores.

The initial analysis includes:

Dataset structure and data types
Missing-value analysis
Duplicate-value checking
Descriptive statistics
Categorical-variable distributions
Correlation analysis
Feature-wise relationships with exam scores
Methodology

Data Collection → Data Understanding → Data Cleaning → Exploratory Data Analysis → Feature Selection → Encoding → Train-Test Split → Model Training → Hyperparameter Tuning → Evaluation → Model Selection → Deployment

For categorical data, LabelEncoder is used for the selected part_time_job feature.

The dataset is divided into 80% training and 20% testing data.

# Machine Learning Models

Three regression algorithms are currently compared:

Linear Regression
Decision Tree Regression
Random Forest Regression

For Decision Tree and Random Forest models, GridSearchCV with 5-fold cross-validation is used to search through selected hyperparameter combinations.

# Model Evaluation

The models are evaluated using two regression metrics:

RMSE (Root Mean Squared Error)
Measures the magnitude of prediction errors, with larger errors receiving greater weight. Lower RMSE indicates better performance.

R² Score
Measures how much of the variation in exam scores is explained by the model. Higher R² indicates better performance.

The models are compared using both metrics rather than relying on a single performance measure.

# Model Selection

The model with the lowest RMSE is selected as the best-performing model.

The selected model is then retrained on the complete available feature-target dataset and saved as:

best_model.pkl

The saved model is subsequently used by the Streamlit application.

# Web Application

A Streamlit application was developed to provide an interactive interface for the trained model.

The user provides:

Study hours per day
Attendance percentage
Mental health rating
Sleep hours
Social media hours
Part-time job status

After clicking Predict Exam Score, the application uses the trained model to estimate the examination score.

# Technology Stack

Programming: Python

Data Analysis: Pandas, NumPy

Data Visualization: Matplotlib, Seaborn

Machine Learning: Scikit-learn

Model Persistence: Joblib

Web Application: Streamlit

Development Environment: Google Colab

Version Control: GitHub

# Learning Outcomes

Through this project, I gained practical experience in:

Exploratory data analysis
Data cleaning and preprocessing
Feature selection
Categorical encoding
Regression modelling
Train-test splitting
Hyperparameter tuning using GridSearchCV
Cross-validation
Regression model evaluation
Comparing multiple ML algorithms
Saving and loading trained models
Building an ML-powered web application

# Future Improvements

Potential improvements include:

Testing additional regression algorithms
More systematic feature engineering
Implementing a Scikit-learn preprocessing pipeline
More extensive hyperparameter optimization
Adding additional regression metrics such as MAE
Model interpretability and feature-importance analysis
Testing the model on additional student datasets
Improving the Streamlit interface and input validation

# Development & Acknowledgement

The project was independently developed as an academic machine learning project. Reference materials and tutorials were used during the learning and development process, while the implementation, analysis, model evaluation, and application development were adapted and developed as part of the project workflow.

# Project Structure
student-academic-performance-prediction/
│
├── notebook.ipynb
├── app.py
├── best_model.pkl
├── requirements.txt
└── README.md
