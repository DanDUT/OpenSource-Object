#！/usr/bin/python
# coding: utf-8
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def testchart(a):
    #enum = ['daily','weekly','monthly']
    #enum = ['daily']
    #enum = ['monthly']
    #enum = ['weekly']
    enum = [a]
    #print(a)
    #for choice in enum:
    csvFile = 'project_info_{}.csv'.format
    handle = open(csvFile,'r',encoding='utf-8')
    reader = csv.reader(handle)
    data = list(reader)
    data = np.array(data)

     # analysis language
    #获取license所在的列
    license = data[1:,2]
    df_data = {'License':license}
     #DataFrame读入数据
    df = pd.DataFrame(df_data)
    #数据清洗，去除空值
    df.drop(df[df['License']== 'null'].index,inplace=True)
    df.drop(df[df['License']== 'Viewlicense'].index,inplace=True)
    groups = df.groupby("License").groups
    numlen=len(df)
    return numlen

if __name__ == "__main__":
    print(testchart('daily'))
    print(testchart('weekly'))
    print(testchart('monthly'))
    

