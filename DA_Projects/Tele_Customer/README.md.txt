# Telco Customer Churn Analysis

## Project Overview

This project analyzes customer churn behavior in a telecommunications company using the Telco Customer Churn dataset. The goal is to identify factors that influence customer churn and provide insights that can help improve customer retention.

## Objectives

* Understand customer demographics and service usage patterns.
* Analyze the relationship between customer churn and key variables.
* Identify factors associated with higher churn rates.
* Generate actionable business insights through data analysis and visualization.

## Dataset

The dataset contains information about telecom customers, including:

* Customer demographics
* Account information
* Contract details
* Payment methods
* Internet services
* Monthly charges
* Total charges
* Churn status

### Key Features

* Gender
* SeniorCitizen
* Partner
* Dependents
* Tenure
* PhoneService
* InternetService
* Contract
* PaymentMethod
* MonthlyCharges
* TotalCharges
* Churn

## Tools and Technologies

* Python
* Pandas
* Matplotlib
* Jupyter Notebook

## Data Cleaning

The following preprocessing steps were performed:

* Checked for missing values.
* Converted TotalCharges to numeric format.
* Handled invalid or missing values.
* Verified data types.
* Removed inconsistencies where necessary.

## Exploratory Data Analysis (EDA)

### Customer Churn Distribution

Analyzed the proportion of customers who churned versus those who stayed.

### Monthly Charges Analysis

Compared average monthly charges across:

* Churn categories
* Contract types
* Internet services
* Payment methods

### Tenure Analysis

Examined customer tenure patterns and their relationship with churn.

### Contract Analysis

Studied churn behavior across:

* Month-to-month contracts
* One-year contracts
* Two-year contracts

### Payment Method Analysis

Evaluated whether payment methods influence customer retention.

## Visualizations

The project includes:

* Bar Charts
* Grouped Bar Charts
* Histograms
* Box Plots
* Scatter Plots
* Subplots Dashboard

## Key Insights

* Customers with month-to-month contracts show higher churn rates.
* Customers with longer tenure are less likely to churn.
* Higher monthly charges are often associated with increased churn.
* Certain payment methods exhibit higher churn tendencies.

## Conclusion

The analysis highlights important factors influencing customer churn. Contract type, tenure, and monthly charges play significant roles in customer retention. These insights can help telecom companies develop targeted retention strategies.

## Repository Structure

├── data/
│   └── Telco-Customer-Churn.csv

├── notebooks/
│   └── churn_analysis.ipynb

├── images/
│   └── visualizations

├── README.md

└── requirements.txt

## Future Improvements

* Build predictive machine learning models.
* Perform feature engineering.
* Develop interactive dashboards using Tableau or Power BI.
* Deploy churn prediction models for business use.

## Author

Priyanga Amsanathan
Aspiring Data Analyst
