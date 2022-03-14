#Import package requests and BeautifulSoup
import requests
from bs4 import BeautifulSoup

#Request ke website
page = request.get("https://www.republika.co.id/")

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