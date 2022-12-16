# Data Science Salary Estimator: Project Overview
* Created a tool that estimates data science salaries (MAE ~$11K) to help data scientists negotiate their income when they get a job.
* Scraped over 1000 job descriptions from Glassdoor using Python and Selenium
* Engineered features from the text of each job description to quantify the value companies put on Python, Excel, AWS, and Spark.
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
* Built a client facin API using Flask

## Code and Resources Used
**Python Version:** 3.10.6  
**Package Requirements:** ```pip install -r requrements.txt```  
**Scraper Github:** https://github.com/arapfaik/scraping-glassdoor-selenium  
**Scraper Tutorial:** https://www.youtube.com/watch?v=GmW4F6MHqqs&list=PL2zq7klxX5AReJn7nZfqOKLZ3IpKj7fwc&index=26  
**Flask Productionaization:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2  

## YouTube Project Walk-Through
https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t  

## Web Scraping
Adapted web scraper github repo (above) to scrape 1000 job postings from glassdoor.com. From each job, we got the extracted the following:
*	Job title
*	Salary Estimate
*	Job Description
*	Rating
*	Company 
*	Location
*	Company Headquarters 
*	Company Size
*	Company Founded Date
*	Type of Ownership 
*	Industry
*	Sector
*	Revenue
*	Competitors 

## Data Cleaning
As part of the data prepartation process, the following modifications were made in order to obtain quality data for input into our model.

*	Parsed numeric data out of salary 
*	Made columns for employer provided salary and hourly wages 
*	Removed rows without salary 
*	Parsed rating out of company text 
*	Made a new column for company state 
*	Added a column for if the job was at the company’s headquarters 
*	Transformed founded date into age of company 
*	Made columns for if different skills were listed in the job description:
    * Python  
    * R  
    * Excel  
    * AWS  
    * Spark 
*	Column for simplified job title and Seniority 
*	Column for description length 

## EDA
Investigated the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables. 

![alt text](https://github.com/PlayingNumbers/ds_salary_proj/blob/master/salary_by_job_title.PNG "Salary by Position")
![alt text](https://github.com/PlayingNumbers/ds_salary_proj/blob/master/positions_by_state.png "Job Opportunities by State")
![alt text](https://github.com/PlayingNumbers/ds_salary_proj/blob/master/correlation_visual.png "Correlations")  

## Model Building 
Categorical variables were transformed into dummy variables and data was split into an 80/20 train/test split   

Three different models were tested and evaluated using Mean Absolute Error. MAE was chosen for its ease of interpretation of the target metric (US$) and outlliers are not detrimental for this type of model.

models:
*	**Multiple Linear Regression** – Baseline for the model
*	**Lasso Regression** – Because of the sparse data from the many categorical variables, normalized regression like lasso would be effective.
*	**Random Forest** – Again, with the sparsity associated with the data, this would be a good fit.

## Model performance
The Random Forest model far outperformed the other approaches on the test and validation sets. 
*	**Random Forest** : MAE = 11.19
*	**Linear Regression**: MAE = 18.77
*	**Lasso Regression**: MAE = 19.56

## Productionization 
Built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary. 
