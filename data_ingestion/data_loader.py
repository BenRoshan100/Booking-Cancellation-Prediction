import pandas as pd

class Data_Getter:

    def __init__(self,file_object,logger_object):
        self.training_file= 'Training_Raw_files_validated/Training_Raw/booking_data_training.csv'
        self.prediction_file= 'Prediction_Raw_files_validated/Prediction_Raw/booking_data_prediction.csv'
        self.file_object =file_object
        self.logger_object = logger_object

    def get_data_train(self):

        self.logger_object.log(self.file_object, 'Entered the get_data method of Data_Getter class')
        try: 
            self.data=pd.read_csv(self.training_file)
            self.logger_object.log(self.file_object, 'Data Load successful. Exited the get_data method of Data_Getter class')
            return self.data
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occued in get_data method of Data_Getter class. Exception message:'+str(e))
            self.logger_object.log(self.file_object,'Data Load Unsuccessful. Exited get_data method of Data_Getter class.')
            raise Exception()
        
    def get_data_predict(self):

        self.logger_object.log(self.file_object, 'Entered the get_data method of Data_Getter class for Prediction')
        try: 
            self.data=pd.read_csv(self.prediction_file)
            self.logger_object.log(self.file_object, 'Data Load successful for Prediction. Exited the get_data method of Data_Getter class')
            return self.data
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occued in get_data method of Data_Getter class. Exception message:'+str(e))
            self.logger_object.log(self.file_object,'Data Load Unsuccessful. Exited get_data method of Data_Getter class.')
            raise Exception()