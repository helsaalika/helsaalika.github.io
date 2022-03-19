from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import urllib.request
import json
from datetime import datetime

service = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.get("https://www.flickchart.com/Charts.aspx?genre=Fantasy&perpage=100")

now = datetime.now()
movielist = []
i = 1

for movie in driver.find_elements_by_class_name("movieInfo"):
    for img in movie.find_elements_by_tag_name("img"):
        print(img.get_attribute("src"))
    urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".png")

    ranking = movie.find_element_by_class_name("movieRanking")
    judul = movie.find_element_by_css_selector("span[itemprop='name']")
    tahun = movie.find_element_by_class_name("chartsYear")
    genre = movie.find_element_by_class_name("genre")
    print(ranking.text)
    print(tahun.text)
    print(judul.text)
    print(genre.text)

    i = i+1;
    movielist.append(
        {"ranking" : ranking.text,
         "tahun" : tahun.text,
         "judul" : judul.text,
         "genre" : genre.text,
         "img" : img.get_attribute("src"),
         "waktu" : now.strftime("%Y-%m-%d %H:%M:%S")})

hasil_scraping = open("hasilscraping.json","w")
json.dump(movielist,hasil_scraping,indent = 6)
hasil_scraping.close()

driver.quit()
