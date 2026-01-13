# Student Exam Performance Prediction System

A complete end-to-end Machine Learning web application that predicts a student’s **Maths score** based on demographic details and prior academic performance.  
The project follows an **industry-style ML pipeline architecture** and is deployed using **Flask**.

##  Project Overview

This system predicts the **Maths score** of a student using the following inputs:

- Gender  
- Race / Ethnicity  
- Parental Level of Education  
- Lunch Type  
- Test Preparation Course  
- Reading Score  
- Writing Score  

A trained Machine Learning regression model and a preprocessing pipeline are saved as artifacts and reused during prediction.


## Tech Stack

### Programming & Machine Learning
- Python  
- NumPy  
- Pandas  
- Scikit-learn 

### Backend & Deployment
- Flask  
- Pickle (Model & Preprocessor serialization)

### Frontend
- HTML  
- CSS  


## Working of Project

### 🔹 Training Pipeline
- Data ingestion from CSV files  
- Data preprocessing and feature engineering  
- Model training using CatBoost Regressor  
- Saving trained model and preprocessor as `.pkl` files  

### 🔹 Prediction Pipeline
- User inputs data through a web form  
- Input is converted to a Pandas DataFrame  
- Preprocessing pipeline transforms the input  
- Model predicts Maths score  
- Result is displayed on the web page  


## How to Run the Project

- 1 Clone the repository

- 2 Create and activate virtual environment

- 3 Install Depenencies (using the 'requirements.txt' file)

- 4 Run the Flask application

- 5 open http://127.0.0.1:5000/predictdata in browser
