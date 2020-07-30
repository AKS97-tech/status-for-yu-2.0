# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 05:27:48 2020

@author: ayman
"""


import xlsxwriter
import pandas as pd
import numpy as np

total=0
counter=0
#table.xlsx#
#LTR_NAME
#HALL_CODE_NO
#CRE_DSCP
#FCY
#DNAME
#SECTION
#names#
#acadimicmembers#
#EMP_NAME
#EMP_EMAIL
#WCE_DSCP
#sheet2#
#Email
t="w1"
lst=[]
lst_1=[]
lst_email_zoom=[]
lst_email_table=[]
lstEmailNotFound=[]
#
#def check(e):
#    df_e = pd.read_excel(t+'.xlsx')
#    for i in df_e.index :
#        email_zoom = df_e['Email'][i]
##        lst_email.append(str(df_e['Email'][i]))
#        if (str(email_zoom).lower() == str(e).lower()):
#            ret=df_e['Meetings'][i]
#            return ret
##        print(email_zoom)
#    return int(0)
#def get_row(i,numb,num,subs):
##    global num,subs
##    for c in range(len_col):
#    my_list=df.iloc[i].tolist()
##    my_list = [str(my_list) for l in my_list]
#    for o,n in enumerate(my_list):
#        my_list[o]=str(my_list[o])
#    my_list.append(str(subs))
#    my_list.append(str(num))
#    my_list.append(int(numb))
#    lst.append(my_list)  
#####################
#df = pd.read_excel('table.xlsx')  
#df_e = pd.read_excel(t+'.xlsx')
#df_enf = pd.read_excel(r'table.xlsx',sheet_name='emailsNotFound')
#lstEmailNotFound.append("Email")
#for i in df_enf.index :
#    lstEmailNotFound.append(str(df_enf['Email'][i]))
#for i in df.index :
#    lst_email_table.append(str(df['الايميل'][i]))
#for i in df_e.index :
#    if(str(df_e['Email'][i]) not in lst_email_table):
#        lstEmailNotFound.append(str(df_e['Email'][i]))
#l=list(df.columns.values)
#l.append("subjects")
#l.append("numOfSub")
#l.append(t)
#elst=[]
#
#lst_1.append(l)
#for i in df.index :
#    email = df['الايميل'][i]
#    if(email not in elst):
#        subs=''
#        num=0
#        elst.append(email)
#        number = check(email)
#        for o in df.index:
#            if(str(df['الايميل'][o]).lower() == email.lower()):
#                subs +=","+str(df['رمز المساق'][o])+str(df['رقم المساق'][o])
#                num+=1
#        get_row(i,number,num,subs)
#        for i in lst:
#            lst_1.append(i)
#    else:
#        continue
#    lst.clear()
#workbook = xlsxwriter.Workbook('output_stat.xlsx')
#worksheet = workbook.add_worksheet('stat')
#for row_num, row_data in enumerate(lst_1):
#    for col_num, col_data in enumerate(row_data):
#        worksheet.write(row_num, col_num, col_data)
#worksheet = workbook.add_worksheet('emailsNotFound')
#row = 0
#column = 0
#for item in  lstEmailNotFound: 
#    worksheet.write(row, column, item) 
#    row += 1
#workbook.close() 
df = df = pd.read_excel('table.xlsx') 
for i in df.index:
    if ( df['الايميل'][i].lower() == "ayman@yu.edu.jo"):
        print(df['ت'][i])
