# ML Model Development Based on the Global COVID-19 Forecasting Dataset

## Description of the Project
As the result of the effort of the White House Office of Science and Technology Policy (OSTP) working together with coalition research groups and companies (including Kaggle) to prepare the COVID-19 Open Research Dataset (CORD-19) in order to address key open scientific questions on COVID-19, Kaggle launched a companion COVID-19 forecasting challenge to help answer a subset of those questions.

On the basis of Kaggle’s challenge, this project involves developing a machine learning model to predict the cumulative number of COVID-19 confirmed cases and the number of resulting fatalities across the world. The model also forecasts future trends, helping medical and governmental institutions prepare and adjust as pandemics unfold.

## Data Dictionary
The dataset includes the following fields:

* ID: Unique identifier for each row.
* County: The county within a specific country (e.g., US counties).
* Province_State: The province or state within a country where the data is reported (if applicable).
* Country_Region: The name of the country (e.g., Germany, France, Spain).
* Weight: A weight assigned to each row for calculating the competition's final score.
* Date: Timestamp for the respective row.
* Target: Placeholder indicating confirmed cases or fatalities.
* TargetValue: Actual count of confirmed cases or fatalities (target variable for prediction and forecasting).

## Results
### Supervised Machine Learning Models  

The **XGBoost model** demonstrated the best performance:  
- High accuracy (94%)
- Low Mean Squared Error (MSE).  

### Time Series Models  

**ARIMA** outperformed **SARIMA** in terms of:  
- Accuracy.  
- Prediction reliability. .

## Dataset
The dataset used for this project is publicly available on Kaggle: [COVID-19 Dataset by Sirio Libanês Hospital](https://www.kaggle.com/competitions/covid19-global-forecasting-week-5/data). 

