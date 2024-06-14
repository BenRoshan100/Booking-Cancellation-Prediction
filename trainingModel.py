from sklearn.model_selection import train_test_split
from application_logging import logger
from data_ingestion import data_loader
from data_preprocessing import preprocessing
from file_operations import file_methods
from best_model_finder import tuner 


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
            label_encode_cols=['type of meal', 'room type', 'booking status']
            onehot_encode_cols=['market segment type']
            data=preprocessor.encode_data(data,label_encode_cols,onehot_encode_cols)
            
            X,Y=preprocessor.separate_label_feature(data,label_column_name='booking status')
            is_null_present=preprocessor.is_null_present(X)

            if(is_null_present):
                X=preprocessor.impute_missing_values(X)
            
            date_column='date of reservation'
            X=preprocessor.extract_date_features(X,date_column)

            cols_to_drop=preprocessor.get_columns_with_zero_std_deviation(X)
            id_column='Booking_ID'
            cols_to_drop.append(id_column)
            

            X=preprocessor.remove_columns(X,cols_to_drop)

            """Model Training starts here"""

            x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=1/3,random_state=143)

            model_finder=tuner.Model_Finder(self.file_object,self.log_writer)

            best_model_name,best_model=model_finder.get_best_model(x_train,y_train,x_test,y_test)

            file_op=file_methods.File_Operation(self.file_object,self.log_writer)

            save_model=file_op.save_model(best_model,best_model_name)

            self.log_writer.log(self.file_object,'Successful End of Training')
            self.file_object.close()

        except Exception as e:
            self.log_writer.log(self.file_object,'Unsuccessful End of Training')
            self.file_object.close()
            raise e
