import numpy as np
import pandas as pd
import os
import sys
from src.utils import save_object
from src.utils import evaluate_model

from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn.neighbors import KNeighborsRegressor




@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
        
    
    def initate_model_training(self,train_array,test_array):
        try:
            logging.info('Splitting Dependent and Independent variables from train and test data')
            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models={
            'RandomForestRegressor':RandomForestRegressor(),
            'LinearRegression':LinearRegression(),
            'DecisionTreeRegressor':DecisionTreeRegressor(),
            "KNeighborsRegressor": KNeighborsRegressor(n_neighbors=5,p=2,algorithm="auto"),
            'XGBRegressor':XGBRegressor(base_score=0.5, booster='gbtree', callbacks=None,
            colsample_bylevel=1, colsample_bynode=1, colsample_bytree=1,
            early_stopping_rounds=None, enable_categorical=False,
            eval_metric=None, gamma=0, gpu_id=-1, grow_policy='depthwise',
            importance_type=None, interaction_constraints='',
            learning_rate=0.1, max_bin=256, max_cat_to_onehot=4,
            max_delta_step=0, max_depth=6, max_leaves=0, min_child_weight=1,
            monotone_constraints='()', n_estimators=32, n_jobs=0,
            num_parallel_tree=1, predictor='auto', random_state=0, reg_alpha=0,
            reg_lambda=1)
            
        }
            
            model_report:dict=evaluate_model(X_train,y_train,X_test,y_test,models)
            print(model_report)
            print('\n====================================================================================\n')
            logging.info(f'Model Report : {model_report}')

            # To get best model score from dictionary 
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            best_model = models[best_model_name]

            print(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
    
            
        
        
        
        
        
        
        except Exception as e:
            logging.info('Exception occured at Model Training')
            raise CustomException(e,sys)