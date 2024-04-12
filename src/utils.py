from src.exception import CustomException
from src.logger import logging
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
from src.data_access import Insurance_Data
from sklearn.model_selection import train_test_split
import os,sys
from pandas import DataFrame

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig) :
            try:
                self.data_ingestion_config = data_ingestion_config

            except Exception as e:
                 raise CustomException(e,sys)
    
    def export_data_to_feature_store(self) ->DataFrame:
        """
         This function exports data from mongodb collection to the
         feature store in given file format and returns Dataframe 
        """
        try:
            logging.info("Exporting data from mongodb to feature store")
            insurance_data = Insurance_Data()
            dataframe = insurance_data.export_collection_as_dataframe(collection_name=self.data_ingestion_config.data_ingestion_collection_name)
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path 

            logging.info(f"Creating directory at {feature_store_file_path}")
            folder_path = os.path.dirname(feature_store_file_path)
            os.makedirs(folder_path,exist_ok=True)
            
            logging.info(f"Saving csv file at {feature_store_file_path}")
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            logging.info('Dataframe exported to feature store successfully')
            
            return dataframe

        except  Exception as e:
            raise  CustomException(e,sys)
    
    def split_data_as_train_test(self,dataframe:DataFrame):
        """
         This function will split feature store data into
         train and test dataset
        """
        try:
         train_set,test_set = train_test_split(dataframe,test_size=self.data_ingestion_config.train_test_split_ratio)
         logging.info("Performed train,test split ")
         
         dir_path = os.path.dirname(self.data_ingestion_config.train_file_path)
         os.makedirs(dir_path,exist_ok=True)

         train_path = self.data_ingestion_config.train_file_path
         logging.info(f"Saving train data at:{train_path}")
         train_set.to_csv(train_path,index=False,header=True)

         test_path = self.data_ingestion_config.test_file_path
         logging.info(f"Saving test data at:{test_path}")
         test_set.to_csv(test_path,index=False,header=True)

         logging.info(f"Exported train and test data")

        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            dataframe = self.export_data_to_feature_store()
            self.split_data_as_train_test(dataframe=dataframe)
            
            data_ingestion_artifact = DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.train_file_path,
                test_file_path=self.data_ingestion_config.test_file_path
            )
            return data_ingestion_artifact
        
        except Exception as e:
            raise CustomException(e,sys)