from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler, MinMaxScaler,RobustScaler
from sklearn.compose import ColumnTransformer

import pandas as pd
import numpy as np
import sys
import os 
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging

from src.utils import save_object

## Data Transformation config

@dataclass
class DataTransformationConfig():
    preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl")
    








## Data transformation class

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    
    def get_data_transformation_object(self):
        try:
            logging.info("Data Transformation initiated")
            # Define which columns should be oridinal -encoded and which should be scaled
            
            numeric_features =['age', 'bmi']
            categorical_features =['sex', 'smoker', 'region']
            
            logging.info("Pipeline INitiated")
            
            # Pipeline intialize
            preprocessors = ColumnTransformer(
                transformers=[
                    ('trf1',OneHotEncoder(sparse=False,handle_unknown='ignore'),categorical_features),
                    ('trf2',StandardScaler(),numeric_features),
                            ],remainder='passthrough'
                        ) 
            
            return preprocessors
        
            logging.info("Pipeline Completed")
            
        
        except Exception as e:
            
            logging.info("Error in Data Transformation")
            raise CustomException(e,sys)
        

    
    def initiate_data_transformation(self,train_path,test_path):
        try:
            # Reading train and test data
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            
            logging.info("Read train and test data completed")
            logging.info(f"Train Dataframe Head : \n{train_df.head().to_string()}")
            logging.info(f"Test Dataframe Head : \n{test_df.head().to_string()}")
        
            logging.info("Obtaing preprocessing object")
            
            preprocessing_obj=self.get_data_transformation_object()
            
            target_column_name="expenses"
            drop_columns=[target_column_name,"id"]
            
            
            # Feature devide  into independet and depedent features
            input_feature_train_df=train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df=train_df[target_column_name] 



            input_feature_test_df=train_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df=train_df[target_column_name] 
            
            ## apply the transformation
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.fit_transform(input_feature_test_df)
            
            logging.info("Applying preprocessing object on training and testing datsets.")
            
            
            train_arr=np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_df)]
            
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj)
            
            logging.info("Preprocessor pickle in create and saved")
            
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
            
        except Exception as e:
            loging.info("Exception occured in the initiate_datatransformation")
            
            raise CustomException(e,sys)