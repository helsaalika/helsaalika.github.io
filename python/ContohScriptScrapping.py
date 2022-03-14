#Import package requests and BeautifulSoup
import requests
from bs4 import BeautifulSoup

#Request ke website
page = requests.get("https://www.republika.co.id/")

#Extract konten menjadi objek BeautifulSoup
obj = BeautifulSoup(page.text, "html.parser");

print("Menampilkan Objek")
print("===================")
print(obj)

print("\nMenampilkan title browser dengan tag")
print("========================================")
print(obj.title)

print("\nMenampilkan title browser tanpa tag")
print("========================================")
print(obj.title.text)

print("\nMenampilkan semua tag h2")
print("========================================")
print(obj.find_all('h2'))

print("\nMenampilkan semua tag h2")
print("========================================")
for headline in obj.find_all('h2'):
    print (headline.text)

print("\nMenampilkan headline berdasarkan div class")
print("==============================================")
print(obj.find_all('div',class_='bungkus_txt_headline_center'))

print("\nMenampilkan semua teks headline")
print("========================================")
for headline in obj.find_all('div',class_='bungkus_txt_headline_center'):
    print(headline.find('h2').text)


#Menyimpan data file data txt
print("\nMenyimpan headline pada file txt")
print("========================================")
f=open('D:\scraping\\headline.txt','w')
for headline in obj.find_all('div',class_='bungkus_txt_headline_center'):
    f.write(headline.find('h2').text)
    f.write('\n')
f.close()


#Menyimpan data file data json
print("\nMenyimpan headline pada file json")
print("========================================")
#Import package json
import json

#deklarasi list kosong
data=[]

#lokasi file json
f=open('D:\scraping\\headline.json','w')
for headline in obj.find_all('div',class_='bungkus_txt_headline_center'):
    data.append({"judul":headline.find('h2').text})

jdumps=json.dumps(data)
f.writelines(jdumps)
f.close()