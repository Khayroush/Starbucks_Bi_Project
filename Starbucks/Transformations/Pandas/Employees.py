# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AbFP17mXDBmDhGVLZ-UVv31QZ-8uENo2
"""

from google.colab import drive
drive.mount('/content/drive')
import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Employee.csv')

df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Employee.csv')

df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/employees.csv")

df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/employees.csv", skiprows=[0])

df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/employees.csv")

df

df=df.drop(columns="COMMISSION_PCT")

df

for index, row in data.iterrows():data.at[index, 'storeId'] = 'S' + str(1000 + index)

for index, row in df.iterrows():df.at[index, 'storeId'] = 'S' + str(1000 + index)

df

for index, row in df.iterrows():
    df.at[index, 'Storeid'] = 'S' + str(1000 + (index // 7) * 7)

df

df=df.drop(columns={"JOB_ID","MANAGER_ID","DEPARTMENT_ID","storeId"	)

df=df.drop(columns={"JOB_ID","MANAGER_ID","DEPARTMENT_ID","storeId"})

df

df = df.rename(columns={'Storeid': 'storeID'})

df

d.to_json('/content/drive/MyDrive/employees.json', orient='records', lines=True)

df.to_json('/content/drive/MyDrive/employees.json', orient='records', lines=True)
