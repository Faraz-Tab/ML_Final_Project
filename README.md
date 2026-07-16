# Demystifying ML — Diabetes Prediction

Capstone project building, tuning, and deploying machine learning models that predict diabetes from patient health indicators, across two datasets of very different scale.

*Team capstone project.*

## Datasets (Kaggle)

1. **Pima-style dataset** (~2,000 records): glucose, blood pressure, BMI, insulin, pregnancies, diabetes pedigree, age
2. **Large-scale dataset** (100,000 records): demographics, hypertension, heart disease, smoking history, HbA1c, blood glucose

## Models

**Model 1 — Classical ML (dataset 1).** A model-selection function benchmarks Logistic Regression, Decision Tree, Random Forest, and SVC with `GridSearchCV`. **Random Forest** scored highest and was serialized (`.pkl`) as the production model.

**Model 2 — Deep Neural Network (dataset 2).** TensorFlow/Keras binary classifier on 15 encoded features, tuned with `keras-tuner`. Because false negatives are the costly error in a medical screening context, tuning targeted **recall** rather than raw accuracy (baseline: 97% accuracy, 64% recall — iterations documented in `static/`).

## Deployment

Flask web app (`app.py` + HTML form) loads the pickled Random Forest and returns live predictions from user-entered health metrics.

```
pip install -r requirements.txt
python app.py   # runs at localhost:5000
```

**Tools:** Python · scikit-learn · TensorFlow/Keras · keras-tuner · Flask · pandas · seaborn
