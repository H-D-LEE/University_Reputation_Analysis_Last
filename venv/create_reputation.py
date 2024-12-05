# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 00:09:02 2024

@author: USER
"""

import sqlite3

def create_tables_for_keywords(database_name='university_reviews_combines.db'):
    # 대학교 평판과 관련된 단어 목록
    reputation_keywords = ['교수', '시설', '등록금', '진로', '복지', '교과', '비교과']
    
    # # 추가 키워드
    # additional_keywords = {
    #     '교과': ['강의', '수업', '전공', '전필', '전선', '교과', '과제', '강좌', '커리큘럼', '과목'],
    #     '비교과': ['컨설트', '컨설팅', '검사', '워크숍', '워크샵', '공모전', '대회', '학술', '연수', '유학', '동아리', '특강', '강연', '멘토링', '튜터링'],
    #     '등록금': ['등록금', '입학금', '학비', '납부액', '납부금', '납부'],
    #     '진로': ['취직', '취업', '창업', '아웃풋', '입사', '대기업', '공기업', '중견기업', '중소기업', '직업', '연봉', '초봉'],
    #     '복지': ['지원', '장학', '장려', '상담', '의료', '보건', '의무실', '할인', '혜택', '편의시설'],
    #     '교수': ['교수님', '교수진', '교직원', '강사'],
    #     '시설': ['도서관', '건물', '캠퍼스', '식당', '라운지', '휴게실', '기숙사', '생활관', '자습실', '과방', '동방', '동아리실', '과실', '강의실']
    # }
    
    # 데이터베이스 연결
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    
    # 각 키워드별로 테이블 생성
    for keyword in reputation_keywords:
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {keyword} (
                            university_name TEXT,
                            review_title TEXT,
                            review_content TEXT,
                            date TEXT,
                            CONSTRAINT title_unique UNIQUE (review_title),
                            CONSTRAINT content_unique UNIQUE (review_content))''')
    
    # # 추가 키워드에 대한 테이블 생성 및 데이터 저장
    # for category, keywords in additional_keywords.items():
    #     # 테이블 생성
    #     cursor.execute(f'''CREATE TABLE IF NOT EXISTS {category} (
    #                         university_name TEXT,
    #                         review_title TEXT,
    #                         review_content TEXT,
    #                         date TEXT,
    #                         CONSTRAINT title_unique UNIQUE (review_title),
    #                         CONSTRAINT content_unique UNIQUE (review_content))''')
    #     # 추가 키워드에 대한 글들을 해당 테이블에 저장
    #     for keyword in keywords:
    #         cursor.execute(f'''
    #             INSERT INTO {category} (university_name, review_title, review_content, date)
    #             SELECT university_name, review_title, review_content, date
    #             FROM university_reviews
    #             WHERE review_content LIKE '%{keyword}%' OR review_title LIKE '%{keyword}%'
    #         ''')
    
    # 연결 종료
    conn.close()