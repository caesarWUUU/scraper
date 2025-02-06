import requests
from bs4 import BeautifulSoup
from collections import Counter

url = 'https://www.ptt.cc/bbs/C_Chat/M.1737734405.A.E40.html'

# 取得 PTT 文章
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
cookies = {'over18': '1'}
r = requests.get(url, headers=headers, cookies=cookies)
soup = BeautifulSoup(r.text, 'html.parser')

# 抓取留言區塊
comments = soup.find_all('div', class_='push')

# 儲存留言結果
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

# print(results)
# 用 Counter 計算票數
vote_count = Counter()

for c in results:
    content = c['content'].replace(':', '').strip()  # ✅ 修正：去掉 ':'，避免影響匹配
    if content.startswith('@'):
        candidate = content[1:2]
        if candidate in ['I', 'G']:
            vote_count[candidate] += 1


print("投票結果:")
for candidate, votes in vote_count.items():
    if candidate == 'I':
        candidate = '赫蘿'
    else:
        candidate = '八奈見杏菜'
    print(f'{candidate} 得票數: {votes}')

