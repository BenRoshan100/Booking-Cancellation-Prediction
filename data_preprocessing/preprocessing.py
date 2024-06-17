import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder

class Preprocessor:

    def __init__(self,file_object,logger_object):
        self.file_object = file_object
        self.logger_object =logger_object

    def remove_columns(self,data,columns):
        self.logger_object.log(self.file_object,'Entered the remove_coluns method of Preprocessor class')
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
        self.null_present=False 
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
        
    def extract_date_features(self,data,date_column):
        self.logger_object.log(self.file_object,'Entered the extract_date_features method of Preprocessor class')
        self.data=data
        try:
            data[date_column] = pd.to_datetime(data[date_column],format='%m/%d/%Y',errors='coerce')
            data[date_column].fillna(method='ffill')

            data['reservation_year']=data[date_column].dt.year
            data['reservation_ month']=data[date_column].dt.month
            data['reservation_day']=data[date_column].dt.day
            data['reservation_dayofweek']=data[date_column].dt.dayofweek
            data['reservation_is_weekend']=data[date_column].dt.dayofweek>=5

            data=data.drop([date_column],axis=1)
            self.logger_object.log(self.file_object,'Extraction of date objects are successful')
            return data
        except Exception as e:
            self.logger_object.log(self.file_object,f'Exception occurred in extract_date_features method of Preprocessor class. Exception message: {str(e)}')
            raise e

    def encode_data(self,data,label_encode_cols,onehot_encode_cols):
        self.logger_object.log(self.file_object,'Entered the encode_data method of Preprocessor class')
        self.data=data
        try:
            label_encoder=LabelEncoder()
            for col in label_encode_cols:
                data[col]=label_encoder.fit_transform(data[col])

            data=pd.get_dummies(data,columns=onehot_encode_cols,drop_first=True)
            self.logger_object.log(self.file_object,'Object features are successfully encoded')
            return data,label_encoder
        
        except Exception as e:
            self.logger_object.log(self.file_object,f'Exception occurred in encode_data method of Preprocessor class. Exception message: {str(e)}')
            raise e
        
    def encode_data_prediction(self,data,label_encode_cols,onehot_encode_cols):
        self.logger_object.log(self.file_object,'Entered the encode_data_prediction method of Preprocessor class')
        self.data=data
        try:
            label_encoder=LabelEncoder()
            for col in label_encode_cols:
                data[col]=label_encoder.fit_transform(data[col])

            data=pd.get_dummies(data,columns=onehot_encode_cols,drop_first=True)
            self.logger_object.log(self.file_object,'Object features are successfully encoded for prediction pipeline')
            return data
        
        except Exception as e:
            self.logger_object.log(self.file_object,f'Exception occurred in encode_data_prediction method of Preprocessor class. Exception message: {str(e)}')
            raise e


    def impute_missing_values(self,data):
        self.logger_object.log(self.file_object,'Entered the impute_missing_values method of Preprocessor class')
        self.data=data
        try:
            numerical_cols=self.data.select_dtypes(include=[np.number]).columns 
            categorical_cols=self.data.select_dtypes(include=[object]).columns 

            low_cardinality_cols=[col for col in self.data.columns if self.data[col].nunique()<20]

            categorical_cols.extend(low_cardinality_cols)
            categorical_cols=list(set(categorical_cols))

            numerical_cols=[col for col in numerical_cols if col not in categorical_cols]

            if numerical_cols:
                knn_imputer=KNNImputer(n_neighbors=3)
                self.data[numerical_cols]=knn_imputer.fit_transform(self.data[numerical_cols])
            
            if categorical_cols:
                simple_imputer=SimpleImputer(strategy='most_frequent')
                self.data[categorical_cols]=simple_imputer.fit_transform(self.data[categorical_cols])

            self.logger_object.log(self.file_object,'Imputing missing values successful')
            print(self.data)
            return self.data


        except Exception as e:
            self.logger_object.log(self.file_object,f'Exception occurred in impute_missing_values method of Preprocessor class. Exception message: {str(e)}')
            raise e
    def get_columns_with_zero_std_deviation(self,data):

        self.logger_object.log(self.file_object,"Entered the get_columns)with_zero_std_deviation method of Preprocessor class")
        numerical_cols=data.select_dtypes(include=[np.number]).columns
        self.data_n=data.describe()
        self.col_to_drop=[]
        try:
            for x in numerical_cols:
                if(self.data_n[x]['std']==0):
                    self.col_to_drop.append(x)
            self.logger_object.log(self.file_object,'Column search for Standard Deviation of Zero Successful. Exited the get_columns_with_zero_std_deviation method of Preprocessor class')
            return self.col_to_drop
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in get_columns_with_zero_std_deviation method of Preprocessor class. Exception message: '+str(e))
            self.logger_object.log(self.file_object,'Column search for Standard Deviation of Zero Failed. Exited the get_columns_with_zero_std_deviation method of Preprocessor class')
            raise Exception()