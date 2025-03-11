import pandas as pd


def load_excel_data(infile="DISARM_FRAMEWORKS_MASTER.xlsx", only_sheets = None):
    """Load an xlsx document.

    Args:
        infile (str): Path to an xlsx file.

    Returns:
        dict: xlsx sheets

    """
    sheets = {}
    xlsx = pd.ExcelFile(infile, engine='openpyxl')
    for sheetname in xlsx.sheet_names:
        if only_sheets and sheetname not in only_sheets:
            continue
        sheets[sheetname] = xlsx.parse(sheetname)
    return sheets

