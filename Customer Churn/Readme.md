# Customer Churn Prediction

This project focuses on predicting customer churn using machine learning techniques. The goal is to identify customers who are likely to leave a service or subscription, enabling proactive retention strategies.

## Features

- **Exploratory Data Analysis (EDA):** Understands customer behavior and key factors influencing churn.
- **Data Preprocessing:** Handles missing values, encodes categorical variables, and scales features.
- **Model Building:** Implements and compares various machine learning models (e.g., Logistic Regression, Decision Trees, Random Forest, XGBoost).
- **Model Evaluation:** Uses metrics such as accuracy, precision, recall, F1-score, and ROC-AUC to assess performance.
- **Feature Importance:** Identifies the most influential features contributing to churn.
- **Interpretability:** Provides insights into model decisions to support business actions.

## Folder Structure

```
Customer Churn/
├── Customer Churn.ipynb   # Main Jupyter notebook with code and analysis
├── Readme.md              # Project documentation
```

## Model Results

| Algorithm                  | ROC AUC Mean | ROC AUC STD | Accuracy Mean | Accuracy STD |
|----------------------------|--------------|-------------|---------------|--------------|
| Logistic Regression        | 84.12        | 1.65        | 74.60         | 1.26         |
| SVC                        | 83.64        | 1.68        | 79.98         | 1.08         |
| Gaussian NB                | 81.82        | 1.79        | 68.99         | 1.46         |
| Random Forest              | 81.72        | 2.02        | 78.47         | 1.57         |
| Kernel SVM                 | 79.66        | 2.12        | 79.85         | 1.08         |
| KNN                        | 77.01        | 2.39        | 75.74         | 1.07         |
| Decision Tree Classifier   | 65.44        | 1.67        | 72.75         | 1.45         |

- **Best ROC AUC:** Logistic Regression (84.12)
- **Best Accuracy:** SVC (79.98)

## How to Run

1. Clone the repository and navigate to the `Customer Churn` folder.
2. Install the required Python libraries (see the notebook for details).
3. Open `Customer Churn.ipynb` in Jupyter Notebook or JupyterLab.
4. Run the notebook cells to reproduce the analysis and results.

## Results

- The best-performing model (Logistic Regression) achieves a ROC AUC of 84.12 and an accuracy of 74.60%.
- SVC achieves the highest accuracy at 79.98%.
- Key drivers of churn are highlighted, supporting targeted retention strategies.

## License

This project is for educational and demonstration purposes.

---

**Author:** Aneesha MP