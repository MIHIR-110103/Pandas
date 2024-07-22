import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where student_id is 101
    filtered_df = students[students['student_id'] == 101]

    # Select only 'name' and 'age' columns
    result_df = filtered_df[['name', 'age']]

    return result_df