# Student Activeness System Using ML

## Overview

This project aims to evaluate student engagement in online classes by analyzing their interactions with a learning platform. The system captures various metrics during a session, including question attempts, mouse activity, and user engagement. The collected data is then used to train machine learning models to classify student activity levels.

## Components

### Files and Scripts

1. **`main.py`**  
   A web scraper designed to extract multiple-choice questions (MCQs) from [sanfoundry.com](https://www.sanfoundry.com). These questions are used for pop-ups during the online session.

2. **`scratch_1.txt`**  
   Contains URLs pointing to webpages with MCQs on various subjects. This file is used by `main.py` to fetch questions.

3. **`final2.csv`**  
   Contains MCQs that are used in this project for pop-up questions.

4. **`scratch_7.py`**  
   The main script that runs on the client side during an online session. It handles user interactions, including question attempts, mouse clicks, scrolls, and movements, and sends the collected data to the server.

5. **`server.py`**  
   The centralized server script that collects and stores data from various clients. It consolidates the data into a common file (`dataset.csv`).

6. **`dataset.csv`**  
   Stores the incoming data from the server. This file is used to build the dataset for training and testing the machine learning models.

7. **`mouse_log12.csv`**  
   Logs mouse activity, including scrolls, clicks, and movements, along with timestamps for a single client session.

8. **`scratch_8.py`**  
   Contains a countdown timer function used to manage the time frame for answering questions.

9. **`minor_project1 (2).csv`**  
   A collaborative file used to prepare the dataset for training the machine learning model.

10. **`Final_dataset.csv`**  
    The final dataset used for training and testing the machine learning models. It combines various sources of data into a comprehensive format.

11. **`minor activeness file1.ipynb`**  
    A Jupyter notebook used to train and test the machine learning models. It includes implementations of algorithms like SVM and KNN to classify user activity into categories such as "Very Active", "Active", "Less Active", and "Least Active".

## Getting Started

1. **Clone the Repository**

2. **Install Dependencies**
    -Ensure you have the required packages installed. You might need to install libraries like requests, beautifulsoup4, pandas, scikit-learn, etc. You can create a requirements.txt file for easier management:

3. **Run the Web Scraper**
    -To fetch MCQs run python main.py
4. **Start the Client Session**
    -Run the client-side script: python scratch_7.py
5. **Start the Server** 
    -To collect and store data: run python server.py
6. **Train and Test the Model**
    -Open the Jupyter notebook:jupyter notebook "minor activeness(1).ipynb"

Follow the instructions in the notebook to train and test the model.

-Data Flow
Data Collection:
During an online session, scratch_7.py collects data from user interactions and sends it to server.py.

-Data Storage:
server.py stores collected data in dataset.csv, which aggregates inputs from multiple sessions.

-Model Training:
The aggregated dataset (Final_dataset.csv) is used to train machine learning models using algorithms implemented in minor activeness file1.ipynb.
