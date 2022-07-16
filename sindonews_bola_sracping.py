from bs4 import BeautifulSoup
import json, random, re, requests
import pandas as pd

r = requests.get('https://sports.sindonews.com/bola')
soup = BeautifulSoup(r.text, "html.parser")

data_berita_detik = pd.DataFrame()

for p in soup.find_all("div", {"classs": "news"}) :
    if str(p.find("div", {"class": "breaking-title"})) != "None" :
        judul = p.find("a").get_text()
        '''judul = judul.replace("\n" ,"")
        judul = judul.replace("\t" ,"")
        judul = judul.replace("  " ,"")'''
   
    
    data_berita_detik = data_berita_detik.append({'Judul' : judul}, ignore_index=True)
print(data_berita_detik)
