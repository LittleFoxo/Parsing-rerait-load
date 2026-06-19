import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime


def login(title_, news_):
    session = requests.Session()
    login_page = session.get('')
    
    soup = BeautifulSoup(login_page.text, 'html.parser')
    csrf_meta = soup.find('meta', {'name': 'csrf-token'})
    if csrf_meta:
        csrf = csrf_meta['content']
    else:
        raise Exception('CSRF token not found')

    data = {
        'csrf_token': csrf,
        'login_email': '',      
        'login_password': '',   
        'submit': '1',
        'back': '',
    }

    response = session.post('', data=data)
    
    if response.status_code == 200:
        print("Успешный вход")
        success = load(title_, news_, csrf, session)
        print("Успех код 200" if success else f"Неудача2: {response.status_code}" + "Тело ответа:" + response.text[:500])
    else:
        print("Неудача1. Тело ответа:", response.text[:500])

def load(title_, news_, csrf, session): 
    now = datetime.now()
    
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Referer': '',
    })
    
    form_data = {
        "csrf_token": csrf,
        "category_id": "8",
        "title": title_,
        "teaser": title_,
        "content": news_,
        "is_private": "0",
        "is_pub": "0",
        "to_draft": "Сохранить в черновиках",
        "date_pub[date]": now.strftime("%d.%m.%Y"),
    }
    
    url = ""
    resp = session.post(url, data=form_data, allow_redirects=False)
    
    soup = BeautifulSoup(resp.text, 'html.parser')
    errors = soup.find_all(class_='error')
    print("Ошибки формы:", [e.text for e in errors])

    return len(errors) == 0
 

    