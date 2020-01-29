

# Home Equity PD Machine Learning Web Model

This project using **Python** language developed three **Machine Learning** models *Logistic Regression*, *Support Vector Machine* for Classification and *Deep Learning* and used the ensemble method to predict a Home Equity Loan is default or not. Then developed a **Flask** full stack *web application* for the model deployment. After the user input the loan data an *API Call* for prediction was sent to the server and the server by running the machine learning model got predictin result then rendered a **Jinja Template**</span> with the result to the user.

- - -

![MachinLearning.jpg](static/images/img3.jpg)

- - -


## Data Source

The Home Equity Loan data is from  [**Home Equity Loan Dataset**](http://www.creditriskanalytics.net/datasets-private2.html).

This data set reports `characteristics` and `delinquency` information for **5,960** home equity loans. 

A home equity loan is a loan where the obligor uses the equity of his or her home as the underlying collateral. 


## Technologies Used

* Python web framework **Flask** and it's extensions **Render_Template** are used to render templates with specific data by using Jinja template library back to user.

* Python machine learning algrithems  **Logistic Regression**, **Support Vector Machine** for Classification and **Deep Learning** are used.

* After **Data Preprocessing** process **Feature Selection** is done by using `Correlation Matrix` which keep top 15 features highly correlated to the target variable and these 15 features are less correclated to each other. 

* **Hyperparameters Tunning** is done by using `GridSearchCV`. It allows to combine an estimator with a grid search preamble to tune hyper-parameters. The method picks the optimal parameter from the grid search and uses it with the estimator selected by the user. 

*  The **Ensemble** method is used for doing **Model Prediction**. it is a meta-algorithms that combine several machine learning techniques into one predictive model in order to decrease `variance` (bagging), `bias` (boosting), or improve predictions (stacking).


## Project Files:

* **DevHomeEquityPDModel.ipynb**: This is the script for building the machine learning model.

* **app.py**: It is the Flask Server which has two routes. The root route `/` that will show the landing page, the other route called `/predictonesample` that will prvoide the *DEFAULT* prediction API.

* **index.html**: It is `Jinja` template HTML file structured by using `bootstrap`, it takes the prediction result string and displays the data in the appropriate HTML elements.

* **modelprediction.html**: It is the page accept users' input *loan data* and show the returned *prediction result* to users.


## Final Results

By sending requests from **Brower** to the **Flask Server** can get below results: 

- - -

![result_1.png](static/images/MLModelRun.gif)

- - -
