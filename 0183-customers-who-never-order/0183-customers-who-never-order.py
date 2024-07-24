import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers = customers.rename(columns={
                                'id':'customerId',
                                'name':"Customers"                                
                                })

    df_merge = pd.merge(customers,
                        orders,
                        on = 'customerId',    
                        how = 'left')

    df = df_merge[df_merge['id'].isnull() == True]
    df_names = pd.DataFrame(df['Customers'])

    return df_names