import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee.drop_duplicates(subset='salary',inplace=True)

    sorted_sal = employee.sort_values(by='salary',ascending=False)

    if N > len(sorted_sal) or N < 1:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    sorted_sal.reset_index(inplace=True)

    return pd.DataFrame({f'getNthHighestSalary({N})':[sorted_sal.loc[N-1,'salary']]})
    # return sorted_sal