HBO Data Analysis
📌Project Overview

This project explores the HBO dataset using Python to perform data cleaning, exploratory data analysis (EDA), and visualization. The objective is to uncover trends in movie production, genres, ratings, and other key attributes while demonstrating essential data analysis skills.

🎯 Objectives
Clean and preprocess the HBO dataset.
Handle missing and duplicate values.
Analyze movie release trends over the years.
Explore genre popularity.
Study IMDb ratings and RT Score distributions.
Identify top-rated movies.
Generate meaningful visualizations to support insights.

🛠️ Tools & Technologies
Python
Pandas
NumPy
Matplotlib
Seaborn
Jupyter Notebook

📂 Dataset

The dataset contains information about movies, including:

Title
Type
Release Year
Platform
Genre
Creator/Director
Main Cast
IMDb
RT Score
Awards & Noms
Seasons
Short Sync
Viewership/Views
Popularity Indicator

📋 Data Cleaning

The following preprocessing steps were performed:

Checked data types and converted columns where necessary.
Identified and handled missing values.
Removed duplicate records.
Processed multi-genre entries using split() and explode().
Verified data consistency before analysis.

📊 Exploratory Data Analysis

The analysis includes:

Distribution of IMDb vs RT Score vs Seasons ratings.
Most common movie genres.
Top 10 Rated Tiles
Average rating by genre.
Types of watching
Average RT Score in the relation of platform and types of watching
Runtime distribution.
Top-rated movies.
Genre-wise movie counts.
Correlation between numerical features.

📈 Visualizations

Visualizations created during the project include:

Bar Charts
Histogram
Box Plot
Scatter Plot
Heatmap
Pie Chart

Key Findings

Missing values in the RT Score and Awards & Noms column were replaced with "Median" and "Mode" values.
No duplicate records were found.
Comedy is the most common genre.
TV are more common than Movie series.
TV series have a slightly higher average rating than movies.
A weak positive correlation exists between RT Score and IMDb.
Outliers in the RT Score and IMDb represent blockbuster titles and were retained because they are genuine observations.

📁 Project Structure
IMDb_Movies/
│
│   └── HBO_Dataset.csv
│
├── Notebook/
│   └── HBO_Analysis.ipynb
│
├── Images/
│   └── Visualizations
│
├── README.md
│
└── requirements.txt

Conclusion

This project demonstrates a complete Exploratory Data Analysis workflow on an IMDb dataset. Data cleaning, visualization, statistical analysis, and outlier detection were performed to better understand movie and TV show trends.

The analysis showed that dramatic content dominates the dataset, production has increased rapidly since the early 2000s, and popularity has only a weak positive relationship with audience ratings.

The project highlights essential data analysis skills including data preprocessing, visualization, feature exploration, and insight generation using Python and Pandas.


📚 Skills Demonstrated

Data Cleaning
Exploratory Data Analysis (EDA)
Data Visualization
Feature Engineering
Statistical Analysis
Python Programming
Pandas
Matplotlib
