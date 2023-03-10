import requests
import re
from all_links import links
from tqdm import tqdm
from bs4 import BeautifulSoup

count = 1
lnk = "Link "
title_ru = "Title (rus): "
desc_rus = "Description (rus): "
title_eng = "Title (eng): "
desc_eng = "Description (eng): "
pub_date = "Publish date: "

for link in tqdm(links):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')

    if response.status_code == 200:
        with open('response.html', 'wb') as f:
            f.write(response.content)

        with open('response.html', 'r') as f:
            content = f.read()

        # Matching css-selectors
        match_title_eng = soup.find("meta", itemprop="name")["content"]

        match_desc_eng = soup.find('meta', {'name': 'description'})['content']

        match_date = soup.find('meta', {'itemprop': 'datePublished'})['content']

        # Matching regulars
        match_title = re.search(r'playerOverlayVideoDetailsRenderer":{"title":{"simpleText":".*?"},', content,
                                re.DOTALL)
        if match_title:
            data_title = match_title.group(0)

        match_description = re.search(r'description":{"simpleText":".*?"},', content, re.DOTALL)
        if match_description:
            data_desc = match_description.group(0)
            all_data = f"{lnk}{count}: {link}\n{pub_date}{match_date}\n{title_ru}{data_title}\n{desc_rus}{data_desc}\n{title_eng}{match_title_eng}\n{desc_eng}{match_desc_eng}\n\n"
            all_data = all_data.replace('playerOverlayVideoDetailsRenderer":{"title":{"simpleText":', '')
            all_data = all_data.replace('description":{"simpleText":"', '')
            all_data = all_data.replace('"}', '')
            all_data = all_data.replace('}}]}},', '')
            all_data = all_data.replace('"},', '')

            with open('parse_result.txt', 'a') as f:
                f.write(all_data + '\n')

        count += 1
    else:
        print('Page load error:', response.status_code)
