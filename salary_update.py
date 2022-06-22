from cmath import nan
import cx_Oracle
from pydoc import apropos
from colorama import Cursor
from numpy import inner
import pandas as pd
from datetime import date
con=cx_Oracle.connect('feb22_baikuntha/feb22_baikuntha@orcl-aws.c8sefhobaih4.ap-south-1.rds.amazonaws.com:1521/ORCL')
employee=pd.read_csv('employeedetails.csv')
# print(employee)
approsal=employee.head(5)
# print(approsal)
# approsal.to_csv('aprrosal_data')
# convert DOJ  to dateformate
approsal['DOJ']=pd.DatetimeIndex(approsal['DOJ']).year
current_year=date.today().year
# find experence
approsal['experence']=current_year-approsal['DOJ']
# #print(approsal)
# # apply the bussiness rule
approsal.loc[approsal['SALARY']>=1000000 , 'SALARY']= approsal['SALARY']+approsal['SALARY']*0.15
#print(approsal)
approsal.loc[(approsal['SALARY']<=1000000 )&(approsal['experence']>3)&(approsal["experence"]<7) ,'SALARY']=approsal['SALARY']+approsal['SALARY']*0.3
# print(approsal)
approsal.loc[(approsal['SALARY']<=1000000 )&(approsal['experence']>7)&(approsal["experence"]<15) ,'SALARY']=approsal['SALARY']+approsal['SALARY']*0.35
#print(approsal)
approsal.loc[(approsal['SALARY']<=1000000 )&(approsal['experence']>15)&(approsal["experence"]<20) ,'SALARY']=approsal['SALARY']+approsal['SALARY']*0.40
#print(approsal)
#drop the nan values
approsal1=approsal.dropna()
#print(approsal)
salary_befor_update_log=approsal1[['NAME','SALARY']]
# salary_befor_update_log.to_csv('salary_before_update')
# print(approsal)
