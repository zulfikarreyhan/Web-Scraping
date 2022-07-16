from bs4 import BeautifulSoup
import json, random, re, requests
import pandas as pd

r = requests.get('https://sports.sindonews.com/bola')
soup = BeautifulSoup(r.text, "html.parser")

data_berita_sindo = pd.DataFrame()

for p in soup.find_all("div", {"class":"breaking-title"}) :
    if str(p.find("div", {"class":"breaking-title"})) != "None" :
        judul = p.find("a").get_text()
        waktu = p.find("p").get_text()
        
    
    data_berita_sindo = data_berita_sindo.append({'Judul':judul, 'Waktu' : waktu}, ignore_index=True)

print(data_berita_sindo)
