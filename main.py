#from wsgrief import simple_server 
from flask import Flask,request,render_template
from flask import Response
import os 
from flask_cors import CORS, cross_origin 
import flask_monitoringdashboard as dashboard
from training_Validation_Insertion import train_validation
from trainingModel import trainModel
import json 

os.putenv('LANG', 'en-US.UTF-8')
os.putenv('LC_ALL', 'en-US.UTF-8')

# path='D:\ACADEMIC\ML Projects\Booking cancellation\Training_Data_Files'
# train_valObj=train_validation(path) #Initializing the validation object
# train_valObj.train_validation() #Calling the validation
app=Flask(__name__)
dashboard.bind(app) 
CORS(app)

@app.route("/",methods=["GET"])
@cross_origin() 
def home():
    return render_template('index.html')

@app.route("/train",methods=['POST'])
@cross_origin() 
def trainRouteClient():
    try:
        if request.json['folderPath'] is not None:
            path=request.json['folderPath']
            train_valObj=train_validation(path) #Initializing the validation object

            train_valObj.train_validation() #Calling the validation
            trainModelObj=trainModel()
    except ValueError:
        return Response("Error Occuered %s" %ValueError)
    except KeyError:
        return Response("Error Occuered %s" %KeyError)
    except Exception as e:
        return Response("Error Occuered %s" %e)

port=int(os.getenv("PORT",5000))
if __name__=="__main__":
    host='0.0.0.0'
    httpd=simple_server.make_server(host,port,app)
    httpd.serve_forever()
