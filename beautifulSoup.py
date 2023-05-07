from bs4 import BeautifulSoup
import requests
from database import databaseAdd

# Siteye get isteği gönderilir.
response = requests.get('https://t24.com.tr/')

# Web sayfasının içeriği çekilir.
html_content = response.content

# BeautifulSoup objesi oluşturulur.
soup = BeautifulSoup(html_content, 'html.parser')

# Gerekli ul etiketi seçilir.
ul_element = soup.findAll('ul',class_="_1nNTb")
print(len(ul_element))

for li in ul_element:
    a_tag = li.findAll('a')
    for a in a_tag:
        if a:
            link = a['href']
            response2 = requests.get(link)
            response2 =response2.content
            docs2 = BeautifulSoup(response2 ,'html.parser')
            title = docs2.title.text
            try:
                published_date = docs2.find('div',class_ ='_392lz')
                published_date =published_date.find('p').text
            except Exception as e:
                print("Eror message:", e)
                import traceback
                print("Traceback info:")
                traceback.print_exc()

            try:
                databaseAdd('news.db','News',[title,link,published_date],['title','link','published_date'])
            except Exception as e:
                print("Eror message:", e)
                import traceback
                print("Traceback info:")
                traceback.print_exc()
