from datetime import datetime 
from Prediction_Raw_Data_Validation.predictionDataValidation import Prediction_Data_validation
from DataTransform_Prediction.DataTransformationPrediction import dataTransformPredict
from Prediction_Raw_Data_Validation.PredictionDataBaseOperation import dBOperation
from DataTransform_Training.DataTransformation import dataTransform
from application_logging import logger

class pred_validation:
    def __init__(self,path):
        self.raw_data=Prediction_Data_validation(path)
        self.dataTransform=dataTransformPredict()
        self.dBOperation=dBOperation()
        self.file_object=open("Prediction_Logs/Prediction_log.txt",'a+')
        self.log_writer=logger.App_Logger()
    
    def prediction_validation(self):
        try:
            self.log_writer.log(self.file_object,'Start of Validation files for prediction!')

            LengthOfDateStampInFile,LengthOfTimeStampInFile,column_names,noofcolumns=self.raw_data.valuesFromSchema()
            regex=self.raw_data.manualRegexCreation()
            self.raw_data.validationFileNameRaw(regex,LengthOfDateStampInFile,LengthOfTimeStampInFile)
            self.raw_data.validateColumnLength(noofcolumns)
            self.raw_data.validateMissingValuesInWholeColumn()
            self.log_writer.log(self.file_object,"Raw Data Validation Complete!")
            self.log_writer.log(self.file_object,"Starting Data Transformation!")
            self.dataTransform.replaceMissingWithNull()
            self.log_writer.log(self.file_object,"Data Transformation Complete!")
            self.log_writer.log(self.file_object,"Merging all Prediction Files!")
            self.dBOperation.csv_merge()
            self.log_writer.log(self.file_object,"Merging Complete!")
        except Exception as e:
            raise e