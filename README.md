


# Home Equity Loan PD model

   < In Development > 

This project used <span style="color:purple;">**Machine Learning, Flask, HTML, CSS, Bootstrap**</span> to predict Home Equity Loan's probability of default. After user input data user will seee the perdiction result by rendering the templates with the model prediction result from running the machine learning model on server which uses <span style="color:purple;">**Jinja Template**</span> library on a HTML page. 

- - -

## Data Set

The data set reports characteristics and delinquency information for 5,960 home equity loans. 

A home equity loan is a loan where the obligor uses the equity of his or her home as the underlying collateral. The data set has the following characteristics:

◾ BAD: 1 = applicant defaulted on loan or seriously delinquent; 0 = applicant paid loan

◾ LOAN: Amount of the loan request

◾ MORTDUE: Amount due on existing mortgage

◾ VALUE: Value of current property

◾ REASON: DebtCon = debt consolidation; HomeImp = home improvement

◾ JOB: Occupational categories

◾ YOJ: Years at present job

◾ DEROG: Number of major derogatory reports

◾ DELINQ: Number of delinquent credit lines

◾ CLAGE: Age of oldest credit line in months

◾ NINQ: Number of recent credit inquiries

◾ CLNO: Number of credit lines

◾ DEBTINC: Debt-to-income ratio


## Technologies Used

*  **Bootstrap Table** is used to set the layout of the webpage and it can makes a *Responsive Tables* by using `table-responsive` class. It scrolls horizontally up to small devices (under 768px) and when viewing on anything larger than 768px wide no any difference.

* Python data manipulation and analysis library **Pandas** is used for importing table data from a webpage adn convert the data to a HTML table string. 

* Python web framework **Flask** and it's extensions **Render_Template** and **Redirect** are used to establish database connection,  to render templates with specific data by using Jinja template library, redirect route back to home page.

* Python machine learning algrithems  **Logistic Regression** and **SVM** are used.

## Project Files:

* **DevHomeEquityPDModel.ipynb**: This is the script for building the machine learning model.

* **app.py**: It is the Flask Server which has two routes. The root route `/` that will show the landing page, the other route called `/prediction` that will prvoide the default prediction API.

* **index.html**: It is `Jinja` template HTML file structured by using `bootstrap`, it takes the prediction result string and displays all of the data in the appropriate HTML elements.

* **modelprediction.html**: It is the page accept user's input and show the predictio result.

## Final Results

By sending requests from **Brower** to the **Flask Server** can get below results: 

- - -




- - -
