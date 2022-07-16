from bs4 import BeautifulSoup
import json, random, re, requests
import pandas as pd

r = requests.get('https://esports.id/news')
soup = BeautifulSoup(r.text, "html.parser")

db_berita = pd.DataFrame()

for p in soup.find_all("div", {"class" : "news-list"}):
    if str(p.find_all("div", {"class":"col-8"})) != "None":
        title = p.find("h5").get_text()
        berita = p.find("p").get_text()
    if str(p.find("div", {"class":"detail"})) != "None":
        date = p.find("date").get_text()
        date = date.replace("\n","")
        date = date.replace("\t","")
        date = date.replace("","")
    if str(p.find("div",{"class":"detail"})) != "None":
        tag = p.find("span").get_text()
        
        
    db_berita = db_berita.append({'JUDUL': title, 'TANGGAL': date, 'TAG BERITA':tag, 'RINGKASAN BERITA':berita}, ignore_index=True)
    
print(db_berita)
#data_berita.to_excel('output1.xlsx', engine='xlsxwriter')