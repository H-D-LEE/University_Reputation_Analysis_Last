# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 00:07:42 2024

@author: USER
"""

import sqlite3

def load_reputation_related_reviews(database_name):
    # 대학교 평판과 관련된 단어 목록
    reputation_keywords = ['교수', '시설', '등록금', '진로', '복지', '교과', '비교과']
    
    # 데이터베이스 연결
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    
    # 대학교 평판과 관련된 단어가 포함된 리뷰를 검색하여 가져오기
    reputation_reviews = []
    for keyword in reputation_keywords:
        query = f"SELECT university_name, review_title, review_content, date FROM university_reviews"
        cursor.execute(query)
        reputation_reviews.extend(cursor.fetchall())
    
    # # 추가 키워드에 대한 리뷰를 검색하여 가져오기
    # for category, keywords in additional_keywords.items():
    #     for keyword in keywords:
    #         query = f"SELECT university_name, review_title, review_content, date FROM university_reviews WHERE review_content LIKE '%{keyword}%' OR review_title LIKE '%{keyword}%'"
    #         cursor.execute(query)
    #         reputation_reviews.extend(cursor.fetchall())
    
    # 중복 제거
    reputation_reviews = list(set(reputation_reviews))
    
    # 연결 종료
    conn.close()
    
    return reputation_reviews