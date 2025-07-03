# Airline Ticket Price Prediction

This project predicts airline ticket prices using machine learning models. It includes data preprocessing, feature engineering, and model training for both regression and classification tasks.

## Features

- Data preprocessing and cleaning
- Feature engineering (date/time, route, distance, etc.)
- Multiple regression models (Linear, Polynomial)
- Decision tree classification
- Model saving and loading
- Correlation analysis and visualization

## Project Structure

- `main.py` - Main script for training and evaluating models
- `Pre_Processing.py` - Data cleaning and feature engineering
- `Helper.py` - Utility functions for encoding, scaling, and feature creation
- `Models.py` - Model wrapper class for training, testing, saving, and loading models
- `Geocoding.py` - Geocoding utilities for calculating distances
- `my_new_data3.csv` - Preprocessed dataset for model training
- `ss.csv` - Stores calculated distances between routes
- `DTModel_DecisionTreeClassification.sav` - Saved decision tree model

## Usage

1. **Preprocess Data**  
   Run `Pre_Processing.py` to clean and engineer features from the raw dataset. This will generate `my_new_data3.csv`.

2. **Train Models**  
   Run `main.py` to:
   - Load the preprocessed data
   - Train linear and polynomial regression models
   - Train and evaluate a decision tree classifier (example with Iris dataset)
   - Display correlation heatmaps

3. **Model Saving/Loading**  
   Models are saved as `.sav` files and can be loaded for future predictions.

## Example

To train and evaluate models:
```sh
python main.py
```

## Requirements

- Python 3.x
- pandas
- numpy
- scikit-learn
- seaborn
- matplotlib
- dateutil

Install dependencies with:
```sh
pip install -r requirements.txt
```

## Example Results

Below are sample results from running the models:

### Regression (Airline Ticket Price Prediction)
| Model                  | Train Score | Test Score | MSE           |
|------------------------|-------------|------------|---------------|
| Linear Regression      | 0.8952      | 0.8944     | 54,570,143.11 |
| Polynomial Regression  | 0.9139      | 0.9110     | 45,976,276.34 |

- **Train/Test Score:** Proportion of variance explained by the model (R²). Higher is better.
- **MSE:** Mean Squared Error. Lower is better.

### Classification (Iris Dataset Example)
| Model                  | Train Score | Test Score |
|------------------------|-------------|------------|
| Decision Tree Classifier | 0.975     | 0.975      |
| Custom Test Score        | 0.8333    |            |

- **Train/Test Score:** Classification accuracy.

---

These results show that the regression models can explain over 89% of the variance in airline ticket prices, with polynomial regression performing best. The classification example demonstrates high accuracy on the Iris dataset.

## Notes

- The project uses both regression and classification approaches.
- Distance between airports is calculated and cached in `ss.csv`.
- The code includes progress indicators for long-running preprocessing steps.

---

Feel free to modify or extend the code for your specific use