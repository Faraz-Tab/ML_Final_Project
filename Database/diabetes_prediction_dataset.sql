CREATE TABLE patient_data (
    id SERIAL PRIMARY KEY,
    gender VARCHAR(255),
    age INT,
    hypertension INT,
    heart_disease INT,
    smoking_history VARCHAR(255),
    bmi DECIMAL(5, 2),
    HbA1c_level DECIMAL(4, 1),
    blood_glucose_level INT,
    diabetes INT
);

