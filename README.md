# Financial Insights
This repository provides an idiot-proof method to get insights about your personal spending habits. It parses the given CSV and generate valuable insights about your spending habits

## Module Purpose
It provides insights about your income and expenses by parsing the uploaded CSV file. It will create following insights:

1. Pie chart depicting total income and total expense (inflows vs outflows)
2. Quarterly insights. Income vs Expense for all 4 quarters
3. Expense bar chart depicting expense in each category

## CSV File Format
Module uses a very simple CSV format as shown below:

Date, Expense Type, Expense Head, Amount

Where:
 **Date** is in **mm-dd-yyyy** format
**Expense Type** can be either **Expense** or **Income**
**Expense Head** can be a single or two word category such as: **School** or **School Books**
**Amount** is the number highlighting the transaction amount such as **45.50**

## Folder Structure
Folder structure is as follows:

**ROOT Installation Folder**
           | - -
           | - - - data
           | - - - objects
           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| - - - charts.py
           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| - - - custom_logger.py
           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| - - - data_reader.py
           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| - - -_ _init_ _.py
           | - - - output
           | - - - main.py
           | - - - requirements.txt

## Setup Python Libraries
Script assumes Python version 3.8 or higher. You can setup required Python libraries using the following code:

    pip3 install -r requirements.txt

## How to run it
You can execute the script (main.py - entry point) using the following command:

    python3 main.py

Output would look like the following:

    INFO:Yearly_Parser:Initializing DataReader
    INFO:Yearly_Parser:Number of data files in the directory: 1
    INFO:Yearly_Parser:Reading 2023.csv
    2023Q1 -- Expense -- 1525669.0
    2023Q1 -- Income -- 3502987.64
    2023Q2 -- Expense -- 1063338.0
    2023Q2 -- Income -- 2065191.0
    2023Q3 -- Expense -- 687004.0
    2023Q3 -- Income -- 4255222.0
    2023Q4 -- Expense -- 717412.0
    2023Q4 -- Income -- 6362349.69
    INFO:Yearly_Parser:Successfully exported output result as csv

