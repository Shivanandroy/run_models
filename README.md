# run_models

**run_models** lets you run many regression and classification models with their default parameters and rank them by RMSE or AUC. 

## Installation

`pip install run_models`

## Dependencies
`numpy`

`pandas`

`scikit-learn`

`xgboost`

`lightgbm`

`catboost`

`matplotlib`

## How to use it?

`run_models` comes with two functions:
- `run_models.run_regressors(data, target_column)` for regression tasks - All models are ranked by RMSE.
- `run_models.run_classifiers(data, target_column)` for classification tasks - All models are ranked y AUC.

`import run_models as rm` 

`fig = rm.run_classifiers(titanic_data, 'Survived')`


