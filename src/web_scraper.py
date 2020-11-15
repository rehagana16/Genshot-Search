from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

source = requests.get('https://genshin-impact.fandom.com/wiki/Diluc').text
soup = BeautifulSoup(source, 'lxml')

test_article = soup.find('article')

summary = test_article.find('blockquote', class_='pull-quote').p.text

print(summary)

#test1 = soup.find('HTML ELEMENT').select one('CHILD ELEMENT').text

#test2 = soup.find('HTML ELEMENT').find_all('CHILD ELEMENT').text

