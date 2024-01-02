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
           
               | - - - charts.py
           
               | - - - custom_logger.py
           
               | - - - data_reader.py
           
               | - - -_ _init_ _.py
           
           | - - - output
           
           | - - - main.py
           
           | - - - requirements.txt

## Setup Python Libraries
Script assumes Python version 3.8 or higher. You can setup required Python libraries using the following code:

    pip3 install -r requirements.txt

## How to run it
You can execute the script (main.py - entry point) using the following command:

    python3 main.py

## Output
Output would look like the following:

    INFO:Yearly_Parser:Initializing DataReader
    INFO:Yearly_Parser:Number of data files in the directory: 1
    INFO:Yearly_Parser:Reading 2023.csv
    2023Q1 -- Expense -- 15256.0
    2023Q1 -- Income -- 3502.64
    2023Q2 -- Expense -- 1063.0
    2023Q2 -- Income -- 2065.0
    2023Q3 -- Expense -- 6874.0
    2023Q3 -- Income -- 42522.0
    2023Q4 -- Expense -- 7112.0
    2023Q4 -- Income -- 63629.69
    INFO:Yearly_Parser:Successfully exported output result as csv


Output folder will contain following files:

    income_expense_graph.png
    out_2023.csv
    quater_2023Q1.png
    quater_2023Q2.png
    quater_2023Q3.png
    quater_2023Q4.png

Where:
**income_expense_graph.png** contains the pie chart that shows annual income vs expense in a **Pie chart**.

**out_2023.csv** contains the output CSV file containing the aggregate sums per expense category  and expense type. E.g.,  expense category = School and expense type = Expense

**quater_2023Q1, quater_2023Q2, quater_2023Q3, quater_2023Q4,**  are the image files that show income vs expense bar graph and bar graph for expense categories.
