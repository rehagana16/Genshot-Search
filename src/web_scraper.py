from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import os
import codecs

url = 'https://genshin-impact.fandom.com/wiki/'

character_name_array = ['Amber', 'Barbara', 'Beidou', 'Bennett', 'Chongyun', 'Diluc', 'Diona', 'Fischl', 'Jean', 'Kaeya', 'Keqing', 'Klee', 'Lisa', 'Mona', 'Ningguang', 'Noelle', 'Qiqi', 'Razor', 'Sucrose', 'Tartaglia', 'Traveler', 'Venti', 'Xiangling', 'Xingqiu']

url += character_name_array[x]

source = requests.get('https://genshin-impact.fandom.com/wiki/Diona').text
soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')
character_description = article.find('blockquote', class_='pull-quote').p.text

article_title = soup.find('aside', class_= 'portable-infobox pi-background pi-europa pi-theme-char pi-layout-default')
character_name = article_title.h2.text

article_vision = soup.find('td', class_= 'pi-horizontal-group-item pi-data-value pi-font pi-border-color pi-item-spacing')
character_vision = article_title.find('div', class_= 'pi-data-value pi-font').a.text


print(character_name)
print(character_description)

#character_name += str('.txt')
#print(character_name)

#buat save hasil scraping ke file .txt
#fpath = os.path.join('txt_database', character_name)
#f = codecs.open(fpath,"w", encoding = 'utf-8')
#f.write(character_description)
#f.close()


