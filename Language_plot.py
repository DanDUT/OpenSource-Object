import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    enum = ['daily','weekly','monthly']
    #enum = ['daily']
    #enum = ['weekly']
    #enum = ['monthly']
    for choice in enum:
        csvFile = 'project_info_{}.csv'.format(choice)
        handle = open(csvFile,'r',encoding='utf-8')
        reader = csv.reader(handle)
        data = list(reader)
        #numpy的array数组
        data = np.array(data)

        # analysis language
        language1 = data[1:,7]
        language2 = data[1:,8]
        language3 = data[1:,9]
        language4 = data[1:,10]
        #拼接
        language = np.concatenate((language1,language2,language3,language4)) 
        df_data = {'Language':language}
        #生成DataFrame组
        df = pd.DataFrame(df_data)
        #空格命名为Null
        df['Language'].replace('', np.nan, inplace=True)
        #去空值
        df.dropna(subset=['Language'], inplace=True)
        #去掉Other
        df.drop(df[df['Language']== 'Other'].index,inplace=True)
        #print(df)
        #分组依据
        groups = df.groupby("Language").groups

        names = []
        values = []
        for item in groups:
            names.append(item)
            values.append(groups[item].size)  
        fig, axs = plt.subplots(1,2,figsize=(40, 10), sharey=True)
        #fig, axs = plt.subplots(figsize=(30, 10), sharey=True)
        #axs.bar(names, values,color='purple')
        axs[0].bar(names, values,color='orange')
        #axs[1].scatter(names, values,color='purple')
        axs[1].plot(names, values,color='orange')
        fig.suptitle('Language Plotting')
        plt.savefig("Language_Ploting_{}.png".format(choice))
    

