import pandas as pd


def load_excel_data(infile="DISARM_FRAMEWORKS_MASTER.xlsx"):
    """Load an xlsx document.

    Args:
        infile (str): Path to an xlsx file.

    Returns:
        dict: xlsx sheets

    """
    sheets = {}
    xlsx = pd.ExcelFile(infile)
    for sheetname in xlsx.sheet_names:
        sheets[sheetname] = xlsx.parse(sheetname)
    return sheets

