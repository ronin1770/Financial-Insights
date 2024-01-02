import pandas as pd 
import os, traceback

class DataReader:

    def __init__(self, logger) -> None:
        self._logger = logger
        self._logger.info("Initializing DataReader")
        self._data_directory = "./data/"
        self._output_directory = "./output/"
        self._data_frame = None
    
    def get_list_of_data_files(self):
        #check if there any csv files in the data folder
        try:
            all_files = os.listdir(self._data_directory)
            csv_files = [file for file in all_files if file.endswith('.csv')]

            return csv_files
        except: 
            traceback_info = traceback.format_exc()
            self._logger.error(f"Exception in get_list_of_data_files: {traceback_info}")
            return []
        
    def read_csv_file(self, filename):
        #check if there any csv files in the data folder
        try:
            #check if the file exists
            csv_file_path = self._data_directory + filename

            if not os.path.exists(csv_file_path):
                self._logger.error(f"File {filename} doesn't exists at the location: {csv_file_path}")
                return False
            
            self._data_frame = pd.read_csv(csv_file_path)
            return True 
        except: 
            traceback_info = traceback.format_exc()
            self._logger.error(f"Exception in read_csv_file: {traceback_info}")
            return False
    
    def create_aggregate_report(self):
        if self._data_frame.empty:
            self._logger.error("Aggregate can't be created as underlying dataframe is None")
            return None        
        try:
            self._data_frame['Amount'] = pd.to_numeric(self._data_frame['Amount'].str.replace(',', ''), errors='coerce')
            self._data_frame['Amount'] = self._data_frame['Amount'].abs()

            # Group by 'Expense Type' and 'Expense Head', then sum the 'Amount' for each group
            result_df = self._data_frame.groupby(['Expense Type', 'Expense Head'])['Amount'].sum().reset_index()

            return result_df

        except: 
            traceback_info = traceback.format_exc()
            self._logger.error(f"Exception in create_aggregate_report: {traceback_info}")
            return None
        
    def export_to_csv(self, dataframe, filename):
        if dataframe.empty:
            self._logger.error("Data can't be exported to CSV as it is empty")
            return False

        try:
            output_file = self._output_directory + filename
            dataframe.to_csv(output_file, index=False)
            return True
        except: 
            traceback_info = traceback.format_exc()
            self._logger.error(f"Exception in export_to_csv: {traceback_info}")
            return None
    

    def create_quaterly_break_down(self):        
        try:
            # Assuming your dataframe is named df
            self._data_frame['Date'] = pd.to_datetime(self._data_frame['Date'], format='%m/%d/%Y')
            self._data_frame['Quarter'] = self._data_frame['Date'].dt.to_period("Q")

            # Group by 'Quarter' and 'Expense Type', then sum the 'Amount'
            result = self._data_frame.groupby(['Quarter', 'Expense Type'])['Amount'].sum().reset_index()

            # Print the result
            for index, row in result.iterrows():
                quarter = row['Quarter']
                expense_type = row['Expense Type']
                amount = row['Amount']

                print( f"{quarter} -- {expense_type} -- {amount}")
            return result
        except: 
            traceback_info = traceback.format_exc()
            self._logger.error(f"Exception in create_quaterly_break_down: {traceback_info}")
            return None
        

            