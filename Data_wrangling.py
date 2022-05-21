#Importing required libraries
import pandas as pd #Pandas for data analysis and manipulation
import matplotlib.pyplot as plt #Matplotlib for creating visualizations

#Dataset URL: "https://www.kaggle.com/datasets/farhansadeek/ap-exam-curve-data-2022"

#Reading and printing dataset
mydataset = pd.read_csv("AP Exam Curve 2022.csv") #Store in the same folder
print("\nOriginal Dataset is given below\n")
print(mydataset)

#Printing basic stats
print("\n\nUsing describe() function on our Original Dataset\n")
description = mydataset.describe()
print(description)

#Checking and printing dimensions of dataframe
size = mydataset.size
shape = mydataset.shape
ndim = mydataset.ndim
print("\nSize of Original Dataset: {}\n".format(size))
print("Shape of Original Dataset: {}\n".format(shape))
print("ndim of Original Dataset: {}\n".format(ndim))

#Checking datatypes of variables
print("\nUsing info() function on our Original Dataset\n")
mydatasetinfo = mydataset.info()
print(mydatasetinfo)

#Checking count of variables
dtypes = mydataset.dtypes.value_counts()
print(dtypes)

#Checking for null values
nullvalsdataset = mydataset.isnull()
print("\n\nUsing  isnull() function on our Original Dataset\n")
print(nullvalsdataset)

#Filling null values if any
fillingvals = mydataset.fillna(0)
print(fillingvals)

#Checking for outliers
mydataset['Total'].plot(kind = 'box')
plt.show()
