import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/C_Chat/M.1737734405.A.E40.html'



r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

comments = soup.find_all('div', class_='push')

results = []

for c in comments:
    push_tag = c.find('span', class_='hl push-tag')
    push_userid = c.find('span', class_='f3 hl push-userid')
    push_content = c.find('span', class_='f3 push-content')


    results.append({
        'tag': push_tag.get_text(strip=True) if push_tag else '',
        'user': push_userid.get_text(strip=True) if push_userid else '',
        'content': push_content.get_text(strip=True) if push_content else ''
    })

for r in results:
    print(r)
