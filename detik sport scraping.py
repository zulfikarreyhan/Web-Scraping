from bs4 import BeautifulSoup
import json, random, re, requests
import pandas as pd

r = requests.get('https://sport.detik.com/')
soup = BeautifulSoup(r.text, "html.parser")

data_berita_detik = pd.DataFrame()

for p in soup.find_all("div",{"class":"media__text"}) :
    if str(p.find("a", {"class":"media__link"})) != "None" :
        judul = p.find("a").get_text()
        judul = judul.replace("\n" ,"")
        judul = judul.replace("\t" ,"")
        judul = judul.replace("  " ,"")
   
    
    data_berita_detik = data_berita_detik.append({'Judul' : judul }, ignore_index=True)
print(data_berita_detik)
