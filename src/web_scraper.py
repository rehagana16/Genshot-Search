from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import os
import codecs





def web_scraping(filename_scraping, content_scraping) :
    character_name_array = ['Barbara', 'Beidou', 'Bennett', 'Chongyun', 'Diluc', 'Diona', 'Fischl', 'Jean', 'Kaeya', 'Keqing', 'Klee', 'Lisa', 'Mona', 'Ningguang', 'Noelle', 'Qiqi', 'Razor', 'Sucrose', 'Tartaglia', 'Traveler', 'Venti', 'Xiangling', 'Xingqiu']
    for i in range (len(character_name_array)) :
        url = 'https://genshin-impact.fandom.com/wiki/'
        url += character_name_array[i]
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')

        article = soup.find('article')
        character_description = article.find('blockquote', class_='pull-quote').p.text

        article_title = soup.find('aside', class_= 'portable-infobox pi-background pi-europa pi-theme-char pi-layout-default')
        character_name = article_title.h2.text

        filename_scraping.append(character_name)
        content_scraping.append(character_description)

        #buat save hasil scraping ke file .txt

        txt_name = character_name + str('.txt')
        fpath = os.path.join('..\\test', txt_name)
        f = codecs.open(fpath,"w", encoding = 'utf-8')
        f.write(character_description)
        f.close()





