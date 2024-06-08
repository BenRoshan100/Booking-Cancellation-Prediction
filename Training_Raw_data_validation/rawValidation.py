from datetime import datetime
from os import listdir
import os 
import re 
import json 
import shutil 
import pandas as pd
from application_logging.logger import App_Logger 

class Raw_Data_validation:

    def __init__(self,path):
        self.Batch_Directory = path 
        self.schema_path='schema_training.json'
        self.logger = App_Logger()

    def valuesFromSchema(self):
        try:
            with open(self.schema_path,'r') as f:
                dic=json.load(f)
                f.close()
            pattern=dic['SampleFileName']
            LengthOfDateStampInFile=dic['LengthOfDateStampInFile']
            LengthOfTimeStampInFile=dic['LengthOfTimeStampInFile']
            column_names=dic['ColName']
            NumberOfColumns=dic['NumberofColumns']

            file=open("Training_Logs/valuesfromSchemaValidationLog.txt",'a+')
            message="LengthOfDateStampInFile:: %s" %LengthOfDateStampInFile + "\t" + "LengthOfTimeStampInFile:: %s" % LengthOfTimeStampInFile + "\t" + "NumberofColumns:: %s" % NumberOfColumns + "\n"
            self.logger.log(file,message)

            file.close()

        except ValueError:
            file=open("Training_Logs/valuesfromSchemaValidationLog.txt",'a+')
            self.logger.log(file,"ValueError:Value not found inside schema_training.json")
            file.close()
            raise ValueError
        except KeyError:
            file=open("Training_Logs/valuesfromSchemaValidationLog.txt",'a+')
            self.logger.log(file,"KeyError:Key value error incorrect key passed")
            file.close()
            raise KeyError
        except Exception as e:
            file=open("Training_Logs/valuesfromSchemaValidationLog.txt",'a+')
            self.logger.log(file,str(e))
            file.close()
            raise e

        return LengthOfDateStampInFile,LengthOfTimeStampInFile,column_names,NumberOfColumns

    def manualRegexCreation(self):
        regex = "['booking']+['\_'']+[\d_]+[\d]+\.csv"
        return regex 
     
    def validationFileNameRaw(self,regex,LengthOfDateStampInFile,LengthOfTimeStampInFile):
        pass
