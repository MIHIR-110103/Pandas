import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    department.rename(columns={
        'id':'departmentId',
        'name':'Department'
    })
    merged_df = employee.merge(department,
                                left_on = 'departmentId',
                                right_on = 'id',
                                how = 'inner',
                                suffixes = ('_emp','_dept'))

    df = merged_df.groupby('departmentId').apply(lambda x: x[x['salary']==x['salary'].max()])
    df = df[['name_dept','name_emp','salary']]
    df = df.rename(columns={
                        'name_dept':"Department",
                        'name_emp':"Employee",
                        'salary':"Salary"
    })
    return df