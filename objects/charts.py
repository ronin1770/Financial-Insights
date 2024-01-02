import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

class Chart_Helper:

    def __init__(self, logger, dataframe) -> None:
        self._logger = logger
        self._dataframe = dataframe
        self._output_folder = "./output/"

    def create_income_expense_graph(self):
        outputfile = f"{self._output_folder}income_expense_graph.png"

        # Group by 'Expense Type' and sum the 'Amount' for each group
        pie_data = self._dataframe.groupby('Expense Type')['Amount'].sum()

        # Plotting the pie chart
        labels = pie_data.index
        sizes = pie_data.values
        colors = ['lightcoral', 'lightskyblue']


        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('Expense and Income Distribution')
        plt.savefig(outputfile)
    
    def create_quaterly_bar_chart(self, data_frame):
        data_frame['Date'] = pd.to_datetime(data_frame['Date'], format='%m/%d/%Y')
        data_frame['Quarter'] = data_frame['Date'].dt.to_period("Q")

        # Group by 'Quarter', 'Expense Type', and 'Expense Head', and sum the 'Amount'
        grouped_data = data_frame.groupby(['Quarter', 'Expense Type', 'Expense Head'])['Amount'].sum().reset_index()

        # Separate data into income and expense
        income_data = grouped_data[grouped_data['Expense Type'] == 'Income']
        expense_data = grouped_data[grouped_data['Expense Type'] == 'Expense']

        # Create bar graphs for income and expense
        for quarter in data_frame['Quarter'].unique():
            fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(20, 10))

            # Bar graph for income
            income_subset = income_data[income_data['Quarter'] == quarter]
            income_pivot = income_subset.pivot(index='Expense Head', columns='Quarter', values='Amount')
            income_pivot.plot(kind='bar', ax=axes[0], colormap='viridis', legend=False)
            axes[0].set_title(f'Income - Quarter {quarter}')

            # Bar graph for expense
            expense_subset = expense_data[expense_data['Quarter'] == quarter]
            expense_pivot = expense_subset.pivot(index='Expense Head', columns='Quarter', values='Amount')
            expense_pivot.plot(kind='bar', ax=axes[1], colormap='viridis', legend=False)
            axes[1].set_title(f'Expense - Quarter {quarter}')

            # Formatting y-axis as currency
            for ax in axes:
                ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('PKR{x:,.0f}'))

            # Calculate and add total income and expense to the legend
            total_income = income_subset['Amount'].sum()
            total_expense = expense_subset['Amount'].sum()
            
            axes[0].legend([f'Total Income: PKR{total_income:,.0f}'])
            axes[1].legend([f'Total Expense: PKR{total_expense:,.0f}'])

            plt.tight_layout()

            outputfile = f"{self._output_folder}quater_{quarter}.png"

            # Save the figure
            plt.savefig(outputfile)
            plt.close()  # Close the figure to release resources