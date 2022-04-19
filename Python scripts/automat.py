import os
import glob 
import pandas as pd  



Path = r'C:\Users\kaddi\Downloads\Automation\Python scripts'


Filenames = glob.glob(Path + '/first_demo*.xlsx')
print(Filenames)


for Filename in Filenames:
    Data =pd.read_excel(Filename)
    Data.head(5)
       