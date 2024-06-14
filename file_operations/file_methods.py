import pickle 
import os 
import shutil 

class File_Operation:
    def __init__(self,file_object,logger_object):
        self.file_object = file_object
        self.logger_object = logger_object 
        self.model_directory = 'models/'

    def save_model(self,model,filename):
        self.logger_object.log(self.file_object,'Entered the save_model method of the File_Operation class')
        try:
            path=os.path.join(self.model_directory,filename)
            if os.path.isdir(path):
                shutil.rmtree(self.model_directory)
                os.makedirs(path)
            else:
                os.makedirs(path)
            with open(path+'/'+filename+'.sav','wb') as f:
                pickle.dump(model,f)
            self.logger_object.log(self.file_object,'Model File'+filename+' saved. Exited the save_model method of the Model_Finder class')

            return 'success'
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in save_model method of the Model_Finder class. Exception message: '+str(e))
            self.logger_object.log(self.file_object,'Model File'+filename+' coult not be saved. Exited the save_model method of the Model_Finder class')
            raise Exception()