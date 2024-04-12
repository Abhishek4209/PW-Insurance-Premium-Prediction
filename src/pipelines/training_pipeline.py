import sys
import os 
from src.logger import logging 
from src.exception import CustomException
import pandas as pd

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation



if __name__ == '__main__':
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    print(train_data_path,test_data_path)
    logging.info("Training data is completed")   
    
    data_transformation = DataTransformation() 
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)
    
