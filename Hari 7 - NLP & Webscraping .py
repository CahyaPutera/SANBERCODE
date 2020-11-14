# import library
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

# membuat target url
url = "https://www.kompas.com/"
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# mendapatkan kolom title
title = soup.findAll("h4", {"class":"most__title"})
data_title = []
for i in title:
    data_title.append(i.get_text())

# mendapatkan kolom readtime
read = soup.findAll("div", {"class":"most__read"})
data_read = []
for i in read:
    data_read.append(i.get_text())

# membuat dataframe
df = pd.DataFrame()
df['title'] = data_title
df['readtime'] = data_read

# membersihkan kolom readtime 
for i in range(0,(len(df))):
    df['readtime'][i] = df['readtime'][i].replace('Dibaca', '').replace('kali', '')

# merubah datatype menjadi float
df['readtime'] = df['readtime'].astype('float')

# print dataframe 
print(df)