📊 Project Overview
The goal of this project is to develop a predictive model that can estimate the annual medical insurance cost ($) for a new customer. This is a Regression problem in supervised learning.

The dataset includes several features such as age, BMI, number of children, and smoking status, which significantly impact the final insurance quote.

🧠 Machine Learning Workflow
1. Data Exploratory Analysis (EDA)
Correlation Analysis: Identified that smoking status and BMI are the strongest predictors of high insurance costs.

Distribution Check: Analyzed the skewness of charges and age groups.

2. Feature Engineering
Categorical Encoding: Converted non-numeric data (Sex, Smoker, Region) into numerical values using Label Encoding and One-Hot Encoding.

Data Scaling: Normalized features to ensure the model treats all variables with equal importance.

3. Model Implementation
I experimented with multiple regression algorithms to find the highest accuracy:

Linear Regression: Baseline model for simple relationships.

Random Forest Regressor: Used for capturing non-linear patterns (achieved high performance).

XGBoost: Applied for advanced gradient boosting optimization.

🛠️ Tech Stack
Language: Python 3.x

Libraries:

Pandas & NumPy: For data manipulation and cleaning.

Scikit-Learn: For model training, splitting data, and evaluation.

Matplotlib & Seaborn: For generating heatmaps and distribution plots.

Pickle: For saving the trained model (rf_tuned.pkl).

📈 Model Performance
The final model was evaluated using the following metrics:

R-squared (R²) Score: Measures how well the model explains the variance.

Mean Absolute Error (MAE): Average error in the dollar amount predicted.

🚀 How to Run locally
Navigate to the directory:

Bash

cd "Main Project/Medical-Cost-Prediction Project"
Install requirements:

Bash

pip install -r requirements.txt
Run the Analysis:
Open the Jupyter Notebook to see the step-by-step training:

Bash

jupyter notebook "Medical Cost Insurance.ipynb"
Predict using the Web App:

Bash

python app.py
Developed by Albin Joy
