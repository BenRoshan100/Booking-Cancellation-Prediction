from sklearn.model_selection import train_test_split
from application_logging import logger
from data_ingestion import data_loader
from data_preprocessing import preprocessing


class trainModel:
    
    def __init__(self):
        self.log_writer=logger.App_Logger()
        self.file_object=open("Training_Logs/ModelTrainingLog.txt",'a+')
    
    def trainingModel(self):
        self.log_writer.log(self.file_object,'Start of training')
        try:
            data_getter=data_loader.Data_Getter(self.file_object,self.log_writer)
            data=data_getter.get_data()

            preprocessor=preprocessing.Preprocessor(self.file_object,self.log_writer)

            X,Y=preprocessor.separate_label_feature(data,label_column_name='booking status')

            is_null_present=preprocessor.is_null_present(X)

            if(is_null_present):
                X=preprocessor.impute_missing_values(X)

            cols_to_drop=preprocessor.get_columns_with_zero_std_deviation(X)

            X=preprocessor.remove_columns(X,cols_to_drop)

        except Exception as e:
            raise e
