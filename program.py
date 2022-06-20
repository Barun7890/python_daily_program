from operator import contains
import re
import pandas as pd
import numpy as np
from sqlalchemy import null, true
file=pd.read_csv('list_tuple_set_dict.csv')
df=pd.DataFrame(file)
# df1=df[df['path']=='/']
#print(df)
#df1.to_csv("log_rejected.txt")
employe=df[['id','first_name','last_name']].drop_duplicates()
# print(employe)
index=employe.set_index('id')
#print(index)
index.to_csv('employedetails.csv')
df2=df['path'].str.split('/',expand=True)
df2
df1=df.copy()
df1[['c_id','course','course_name','chapter_name','with_out_chapter_name']]=df1['path'].str.split('/',expand=True)
#df1.to_excel('detail.xlsx')
df1.drop('with_out_chapter_name',axis=1,inplace=True)
#df1.to_excel('details.xlsx')
df1.drop('c_id',axis=1,inplace=True)
# df1.to_excel('detail1.xlsx')
df3=df1.copy()
df3=df3.replace(r'^s*$',float('NaN'),regex=True)
#print(df3)
df4=df3[df3.chapter_name.isnull()]
# df4.to_csv('course_log_unwanted.txt')
df5=df3[df3.chapter_name.notnull()]
#print(df5)
# change the index value
df6=df5[['id','last_login','course_name','chapter_name',]]
# #df5['c']=np.arange(df5.shape[0])
#print(df6) 
data=np.random.randint(1,1113,size=1113)
df6=pd.DataFrame(data,columns=['access_id'])
access_id=pd.concat([df5,df6])
access_id.to_excel("access_details.xlsx")
