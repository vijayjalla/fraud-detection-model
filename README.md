# Fraud Detection Model

This repository contains the implementation of a fraud detection model using Python. The project includes preprocessing, feature scaling, model training, and evaluation of a machine learning model to detect fraudulent transactions.

## Features
- **Dataset Preprocessing**: Standardizes the `Amount` and `Time` columns and handles missing values.
- **Model**: Trains a Random Forest classifier to predict fraudulent transactions.
- **Evaluation**: Provides detailed evaluation metrics like precision, recall, F1-score, and ROC-AUC.

## Repository Structure
```
fraud-detection/
├── README.md               # Project overview
├── fraud_detection.py      # Python script for model training
├── requirements.txt        # Python dependencies
```

## How to Use
### Clone the Repository
```bash
git clone https://github.com/your-username/fraud-detection.git
cd fraud-detection
```

### Install Dependencies
Install the required libraries using:
```bash
pip install -r requirements.txt
```

### Dataset
This script uses the `creditcard.csv` dataset. You can download it from [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud) and place it in the appropriate path. Update the file path in the script:
```python
data = pd.read_csv('/path/to/creditcard.csv')
```

### Run the Model
Run the following command to train and evaluate the model:
```bash
python fraud_detection.py
```

## Evaluation Metrics
- **Confusion Matrix**: Displays the performance of the model in predicting fraud.
- **Classification Report**: Includes precision, recall, F1-score for both fraud and non-fraud classes.
- **ROC-AUC Score**: Measures the ability of the model to distinguish between fraud and non-fraud transactions.

## Dependencies
The project uses the following Python libraries:
```
numpy>=1.21.0
pandas>=1.3.0
scikit-learn>=1.0
joblib>=1.1.0
matplotlib>=3.4.0
faker>=8.12.0
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
- Dataset: [Credit Card Fraud Detection Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- Library: [scikit-learn](https://scikit-learn.org/)
