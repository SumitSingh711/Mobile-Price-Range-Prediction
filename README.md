<h1>Mobile Price Range Prediction Project</h1>

This project focuses on predicting the price range of mobile phones based on various technical features.
You can access the mobile price range predictor web application [here](https://mobile-price-range-prediction-tquanbngnsmgqz6gejkcnd.streamlit.app/). Enter the technical specifications of a mobile phone (RAM, battery, etc.) to get an estimate of its price range.

<h3>Objective</h3>
The goal of this project is to categorize mobile phones into one of four distinct price ranges:

<ul>
<li>Low cost</li>
<li>Medium cost</li>
<li>High cost</li>
<li>Very high cost</li>
</ul>
By analyzing different technical specifications of mobile phones, the model predicts the price category, enabling users to estimate the price range based on the phone's features.

<h3>Approach</h3>
<h4>1. Data Exploration and Preprocessing</h4>
The project started with an in-depth exploration and cleaning of the dataset. Preprocessing steps included:

Handling missing values and outliers.
Encoding categorical variables where needed.
Scaling numerical features to ensure proper model performance.
Key features used in this prediction model include:

Battery Power
RAM
Internal Memory
Screen Size
Pixel Resolution
Camera Quality
Mobile Weight
These features were preprocessed to ensure they were in a form that machine learning models could effectively learn from.

<h4>2. Model Selection and Training</h4>
Multiple machine learning algorithms were applied to classify mobile phones into one of the four price categories. These algorithms include:

Random Forest Classifier
Support Vector Machine (SVM)
Logistic Regression
K-Nearest Neighbors (KNN)
Decision Tree
The performance of each model was assessed using various evaluation metrics, such as:

Accuracy
Precision
Recall
F1 Score
Cross-validation was applied to ensure the model's stability and avoid overfitting.

<h4>3. Model Deployment</h4>
The final model, which turned out to be a Logistic Regression, was deployed as an interactive web application using Streamlit. Users can input various mobile specifications (such as RAM, battery, and memory) and receive real-time predictions on the mobile's price range.

<h4>4. Evaluation</h4>
The models were evaluated using the following metrics:

Accuracy: The overall correctness of predictions.
Precision: How many selected items were relevant.
Recall: How many relevant items were selected.
F1 Score: The balance between precision and recall.

<h4>5. Key Features</h4>
Interactive Web Application: The application allows users to input mobile features and get an instant prediction of the price range.
Cross-Validation: Ensured the model's performance is consistent across different data subsets.
Real-Time Prediction: The app offers instant results based on user inputs.

<h3>Conclusion</h3>
This project demonstrates the potential of machine learning in price prediction tasks. By analyzing mobile phone features, the model can predict the price range, offering practical utility for consumers and businesses alike. The end-to-end approach—from data preprocessing to model deployment—highlights the power of machine learning in real-world applications.

<h3>Technologies Used</h3>
Python
Pandas, NumPy for data handling and preprocessing
Scikit-learn for implementing machine learning models
Streamlit for deploying the app
Matplotlib, Seaborn for data visualization
