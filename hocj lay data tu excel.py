import pandas as pd
poke=pd.read_csv('/Users/khoa/Documents/Thuc Hanh excel/untitled folder/GlobalSuperstore.csv')
#print(poke)
#print(poke.head(10)) #lay 10 hang dau tien
#print(poke.columns) #list ra ten cac cot
#print(poke['Type 1']) #list cot type 1
#print(poke[['HP', 'Attack','Generation','Type 1']]) #list cac cot ra
#print(poke.iloc[1,3])  #lay du lieu hang 1 cot 3
#poke.info()
#pd.set_option('display.max_columns', 24)
#pd.set_option('display.max.row', 51290)

print(poke.head(5))
