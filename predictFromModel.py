import pandas  
from file_operations import file_methods
from data_preprocessing import preprocessing
from application_logging import logger 
from data_ingestion import data_loader
from Prediction_Raw_Data_Validation.predictionDataValidation import Prediction_Data_validation

class prediction:
    def __init__(self,path):
        self.file_object=open("Prediction_Logs/Prediction_Log.txt",'a+')
        self.log_writer=logger.App_Logger()
        if path is not None:
            self.pred_data_val=Prediction_Data_validation(path)
    
    def predictionFromModel(self):
        try:
            self.pred_data_val.deletePredictionFile()
            self.log_writer.log(self.file_object,'Start of Prediction')
            data_getter=data_loader.Data_Getter(self.file_object,self.log_writer)
            data=data_getter.get_data_predict()
            preprocessor=preprocessing.Preprocessor(self.file_object,self.log_writer)
            label_encode_cols=['type of meal', 'room type']
            onehot_encode_cols=['market segment type']
            data=preprocessor.encode_data_prediction(data,label_encode_cols,onehot_encode_cols)
            is_null_present=preprocessor.is_null_present(data)
            if(is_null_present):
                data=preprocessor.impute_missing_values(data)
            date_column='date of reservation'
            data=preprocessor.extract_date_features(data,date_column)
            cols_to_drop=preprocessor.get_columns_with_zero_std_deviation(data)
            data=preprocessor.remove_columns(data,cols_to_drop)
            booking_ids=list(data['Booking_ID'])
            data=data.drop(labels=['Booking_ID'],axis=1)
            file_loader=file_methods.File_Operation(self.file_object,self.log_writer)
            model_name=file_loader.find_correct_model_file()
            model,label_encoder_train=file_loader.load_model(model_name)
            result=list(model.predict(data))
            result = label_encoder_train.inverse_transform(result)
            result=pandas.DataFrame(list(zip(booking_ids,result)),columns=['Booking_ID', 'Prediction'])
            path="Prediction_Output_File/Predictions.csv"
            result.to_csv("Prediction_Output_File/Predictions.csv",header=True,mode='a+')
            self.log_writer.log(self.file_object,'End of Prediction')
        except Exception as e:
            self.log_writer.log(self.file_object,'Error occurred while running prediction. Error:: %s' %e)
            raise e 
        return path, result.head().to_json(orient="records")


