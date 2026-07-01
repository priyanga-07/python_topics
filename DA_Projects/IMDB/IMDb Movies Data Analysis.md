**IMDb Movies Data Analysis**

📌**Project Overview**



This project explores the IMDb Movies dataset using Python to perform data cleaning, exploratory data analysis (EDA), and visualization. The objective is to uncover trends in movie production, genres, ratings, and other key attributes while demonstrating essential data analysis skills.



🎯 **Objectives**

Clean and preprocess the IMDb dataset.

Handle missing and duplicate values.

Analyze movie release trends over the years.

Explore genre popularity.

Study IMDb ratings and vote distributions.

Identify top-rated movies.

Generate meaningful visualizations to support insights.



🛠️ **Tools \& Technologies**

Python

Pandas

NumPy

Matplotlib

Seaborn

Jupyter Notebook



📂 **Dataset**



The dataset contains information about movies, including:



Movie Title

Title Type

Genres

Number of vote

Year

Average Rating



📋 **Data Cleaning**



The following preprocessing steps were performed:



Checked data types and converted columns where necessary.

Identified and handled missing values.

Removed duplicate records.

Processed multi-genre entries using split() and explode().

Verified data consistency before analysis.



📊 **Exploratory Data Analysis**



The analysis includes:



Number of movies released each year.

Distribution of IMDb ratings.

Most common movie genres.

Average rating by genre.

Runtime distribution.

Top-rated movies.

Genre-wise movie counts.

Correlation between numerical features.



📈 **Visualizations**



Visualizations created during the project include:



Bar Charts

Line Charts

Histogram

Box Plot

Count Plot

Scatter Plot

Heatmap



**Key Findings**



* Missing values in the genres column were replaced with "Comedy".
* No duplicate records were found.
* The number of released titles increased significantly after 2000.
* Drama is the most common genre.
* Movies are more common than TV series.
* TV series have a slightly higher average rating than movies.
* A weak positive correlation exists between number of votes and average rating.
* Outliers in the number of votes represent blockbuster titles and were retained because they are genuine observations.



📁 Project Structure

IMDb\_Movies/

│

│   └── imdb\_movies.csv

│

├── Notebook/

│   └── IMDb\_Movies\_Analysis.ipynb

│

├── Images/

│   └── Visualizations

│

├── README.md

│

└── requirements.txt



**Conclusion**



This project demonstrates a complete Exploratory Data Analysis workflow on an IMDb dataset. Data cleaning, visualization, statistical analysis, and outlier detection were performed to better understand movie and TV show trends.



The analysis showed that dramatic content dominates the dataset, production has increased rapidly since the early 2000s, and popularity has only a weak positive relationship with audience ratings.



The project highlights essential data analysis skills including data preprocessing, visualization, feature exploration, and insight generation using Python and Pandas.





**📚 Skills Demonstrated**



Data Cleaning

Exploratory Data Analysis (EDA)

Data Visualization

Feature Engineering

Statistical Analysis

Python Programming

Pandas

Matplotlib

Seaborn

