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
        # 设置字体 雅黑
        plt.rcParams['font.sans-serif'] = ['SimHei']
        # 创建图形
        plt.figure(figsize=(20,8),dpi=80)
        labels = []
        sizes = []
        for item in groups:
            labels.append(item)
            sizes.append(groups[item].size)
            
            fig, ax = plt.subplots()
            #ax.pie(sizes,labels=labels,autopct='%1.1f%%')
            ax.pie(sizes,labels=labels, autopct='%1.1f%%',shadow=True,startangle=90)
            ax.axis('equal')
            # 显示图像
            plt.legend(loc='best')
            #plt.plot()
            plt.title("Language Pie Chart")
            plt.savefig("language_pie_chart-{}.png".format(choice))
            #plt.show()
    

