## Note: Please ensure the relevant year-csv file is uploaded to the data folder 

from objects.custom_logger import *
from objects.data_reader import DataReader
from objects.charts import Chart_Helper

#check if any file exists in the data folder
rd = DataReader(logger)
csv_files = rd.get_list_of_data_files()

logger.info(f"Number of data files in the directory: {len(csv_files)}")

#iterate over the csv_files and create the relevant dataframe

for filename in csv_files:
    logger.info(f"Reading {filename}")
    is_read = rd.read_csv_file(filename)

    if not is_read:
        logger.error(f"Issue with reading {filename}")

    result_df = rd.create_aggregate_report()
    quarterly_df = rd.create_quaterly_break_down()

    if result_df.empty:
        logger.error(f"Result data was computed successfully")
        exit(0)

    output_file = f"out_{filename}"
    exported = rd.export_to_csv(result_df, output_file)

    if not exported:
        logger.error("Failure to export output result as csv")
        exit(0)

    logger.info("Successfully exported output result as csv")

    #create the graph
    ch = Chart_Helper(logger, result_df)    
    ch.create_income_expense_graph()    
    ch.create_quaterly_bar_chart(rd._data_frame)