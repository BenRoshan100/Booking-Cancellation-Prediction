import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

class Preprocessor:

    def __init__(self,file_object,logger_object):
        self.file_object = file_object
        self.logger_object =logger_object

    def remove_columns(self,data,columns):
        self.logger_object.log(self.file_object,'Enetered the remove_coluns method of Preprocessor class')
        self.data=data 
        self.columns=columns 
        try:
            self.useful_data=self.data.drop(labels=self.columns,axis=1)
            self.logger_object.log(self.file_object,'Column removal successful. Exited the remove_coluns method of Preprocessor class')
            return self.useful_data
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occurred during remove_colums method of Preprocessor class. Exception message: '+str(e))
            self.logger_object.log(self.file_object,'Column removal unsuccessful. Exited the remove_coluns method of Preprocessor class')
            raise Exception()
        
    def separate_label_feature(self,data,label_column_name):
        self.logger_object.log(self.file_object,'Entered the separate_label_feature method of Preprocessor class')
        try:
            self.X=data.drop(labels=label_column_name,axis=1)
            self.Y=data[label_column_name]
            self.logger_object.log(self.file_object,'Label Separation successful. Exited the separate_label_feature method of Preprocessor class')
            return self.X,self.Y
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured during separate_label_feature method of Preprocessor class. Exception message: '+str(e))
            self.logger_object.log(self.file_object,'Label Separation failed. Exited the separate_label_feature method of Preprocessor')
            raise Exception()
        
    def is_null_present(self,data):
        self.logger_object.log(self.file_object,'Entered is_null_present method of Preprocessor class')
        self.is_null_present=False 
        try:
            self.null_counts=data.isna().sum()
            for i in self.null_counts:
                if i>0:
                    self.null_present=True 
                    break 
            if (self.null_present):
                dataframe_with_null=pd.DataFrame()
                dataframe_with_null['columns']=data.columns
                dataframe_with_null['missing values count']=np.asarray(data.isna().sum())
                dataframe_with_null.to_csv('preprocessing_data/null_values.csv')
            self.logger_object.log(self.file_object,'Finding missing calues is a success. Data written to the null values file. Exited the is_null_present method of Preprocessor class')
            return self.null_present 
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occurred in is_null_present method of Preprocessor class. Exception message '+str(e))
            self.logger_object.log(self.file_object,'Finding missing values failed. Exited the is_null_present method of Preprocessor class')
            raise Exception()
    def impute_missing_values(self,data):
        self.logger_object.log(self.file_object,'Entered the impute_missing_values method of Preprocessor class')
        self.data=data
        try:
            pass
        except Exception as e:
            pass