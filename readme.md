## Insurance Premium Prediction
### Demo Video:-
```bash
https://www.youtube.com/watch?v=ypIsFoGzY6o&t=7s
```



## Problem Statement:  
The goal of this project is to give people an estimate of how much they need based on 
their individual health situation. After that, customers can work with any health 
insurance carrier and its plans and perks while keeping the projected cost from our 
study in mind. This can assist a person in concentrating on the health side of an 
insurance policy rather han the ineffective part



## Dataset :
The dataset is taken from a Kaggle. You can download the dataset from [here](https://www.kaggle.com/noordeen/insurance-premium-prediction)

## Approach :
Applying machine learing tasks like Data Exploration, Data Cleaning, Feature Engineering, Model Building and model testing to build a solution that should able to predict the premium of the personal for health insurance.

- **Data Exploration :** Exploring the dataset using pandas, numpy, matplotlib, plotly and seaborn.
- **Exploratory Data Analysis :** Plotted different graphs to get more insights about dependent and independent variables/features.
- **Feature Engineering :** Numerical features scaled down and Categorical features encoded.
- **Model Building :** In this step, first dataset Splitting is done. After that model is trained on different Machine Learning Algorithms such as:
    1) Linear Regression
    2) Decision Tree Regressor
    3) Random Forest Regressor
    4) Gradient Boosting Regressor
    5) XGBoost Regressor
    
    

- **Model Selection :** Tested all the models to check the RMSE & R-squared.
- **Pickle File** : Selected model as per best RMSE score & R-squared and created pickle file using pickle library.
- **Webpage &Deployment :** Created a web application that takes all the necessary inputs from the user & shows the output. Then deployed project on the Heroku Platform.









## Usage:
```
To use the insurance premium prediction model:


* Ensure you have Python installed on your system.
* Install the necessary Python libraries specified in the requirements.txt file.
* Run the provided Python script (app.py) after providing the required input data.
* The script will output the predicted insurance premiums for the given input.
 ```
 
## Evaluation:

```
The performance of the prediction model is evaluated using metrics such as mean absolute error (MAE), mean squared error (MSE), and R-squared value on the test set.
These metrics provide insights into the accuracy and reliability of the model in predicting insurance premiums.
```


## Future Work:

```
Future enhancements to the insurance premium prediction model may include:
```


* Incorporating additional features such as medical history, occupation, or lifestyle factors.
* Fine-tuning hyperparameters of machine learning algorithms to improve prediction accuracy.
* Exploring advanced modeling techniques such as neural networks for more complex patterns in the data.
## Web Inerface :
![plate](./prediction.png)
## Libraries used :
    1) Pandas
    2) Numpy
    3) Matplotlib, Seaborn, Plotly
    4) Scikit-Learn
    5) Flask
    6) HTML
    7) CSS

## Technical Aspects :
    1) Python 
    2) Front-end : HTML, CSS
    3) Back-end : Flask
    4) Deployment : Heruko

## Contributors
ABHISHEK UAPDHYAY



Feel free to modify and use this README template according to your project's specific requirements!


