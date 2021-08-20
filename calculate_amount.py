
#Calculate the total comission amount for Acquier LTDA

import pandas as pd
import numpy as np

#Create frames
transacoes = {'transaction_id':[1,2,3,4,5],
              'client_id':[3545,3545,3509,3510,4510],
              'total_amount':[3000,4500,69998,1,34],
              'discount_percentage':[6.99,0.45,0,None,40]
            }

contratos = {'contract_id':[3,4,5,6],
             'client_id':[3545,3545,3509,3510],
             'client_name':['Magazine Luiza','Magazine Luiza',
                            'Lojas Italianas','Carrerfive'],
             'percentage':[2.00,1.95,1,3.00],
             'is_active':[True,False,True,True]
            }            

#Convert do Pandas
df_trans = pd.DataFrame(transacoes)
df_contr = pd.DataFrame(contratos)

#Replace Nan values for liquid amount calculation
df_trans = df_trans.replace(to_replace = np.nan, value = 0)

#Create feature of liquid amount 
df_trans['liquid_amount'] = df_trans['total_amount'] * (1 - df_trans['discount_percentage'] / 100)

#Drop inactive contracts
df_contr.drop(df_contr[df_contr.is_active == False].index, inplace=True)

#Merge frames
total_profit = df_trans.merge(df_contr, left_on='client_id', right_on='client_id')

#Calculate the product of liquid amount and the contract percentage
total_profit['total_gain'] = total_profit['percentage'] * total_profit['liquid_amount'] / 100

#Round for better display purpouse 
total = total_profit['total_gain'].sum().round(3)

#Return value
total
