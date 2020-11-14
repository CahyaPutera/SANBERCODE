# import library
import re
import string 
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

# membuat target url
url = "https://www.kompas.com/global/read/2020/11/13/103507770/ini-bukan-pertama-kalinya-perusahaan-korea-selatan-dituding-bakar-hutan"
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# scraping isi berita
content = soup.findAll("div", {"class":"read__content"})
text = []
for i in content:
    text.append(i.get_text())

# membuat function untuk proses case folding
def case_folding(data):

    # merubah menjadi lowercase    
    data = data.lower()
    
    # menghapus angka    
    data = re.sub(r"\d+", "", data)
    
    # menghapus tanda baca
    data = data.translate(str.maketrans("","",string.punctuation))
    
    # menghapus white spaces
    data = data.replace('\n', '')
    
    # return data
    return data

# membuat function untuk filter stopword
def stopword_filter(data, stopword):
    
    # mendefinisikan dan memisahkan stopword
    stopword = list()
    word_split = data.split()

    # memfilter stopword
    filters = [i for i in word_split if i not in stopword]
    results = ' '.join(filters)

    # return result
    return results

# melakukan case folding pada text
text_clean = case_folding(text[0])

# mendefinisikan stopword dan melakukan stopword removal
stop_word = ['aku', 'saya', 'dan', 'kamu', 'yang', 'itu']
filtered_text = stopword_filter(text_clean, stop_word)

# print text 
print(filtered_text)