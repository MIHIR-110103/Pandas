import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    emp = employees.copy()

    emp['bonus'] = 0

    emp.loc[(emp['employee_id'] % 2 != 0) & (~emp['name'].str.startswith('M')),'bonus'] = emp['salary']
    
    output = emp[['employee_id','bonus']].sort_values(by='employee_id',ascending=True)

    return output
 
