import pandas as pd
import os


def read_excel_sheets(file_path):
    """
    Reads all sheets from an Excel file and returns a dictionary of dataframes.

    Parameters:
        file_path (str): The file path to the Excel file.

    Returns:
        dict: A dictionary containing dataframes with sheet names as keys.
    """
    excel_data = pd.read_excel(file_path, sheet_name=None)
    return excel_data


def save_dataframes_as_csv(dataframes, output_folder):
    """
    Saves each dataframe as a separate CSV file in the specified output folder.

    Parameters:
        dataframes (dict): A dictionary containing dataframes.
        output_folder (str): The path to the output folder where CSV files will be saved.
    """
    os.makedirs(output_folder, exist_ok=True)
    for name, df in dataframes.items():
        df.to_csv(os.path.join(output_folder, f"{name}.csv"), index=False)


def main():
    # Define the file path to the Excel file
    excel_file_path = "your_excel_file.xlsx"

    # Read all sheets from the Excel file
    excel_data = read_excel_sheets(excel_file_path)

    # Print sheet names
    print("Sheet Names:", list(excel_data.keys()))

    # Save dataframes as CSV files
    output_folder = "output_data"
    save_dataframes_as_csv(excel_data, output_folder)
    print("Dataframes saved as CSV files in the folder:", output_folder)


if __name__ == "__main__":
    main()
