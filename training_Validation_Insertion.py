from datetime import datetime 
from Training_Raw_data_validation.rawValidation import Raw_Data_validation
from application_logging import logger

class train_validation:
    def __init__(self,path):
        self.raw_data=Raw_Data_validation(path)
        self.file_object=open("Training_Logs/Training_Main_log.txt",'a+')
        self.log_writer=logger.App_Logger()
    
    def train_validation(self):
        try:
            self.log_writer.log(self.file_object,'Start of Validation files!')

            LengthOfDateStampInFile,LengthOfTimeStampInFile,column_names,noofcolumns=self.raw_data.valuesFromSchema()
            regex=self.raw_data.manualRegexCreation()
            self.raw_data.validationFileNameRaw(regex,LengthOfDateStampInFile,LengthOfTimeStampInFile)
            self.raw_data.validateColumnLength(noofcolumns)
            self.raw_data.validateMissingValuesInWholeColumn()
            self.log_writer.log(self.file_object,"Raw Data Validation Complete!")
        except Exception as e:
            raise e