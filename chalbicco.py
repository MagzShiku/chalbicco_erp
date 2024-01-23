import pandas as pd

def process_data(file_path):
    # Read the Excel file
    data = pd.read_excel(file_path)

    # Access the necessary sheets
    names_and_ids = data['Names and IDs']
    savings = data['Savings']
    loans = data['Loans']
    interest = data['Interest']

    # Process the data and perform calculations
    for index, row in names_and_ids.iterrows():
        name = row['Name']
        id = row['ID']
        savings_amount = savings.loc[savings['ID'] == id, 'Savings Amount'].values[0]
        loan_amount = loans.loc[loans['ID'] == id, 'Loan Amount'].values[0]
        loan_interest = loans.loc[loans['ID'] == id, 'Loan Interest'].values[0]
        savings_interest = savings_amount * 0.05  # Assuming 5% interest rate for savings
        total_interest = savings_interest - loan_interest

        # Print or store the results as per your requirement
        print(f"Name: {name}, ID: {id}, Savings: {savings_amount}, Loan: {loan_amount}, Total Interest: {total_interest}")

# Provide the file path of the Excel sheet
file_path = "path_to_your_excel_file.xlsx"

# Call the function to process the data
process_data(file_path)
