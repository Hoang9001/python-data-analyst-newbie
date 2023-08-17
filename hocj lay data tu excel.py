import pandas as pd
poke=pd.read_csv('/Users/khoa/Documents/Thuc Hanh excel/raw_data_pokemon.csv')
print(poke)
#print(poke.head(10)) #lay 10 hang dau tien
print(poke.columns) #
#print(poke['Type 1'])
#print(poke[['HP', 'Attack','Generation','Type 1']])
print(poke.iloc[1,1])

