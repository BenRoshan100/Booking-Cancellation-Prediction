#from wsgrief import simple_server 
from flask import Flask,request,render_template
from flask import Response
import os 
from flask_cors import CORS, cross_origin 
import flask_monitoringdashboard as dashboard
from training_Validation_Insertion import train_validation
from trainingModel import trainModel
from prediction_Validation_Insertion import pred_validation
from predictFromModel import prediction
import json 

os.putenv('LANG', 'en-US.UTF-8')
os.putenv('LC_ALL', 'en-US.UTF-8')

# path='D:\ACADEMIC\ML Projects\Booking cancellation\Training_Data_Files'
# train_valObj=train_validation(path) #Initializing the validation object
# train_valObj.train_validation() #Calling the validation
# trainModelObj = trainModel() #Initializing the Training object
# trainModelObj.trainingModel() #Calling the training model

path='D:\ACADEMIC\ML Projects\Booking cancellation\Prediction_Data_Files'
pred_val=pred_validation(path) #Initializing the validation object
pred_val.prediction_validation() #Calling the validation
pred=prediction(path) #Initializing the prediction object
path,json_predictions=pred.predictionFromModel()
            
# app=Flask(__name__)
# dashboard.bind(app) 
# CORS(app)

# @app.route("/",methods=["GET"])
# @cross_origin() 
# def home():
#     return render_template('index.html')

# @app.route("/predict",methods=["GET"])
# @cross_origin() 
# def predictRouteClient():
#     try:
#         if request.json is not None:
#             path=request.json['filepath']
#             pred_val=pred_validation(path)
#             pred_val.prediction_validation()

#             pred=prediction(path)

#             path,json_predictions=pred.predictionFromModel()
#             return Response("Prediction File created at !!!" + str(path) + 'and few of the predictions are '+str(json.loads(json_predictions)))
#         elif request.form is not None:
#             path=request.form['filepath']
#             pred_val=pred_validation(path)
#             pred_val.prediction_validation()

#             pred=prediction(path)

#             path,json_predictions=pred.predictionFromModel()
#             return Response("Prediction File created at !!!" + str(path) + 'and few of the predictions are '+str(json.loads(json_predictions)))
#         else:
#             print('Nothing matched')
#     except ValueError:
#         return Response("Error Occurred! %s" %ValueError)
#     except KeyError:
#         return Response("Error Occurred %s" %KeyError)
#     except Exception as e:
#         return Response("Error Occurred %s" %e)
    


# @app.route("/train",methods=['POST'])
# @cross_origin() 
# def trainRouteClient():
#     try:
#         if request.json['folderPath'] is not None:
#             path=request.json['folderPath']
#             train_valObj=train_validation(path) #Initializing the validation object

#             train_valObj.train_validation() #Calling the validation
#             trainModelObj=trainModel()
#             trainModelObj.trainingModel() 
#     except ValueError:
#         return Response("Error Occuered %s" %ValueError)
#     except KeyError:
#         return Response("Error Occuered %s" %KeyError)
#     except Exception as e:
#         return Response("Error Occuered %s" %e)

# port=int(os.getenv("PORT",5000))
# if __name__=="__main__":
#     host='0.0.0.0'
#     httpd=simple_server.make_server(host,port,app)
#     httpd.serve_forever()
