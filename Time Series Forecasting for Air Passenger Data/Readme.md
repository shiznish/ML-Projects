
# Time Series Forecasting for Air Passenger Data

## Project Description
This project focuses on forecasting the number of air passengers over time using time series analysis techniques. The dataset contains monthly totals of international airline passengers from 1949 to 1960. The project explores various models to capture trends, seasonality, and residual patterns in the data.

## Dataset
The dataset used is the **AirPassengers.csv**, which contains:
- **Month**: The time period (e.g., Jan 1949, Feb 1949, etc.).
- **#Passengers**: The total number of passengers for the respective month.

## Methodology
1. **Exploratory Data Analysis (EDA)**:
   - Visualized trends, seasonality, and variability in the data.
   - Checked for stationarity using the Augmented Dickey-Fuller (ADF) test.
   - Performed seasonal decomposition to analyze trend, seasonality, and residuals.

2. **Data Transformation**:
   - Applied differencing to make the time series stationary.
   - Used second-order differencing to remove trend and stabilize variance.

3. **Modeling**:
   - Implemented and compared the following models:
     - **ARIMA (AutoRegressive Integrated Moving Average)**: Captures linear dependencies in the data.
     - **SARIMA (Seasonal ARIMA)**: Extends ARIMA to handle seasonality.
     - **AutoARIMA**: Automatically selects the best ARIMA parameters using grid search.
     - **Grid Search for SARIMA**: Performed exhaustive parameter tuning to find the best seasonal and non-seasonal orders.

4. **Evaluation**:
   - Evaluated model performance using **Root Mean Squared Error (RMSE)**.

## Results
### ARIMA Model
- Parameters: `(p=2, d=2, q=2)`
- Observations:
  - The model failed to capture seasonality effectively.
  - Predictions were not satisfactory.

### SARIMA Model
- Parameters: `(p=2, d=2, q=2)` with seasonal order `(P=1, D=0, Q=3, s=12)`
- RMSE: **28.79**
- Observations:
  - Successfully captured seasonality and trend.
  - Provided accurate forecasts for the test set and future periods.

### AutoARIMA
- Automatically selected parameters: `(p=0, d=1, q=0)` with seasonal order `(P=0, D=1, Q=0, s=24)`
- RMSE: **27.83**
- Observations:
  - Simplified the parameter selection process.
  - Achieved comparable performance to manually tuned SARIMA.


## Conclusion
The **AutoARIMA model** performed the best overall, achieving the lowest RMSE and providing the most accurate predictions. While SARIMA captured seasonality and trend effectively, AutoARIMA's automated parameter selection and superior performance make it the preferred model for this dataset.

## Future Work
- Incorporate external factors (e.g., economic indicators, fuel prices) to enhance forecasting accuracy.
- Explore advanced machine learning models like Prophet or deep learning-based approaches for time series forecasting.

