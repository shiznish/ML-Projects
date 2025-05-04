# Explainable Intrusion Detection in IoT Networks

## Project Overview

This project aims to develop an **Explainable Intrusion Detection System (IDS)** for IoT networks. It leverages deep learning techniques for both **binary classification** (intrusion vs. normal) and **multi-class classification** (different intrusion types). The project also emphasizes model interpretability, enabling insights into the decision-making process through explainability tools.

## Key Features

- **Binary Classification Accuracy**: 99.32%
- **Multi-class Classification Accuracy**: 97.54%
- **Explainability**: SHAP, Captum, and DeepExplainer used to uncover model insights.
- **Optimization**: Hyperparameter tuning with Optuna for optimal performance.

## Libraries and Tools Used

The project workflow utilizes the following libraries:

- **PyTorch**: For building and training the deep learning model.
- **Optuna**: For hyperparameter optimization.
- **SHAP**: For explainability analysis using SHAP values.
- **Torchviz**: For visualizing the computational graph.
- **Captum**: For model interpretability using feature attribution.
- **NumPy**: For numerical operations.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For data visualization.
- **Scikit-learn**: For preprocessing, evaluation, and metrics.

## Methodology

1. **Data Preparation**:
   - Loaded and preprocessed a large dataset of IoT network intrusion data.
   - Tackled binary and multi-class classification tasks.

2. **Model Development**:
   - Built a Multi-Layer Perceptron (MLP) model using PyTorch.
   - Optimized hyperparameters with Optuna.

3. **Explainability**:
   - Analyzed model decisions with SHAP (DeepExplainer) and Captum.
   - Visualized feature importance and attribution scores for better transparency.

4. **Evaluation**:
   - Achieved high accuracy and F1 scores for both binary and multi-class tasks.
   - Iterative refinements improved performance based on explainability insights.

## Results

- **Binary Classification**:
  - Accuracy: **99.32%**
  - Demonstrated strong capability in distinguishing intrusions from normal traffic.

- **Multi-class Classification**:
  - Accuracy: **97.54%**
  - Effectively classified various types of intrusions.

- **Explainability Highlights**:
  - Identified key features contributing to model decisions using SHAP and Captum.
  - Improved model trustworthiness and interpretability.

## Novel Contributions

1. High accuracy for both binary and multi-class classification tasks.
2. Transparency through explainability tools like SHAP and Captum.
3. Robust hyperparameter optimization using Optuna.
4. Iterative feature refinement informed by explainability results.


