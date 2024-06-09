from datetime import datetime
import shutil
from os import listdir
import os
import pandas as pd
from application_logging.logger import App_Logger

class dBOperation:

    def __init__(self):
        self.goodFilePath = "Training_Raw_files_validated/Good_Raw"
        self.mergedFilePath = "Training_Raw_files_validated/Training_Raw/booking_data_training.csv"
        self.logger = App_Logger()

    def csv_merge(self):
        log_file = open("Training_Logs/DatabaseOperation.txt", 'a+')
        try:
            onlyfiles = [f for f in listdir(self.goodFilePath) if f.endswith('.csv')]
            if not onlyfiles:
                self.logger.log(log_file, f"{datetime.now()}: No CSV files found in {self.goodFilePath}")
                return
            
            merged_df = pd.DataFrame()
            for file in onlyfiles:
                file_path = os.path.join(self.goodFilePath, file)
                csv_df = pd.read_csv(file_path)
                merged_df = pd.concat([merged_df, csv_df], ignore_index=True)
            
            # Ensure the target directory exists
            target_dir = os.path.dirname(self.mergedFilePath)
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            
            merged_df.to_csv(self.mergedFilePath, index=False)
            self.logger.log(log_file, f"{datetime.now()}: Merged CSV created at {self.mergedFilePath}")
        except Exception as e:
            self.logger.log(log_file, f"{datetime.now()}: Error while merging data: {str(e)}")
            raise Exception(f"Error while merging data: {str(e)}")
        finally:
            log_file.close()
