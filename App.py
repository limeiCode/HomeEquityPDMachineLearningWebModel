## Flask
import os
import pandas as pd
import numpy as np
# from flask import Flask, jsonify, render_template
from flask import (
    Flask,
    render_template,
    jsonify,
    request)


from sklearn.metrics import accuracy_score 
from sklearn.externals import joblib
# from flask_sqlalchemy import SQLAlchemy
# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine

app = Flask(__name__ , static_url_path='')

from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler


number_of_features=15
def create_network(optimizer='rmsprop'):   
    network = models.Sequential()    
    network.add(layers.Dense(units=16, activation='relu', input_shape=(number_of_features,))) 
    network.add(layers.Dense(units=2, activation='softmax'))        
    network.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])             
    return network
# ValueError: Error when checking input: expected dense_112_input to have shape (15,) but got array with shape (1,)
# sloved by : test_array = np.asarray(test_inputs, dtype=np.float32)

with open('pickles/gridlr.pkl', 'rb') as f:
    gridlr = joblib.load(f)
with open('pickles/gridsvm.pkl', 'rb') as f:
    gridsvm = joblib.load(f)
with open('pickles/griddeep.pkl', 'rb') as f:
    griddeep = joblib.load(f)
    
gridmodels = {'Logistic Regression': gridlr,
              'Linear Support Vector Machine': gridsvm,
              'Deep Neural Network Learning': griddeep
             }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/prediction")
def prediction():
    return render_template("modelprediction.html")
@app.route("/development")
def development():
    return render_template("modeldevelopment.html")
@app.route("/introduction")
def introduction():
    return render_template("modelintroduction.html")


@app.route("/predictonesample", methods=["GET", "POST"])    # flask request: bring data back to Form by render jinja template
# @app.route("/predictonesample/<inpdata>")
def predictioninput():  
    #<input>  15 columns
    finalresult  = ""   
    msg = ""
    form_data = {"delinquentcreditlinescount":""}
    # print(request.method)                                           # initialization here for return "" for GET
    if request.method =="POST":
        form_data = request.form
        # 1)dummpy : dropdowns(cooupation, applyloanreason): selected=1 unselected=0  
        delinquentcreditlinescount = float(request.form["delinquentcreditlinescount"])  # is key not function form["inputdata2"] form("inputdata2")
        derogatoryreportscount = float(request.form["derogatoryreportscount"])  
        recentcreditinquirycount = float(request.form["recentcreditinquirycount"])  
        debttoincomeratio = float(request.form["debttoincomeratio"])
        creditlinecount = float(request.form["creditlinecount"])
        currentpropertyvalue = float(request.form["currentpropertyvalue"]) 
        mortgageamountdue = float(request.form["mortgageamountdue"])
        yearsatpresentjob = float(request.form["yearsatpresentjob"])        
        # occupation = request.form["occupations"]  # Bad Request -- The browser (or proxy) sent a request that this server could not understand.
        occupation = request.form.get('occupations')
        occupation_Other = 0
        occupation_Sales = 0
        occupation_Self = 0
        occupation_Mgr = 0
        occupation_ProfExe = 0
        if occupation == "Sales":
            occupation_Sales = 1
        elif occupation == "ProfExe":
            occupation_ProfExe = 1
        elif occupation == "Manager":
            occupation_Mgr = 1
        elif occupation == "Other":
            occupation_Other = 1
        elif occupation == "Self":
            occupation_Self = 1
        else:
            msg = msg + "Occupation is not selected! "
            # print("not select occupation")
        # applyloanreason = request.form["applyloanfeasons"]
        applyloanreason = request.form.get('applyloanreasons')
        applyloanreason_DebtCon = 0
        applyloanreason_HomeImp = 0
        if applyloanreason == "Debt Consolidation":
            applyloanreason_DebtCon = 1
        elif applyloanreason == "Home Improvement":  # HomeImp
            applyloanreason_HomeImp = 1
        else:
            msg = msg + "Reason is not selected! "
            # print("not select reason")

        test_inputs = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        # below order can't be changed 
        test_inputs[0][0] = delinquentcreditlinescount  
        test_inputs[0][1] = derogatoryreportscount  
        test_inputs[0][2] = recentcreditinquirycount  
        test_inputs[0][3] = debttoincomeratio  
        test_inputs[0][4] = occupation_Other  
        test_inputs[0][5] = occupation_Sales  
        test_inputs[0][6] = occupation_Self  
        test_inputs[0][7] = applyloanreason_HomeImp  
        test_inputs[0][8] = occupation_Mgr  
        test_inputs[0][9] = creditlinecount  
        test_inputs[0][10] = currentpropertyvalue   
        test_inputs[0][11] = applyloanreason_DebtCon  
        test_inputs[0][12] = occupation_ProfExe  
        test_inputs[0][13] = mortgageamountdue  
        test_inputs[0][14] = yearsatpresentjob  

        test_array = np.asarray(test_inputs, dtype=np.float32)

        # 2) MinMaxScaler(): dummied fields + other integer fields    
        X_train = pd.read_csv("data\HomeEquityLoans_X_train.csv")  # should from DB??
        X_scaler = MinMaxScaler().fit(X_train)
        test_array_scaled = X_scaler.transform(test_array)
        # print(test_array_scaled )

        gridlr_predictions = gridlr.predict(test_array_scaled)   # error 500: Failed to load resource: the server responded with a status of 500 (INTERNAL SERVER ERROR)
        gridsvm_predictions = gridsvm.predict(test_array_scaled)
        griddeep_predictions = griddeep.predict(test_array_scaled)

        all_predictions = zip(gridlr_predictions, gridsvm_predictions, griddeep_predictions)

        final_predictions = []    
        for tup in all_predictions:
            final_predictions.append( max( set(list(tup)), key=list(tup).count ) )  
            final=final_predictions[0]

        if final == 1:
            finalresult = "Default"
        else:
            finalresult = "Not Default" 

    # print(msg)
    # return render_template("modelprediction.html", prediction = finalresult, msg=msg )
    return render_template("modelprediction.html", prediction = finalresult, msg=msg, form_data=form_data )

# @app.route('/modeldevelopement/')
# def prediction():                                          
#     # <4> get the static graph picutre from AWS S3 bucket - save in jupyter notevbook and stored in AWS S3
#     # <5> use plotly danamically genertate graph
#     return "picture"

if __name__ == '__main__':
    app.run()


