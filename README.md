# Demystifying ML

This repository contains the relative files and codes for the 4 th and final project at
the UofT Data Analytics course. The main goal of this project is to build and compare 
models that can accurately predict if an individual has Diabetes given a set of information.   

## Dataset

The models are trained on two seperate datasets as the goal is to assess the performance
of these models and find and exp    lore the datasets and it's limitations. Both datasets are available on 
[Kaggle Datasets Page](https://www.kaggle.com/datasets).
* A csv format dataset containing data such as Pregnancies, Glucose, BloodPressure, SkinThickness, 
Insulin, BMI, DiabetesPedigreeFunction, Age and our target column, Outcome of around 2000 individuals.
* Another csv file with features such as gender, age, hypertension, heart_disease, smoking_history,bmi, 
HbA1c_level, blood_glucose_level with our target column being diabetes. It contains 100000 data points gathered from
different individuals.

## Models

### First model

For our First model, we chose to use the first dataset. It was chosen based on a function that compares different algorithms and shows the best accuracy score depending on the dataset it recieves. 

#### Tasks

1. Evaluating our dataset to get a better understanding of it's distribution.
2. Processing the necessary culumns and scaling our data.
2. Defining a function that compares different algorithms to find the best one matching the dataset.
3. Evaluating the result and defining our final Model for Diabetes predictions.

#### Summary of model
After data evaluation and processing using Pandas, We passed our scaled training data to a function that fits the dataset to some chosen algorithms such as Logistic_regression, Decision Tree, RandomForest and and indicates which model can give us the best accuracy. On this dataset, Random Forest had the highest score amognst the models so we chose it for o the final model to make predictions based on the datasets input features that it recieves.

![Scores](static/First_model_scores.png)


#### Libraries used

```ruby
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

#### Algorithms tested

```ruby
from sklearn.model_selection import train_test_split, GridSearchCV, ShuffleSplit
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
```

### Second model

For Our second model, we chose another dataset with a much more data point. We wanted to use a DNN (deep Neural Network) to get the predictions on our dataset. On this dataset, our NN takes 15 features and gives a binary output to predict Diabetes.

#### Taks

1. Check and assess the dataset to make sure of it's validation
2. Process the data using column manipulation to prepare and scaling our data.
3. Define a Neural Network that can identify if a patiant has Diabetes or not.
4. Change model parameters and explore different metrics to get the highest performance of accuracy and tune our model
5. Repeat the process with our first dataset to compare

#### Summary of model
Since our project was to focus on predicting diabetes, We wanted to get our recall to be as high as possible when calculating the Confusion matrix. Our first attempts gave us a 97% accuracy with a recall or 64% on our testing dataset. Pictures of it's performance during the process and tuning are available in the static folder.


#### Libraries used
```ruby
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pandas as pd
import tensorflow as tf
import keras_tuner as kt
import numpy as np
import pandas as pd
```




