# (c) 2026 Середенко К.А. Все права защищены. См. LICENSE
import time
import requests
import llm
import load
from bs4 import BeautifulSoup

infin = 1
link_old = 0
link_old1 = 0

def serch_aif_k():
    url = 'https://kamchatka.aif.ru/news/region' # Отправляем запрос на сайт
    response = requests.get(url) # Отправляем запрос на сайт

    soup = BeautifulSoup(response.text, 'html.parser') # Создаем объект BeautifulSoup для парсинга HTML

    no_title_element_js = soup.find('a', class_='img_box no_title_element_js')
    link = no_title_element_js['href']

    global link_old

    print(link)
    if link_old != link: 
        print("Новая_новость_на_аиф_к")
        link_old = link
        response = requests.get(link) # Отправляем запрос на сайт
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('meta', property="og:title")
        title = title['content']
        print("-----------------<title>-----------------------")
        print(title)
        print("-----------------<news>------------------------")
        article_text = soup.find('div', class_="article_text")
        news_text1 = article_text.get_text('\n' ,strip=True) # получаем новости в формате строки 
        
        print(news_text1)
        print("-----------------<LLM-title>-------------------")
        title_ = llm.paraphrase_single_title(title) # Запрос к LLM
        print(title_)
        print("-----------------<LLM-news>--------------------")
        news_ = llm.paraphrase_single_article(news_text1) # Запрос к LLM
        print(news_)
        print("-----------------<end>-------------------------")
        news_ = "<p>" + news_ + "</p>"
        load.login(title_, news_)
        print("Загрузка успешна")


    elif link_old == link:
        print("Старая_новость_на_аиф_к")


def serch_mk_s():
    url = 'https://www.mk-sakhalin.ru/news/' # Отправляем запрос на сайт
    response = requests.get(url) # Отправляем запрос на сайт

    soup = BeautifulSoup(response.text, 'html.parser') # Создаем объект BeautifulSoup для парсинга HTML

    no_title_element_js = soup.find('a', class_='news-listing__item-link')
    link = no_title_element_js['href']

    global link_old1

    print(link)
    if link_old1 != link: 
        print("Новая_новость_на_мк_с")
        link_old1 = link
        response = requests.get(link) # Отправляем запрос на сайт
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('meta', property="og:title")
        title = title['content']
        print("-----------------<title>-----------------------")
        print(title)
        print("-----------------<news>------------------------")
        article_text = soup.find('div', class_="article__description")
        article_text1 = article_text.find('p')
        

        article_text = soup.find('div', class_="article__body")

        article_text2 = article_text.find_all('p')
        
        news_text1 = str(article_text1) + str(article_text2)
 
        
        print(news_text1)
        print("-----------------<LLM-title>-------------------")
        title_ = llm.paraphrase_single_title(title) # Запрос к LLM
        print(title_)
        print("-----------------<LLM-news>--------------------")
        news_ = llm.paraphrase_single_article(news_text1) # Запрос к LLM
        print(news_)
        print("-----------------<end>-------------------------")
        news_ = "<p>" + news_ + "</p>"
        load.login(title_, news_)
        print("Загрузка успешна")


    elif link_old == link:
        print("Старая_новость_на_мк_с")


# бесконечный цикл
while infin == 1:
    time.sleep(90)
    serch_aif_k()
    time.sleep(90)
#    serch_mk_s()
