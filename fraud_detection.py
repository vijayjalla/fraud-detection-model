# -*- coding: utf-8 -*-
"""fraud_detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NFhOxo6XxRqIwrmZkBBCG5NQJyK_dMet
"""

# fraud_detection_model.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler

# Load the dataset
data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/creditcard.csv')  # Replace with your dataset path
print(data.head())
scaler = StandardScaler()
data[['amount', 'time']] = scaler.fit_transform(data[['Amount', 'Time']])

# Preprocess data
X = data.drop(columns=['Class'])  # Features
y = data['Class']  # Target

# Identify numeric columns
numeric_columns = X.select_dtypes(include=[np.number]).columns

# Fill missing values for numeric columns only
X[numeric_columns] = X[numeric_columns].fillna(X[numeric_columns].median())

# Handle missing values
X.fillna(X.median(), inplace=True)

X_scaled = scaler.fit_transform(X)


# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nROC-AUC Score:")
print(roc_auc_score(y_test, model.predict_proba(X_test)[:, 1]))