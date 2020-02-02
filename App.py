## Flask
import os
import pandas as pd
import numpy as np
from flask import (
    Flask,
    render_template,
    jsonify,
    request)


from sklearn.metrics import accuracy_score 
from sklearn.externals import joblib

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



@app.route("/predictonesample", methods=["GET", "POST"])   
def predictioninput():  
    finalresult  = ""   
    msg = ""
    form_data = { "delinquentcreditlinescount":"", 
        "derogatoryreportscount":"",  
        "recentcreditinquirycount" :"", 
        "debttoincomeratio":"",
        "creditlinecount":"",
        "currentpropertyvalue" :"",
        "mortgageamountdue":"",
        "yearsatpresentjob":"",
        "applyloanreasons":"",
        "occupations":""  } 


    # form_data = { "delinquentcreditlinescount":0, 
    #     "derogatoryreportscount":0,  
    #     "recentcreditinquirycount" :0, 
    #     "debttoincomeratio":0,
    #     "creditlinecount":0,
    #     "currentpropertyvalue" :0,
    #     "mortgageamountdue":0,
    #     "yearsatpresentjob":0,
    #     "applyloanreasons":"",
    #     "occupations":""  } 
    
    if request.method =="POST":
        msg = ""
        form_data = request.form

        # validate form data: https://stackoverflow.com/questions/55772012/how-to-validate-html-forms-in-python-flask
        if form_data["delinquentcreditlinescount"]!=""  \
        and form_data["derogatoryreportscount"]!=""  \
        and form_data["recentcreditinquirycount"]!=""   \
        and form_data["debttoincomeratio"]!=""   \
        and form_data["creditlinecount"]!=""   \
        and form_data["mortgageamountdue"]!=""   \
        and form_data["yearsatpresentjob"]!=""   \
        and (form_data["applyloanreasons"]=="Debt Consolidation" or form_data["applyloanreasons"]=="Home Improvement") \
        and (form_data["occupations"]=="Sales") or (form_data["occupations"]=="ProfExe") or (form_data["occupations"]=="Manager") or (form_data["occupations"]=="Other") or (form_data["occupations"]=="Self"):
        # if form_data["occupations"]!="-- select an option --" :  # ????

            # 1)dummpy : dropdowns(cooupation, applyloanreason): selected=1 unselected=0  
            # delinquentcreditlinescount = float(request.form["delinquentcreditlinescount"])  # also works
            delinquentcreditlinescount = float(form_data["delinquentcreditlinescount"])  
            derogatoryreportscount = float(form_data["derogatoryreportscount"])  
            recentcreditinquirycount = float(form_data["recentcreditinquirycount"])  
            debttoincomeratio = float(form_data["debttoincomeratio"])
            creditlinecount = float(form_data["creditlinecount"])
            currentpropertyvalue = float(form_data["currentpropertyvalue"]) 
            mortgageamountdue = float(form_data["mortgageamountdue"])
            yearsatpresentjob = (form_data["yearsatpresentjob"])  

            occupation = form_data["occupations"]
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

            applyloanreason = form_data["applyloanreasons"]
            applyloanreason_DebtCon = 0
            applyloanreason_HomeImp = 0
            if applyloanreason == "Debt Consolidation":
                applyloanreason_DebtCon = 1
            elif applyloanreason == "Home Improvement":   
                applyloanreason_HomeImp = 1
            else:
                msg = msg + "Reason is not selected! "

            test_inputs = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            # !!!below order can't be changed 
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
            X_train = pd.read_csv("data/HomeEquityLoans_X_train.csv")   
            X_scaler = MinMaxScaler().fit(X_train)
            test_array_scaled = X_scaler.transform(test_array)

            gridlr_predictions = gridlr.predict(test_array_scaled)   
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
        else:
            msg = msg + "Please complete inputs! "

    return render_template("modelprediction.html", prediction = finalresult, msg=msg, form_data=form_data )


if __name__ == '__main__':
    app.run()


