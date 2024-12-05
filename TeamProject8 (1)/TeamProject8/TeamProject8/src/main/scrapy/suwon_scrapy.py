# -*- coding: utf-8 -*-
"""
Created on Sun May  5 15:49:09 2024

@author: USER
"""

import time
import requests
from bs4 import BeautifulSoup
import sqlite3

def scrape_university_reviews(university_name, start_page, end_page):
    base_url = 'https://gall.dcinside.com/board/view/?id=suwon&no={}'  # {}에는 게시물 번호가 들어갈 자리입니다.
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36'}
    
    page_num = start_page
    while True:
        url = base_url.format(page_num)
        response = requests.get(url, headers=headers)
    
        #if response.status_code != 200:
        #    break
        print(url)
        # 페이지의 HTML을 파싱합니다.
        soup = BeautifulSoup(response.content, 'html.parser')
        #print(soup)

        # 대학교 이름이 포함된 게시글만 스크래핑하여 데이터베이스에 저장합니다.
        save_to_database(university_name, soup, page_num)

        page_num += 1
        #print(page_num)
        if page_num == end_page :
            break
        time.sleep(3)  # 3초 대기 후 다음 페이지로 이동합니다.
        
        
def save_to_database(university_name, soup, page_num):
    conn = sqlite3.connect('university_reviews_suwon.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS university_reviews (university_name TEXT, review_title TEXT, review_content TEXT, date TEXT, page_num INTEGER)''')

    # 게시물 제목과 내용에서 대학교 이름이 포함되어 있는지 확인합니다.
    titles = soup.select(".ub-word > .title_subject")
    contents = soup.select(".write_div > p")
    dates = soup.select(".gall_date")
    #print(titles) 
    #print(contents)
    data_to_save = []
    
    # titles와 contents의 길이 중 작은 값을 기준으로 반복합니다.
    min_length = min(len(titles), len(contents))
    if min_length == 0:
        conn.close()
        return False  # 스크래핑한 내용이 없으면 False 반환
    
    for i in range(min_length):
        title = titles[i].text.strip()
        content = contents[i].text.strip()
        date = dates[i]['title'].strip()
        #print("제목:", title)
        #print("내용:", content)
        data_to_save.append((university_name, title, content, date, page_num))  # 페이지 번호 추가

    cursor.executemany("INSERT INTO university_reviews (university_name, review_title, review_content, date, page_num) VALUES (?, ?, ?, ?, ?)", data_to_save)
    conn.commit()
    conn.close()