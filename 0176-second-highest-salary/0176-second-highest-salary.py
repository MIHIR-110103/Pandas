import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    employee.drop_duplicates(subset='salary',inplace=True)

    sorted_sal = employee.sort_values(by='salary',ascending=False)

    if 2 > len(sorted_sal):
        return pd.DataFrame({f'SecondHighestSalary': [None]})
    
    sorted_sal.reset_index(inplace=True)

    return pd.DataFrame({f'SecondHighestSalary':[sorted_sal.loc[1,'salary']]})