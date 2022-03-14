#Import package requests and BeautifulSoup
from datetime import datetime
import requests
from bs4 import BeautifulSoup

#Request ke website
page = requests.get("https://www.republika.co.id/")

#Extract konten menjadi objek BeautifulSoup
obj = BeautifulSoup(page.text, "html.parser");

print("\nMenampilkan Kategori, Judul, dan Waktu")
print("========================================")
now = datetime.now()
for headline in obj.find_all('div',class_='teaser_conten1_center'):
    print(headline.find('p').text)
    print(headline.find('h2').text)
    print(headline.find('div',class_='date').text)
    print(now)
    print('\n')

# #Menyimpan data file data json
print("\nMenyimpan Data pada file json")
print("========================================")
#Import package json
import json

#deklarasi list kosong
data=[]

#lokasi file json
f=open('D:\scraping\\data_berita.json','w')
for headline in obj.find_all('div',class_='teaser_conten1_center'):
    data.append({"judul" : headline.find('h2').text, "kategori" : headline.find('p').text, "waktu_publish" : headline.find('div',class_='date').text, "waktu_scraping" : now.strftime("%Y-%m-%d %H:%M:%S")})
    
jdumps = json.dumps(data)
f.writelines(jdumps)
f.close()