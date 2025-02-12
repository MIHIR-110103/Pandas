import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    valid = users[users["mail"].str.contains(r'^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\?com)?\.com$')]

    return valid