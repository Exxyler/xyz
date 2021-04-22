# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 02:15:24 2020
@author: chamo

"""
import pandas as pd

train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")
target=train['target']
Id_train=train['id']
Id_test=test['id']
Datamerged=pd.concat([train,test])
Temp=Datamerged

"" "Data Preprocessing """                                 

dfnull=pd.DataFrame({'percentage null:':train.isnull().sum() / len(train)*100})
Datamergednull=pd.DataFrame({'percentage null:':Datamerged.isnull().sum() /len(Datamerged)*100})

"""NUll dataset"""

""
"""Binary encoding"""

Datamerged["bin_3"] = Datamerged["bin_3"].apply(lambda x: 1 if x=='T' else (0 if x=='F' else None))
Datamerged["bin_4"] = Datamerged["bin_4"].apply(lambda x: 1 if x=='Y' else (0 if x=='N' else None))
""""

Datamerged["nom_0"].nunique()  ##checking the unique number of files in the Data specifed columns
Datamerged["nom_1"].nunique()
Datamerged["nom_2"].nunique()
Datamerged["nom_3"].nunique() 
Datamerged["nom_4"].nunique()
Datamerged["nom_5"].nunique()
"""
"""Nominal encoding"""
"""
Datamerged["nom_0"]=Datamerged["nom_0"].apply(lambda X: 0 if X=='Red' else (1 if X=='Blue' else
          (2 if X=='Green' else  None )))
Datamerged['nom_1']=Datamerged["nom_1"].apply(lambda X: 0 if X=='Trapezoid' else (1 if X=='Star' else(
        2 if X=='Circle'else(3 if X=='Triangle' else(4 if X=='Polygon' else(5 if X=='Square' else None))))))

Datamerged['nom_2']=Datamerged["nom_2"].apply(lambda X: 0 if X=='Hamster' else (1 if X=='Axolotl' else(
        2 if X=='Lion'else(3 if X=='Dog' else(4 if X=='Cat' else(5 if X=='Snake' else None))))))

Datamerged['nom_3']=Datamerged["nom_3"].apply(lambda X: 0 if X=='Russia' else (1 if X=='Canada' else(
        2 if X=='Finland'else(3 if X=='Costa Rica' else(4 if X=='China' else(5 if X=='India' else None))))))

Datamerged["nom_4"]=Datamerged["nom_4"].apply(lambda X: 0 if X=='Bassoon' else (1 if X=='theremin' else
          (2 if X=='Oboe' else (3 if X=='Piano' else  None ))))""""
"""******************ORDINAL ENCODING**********************************************"""

Datamerged['nom_0'].fillna(Datamerged['nom_0'].mode()[0],inplace=True)
for col in Datamerged:
    print(Datamerged[col].isnull().value_counts())
    
    
""" *******************************TEMP***************************************"""   


Temp=   Temp.dropna()

for col in Temp:
    print(Temp[col].isnull().value_counts())
    



from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder=LabelEncoder()
Datamerged['nom_0']=labelencoder.fit_transform(Datamerged['nom_0'])
onehotencoder = OneHotEncoder(categorical_features = [:,8])
Datamerged= onehotencoder.fit_transform(Datamerged).toarray()
















from sklearn.preprocessing import OrdinalEncoder
ord1=OrdinalEncoder(dtype='np.int64')
ord1.fit([Datamerged['ord_1']])
Datamerged["ord_1"]=ord1.fit_transform(Datamerged["ord_1"])

Datamerged['ord_2']=Datamerged['ord_2'].apply(lambda X: 0 if X=='Freezing' else(1 if X== 'Cold' else(2 if X=='Warm' else
          (3 if X=='Hot' else (4 if X=='Boiling Hot' else (5 if X== 'Boiling Hot' else(6 if X=='Lava Hot' else None )))))))


"""********************missing values*********************""""




"""   *************************Feature selection************************* """"
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
enc=LabelEncoder()

Datamerged[:,11]=enc.fit_transform(Datamerged[:,11])
