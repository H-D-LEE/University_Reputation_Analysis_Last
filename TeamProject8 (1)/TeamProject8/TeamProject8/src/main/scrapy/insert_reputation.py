# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 00:11:50 2024

@author: USER
"""

import sqlite3

def insert_reviews_into_keyword_tables(reviews, university_name, database_name='university_reviews_combines.db'):
    # 대학교 평판과 관련된 단어 목록
    reputation_keywords = ['교수', '시설', '등록금', '진로', '복지', '교과', '비교과']
    additional_keywords = {
        '교과': ['강의', '수업', '전공', '전필', '전선', '교과', '과제', '강좌', '커리큘럼', '과목'],
        '비교과': ['컨설트', '컨설팅', '검사', '워크숍', '워크샵', '공모전', '대회', '학술', '연수', '유학', '동아리', '특강', '강연', '멘토링', '튜터링'],
        '등록금': ['등록금', '입학금', '학비', '납부액', '납부금', '납부'],
        '진로': ['취직', '취업', '창업', '아웃풋', '입사', '대기업', '공기업', '중견기업', '중소기업', '직업', '연봉', '초봉'],
        '복지': ['지원', '장학', '장려', '상담', '의료', '보건', '의무실', '할인', '혜택', '편의시설'],
        '교수': ['교수님', '교수진', '교직원', '강사'],
        '시설': ['도서관', '건물', '캠퍼스', '식당', '라운지', '휴게실', '기숙사', '생활관', '자습실', '과방', '동방', '동아리실', '과실', '강의실']
    }

    # 데이터베이스 연결
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    
    # 리뷰를 키워드별로 분류하여 테이블에 삽입
    for review in reviews:
        # 대학교 평판 키워드에 대한 처리
        for keyword in reputation_keywords:
            for additional_keyword in additional_keywords[keyword]:
                if additional_keyword in review[2]:
                    # 해당 키워드 테이블에 이미 데이터가 있는지 확인
                    cursor.execute(f"SELECT * FROM {keyword} WHERE review_title=? OR review_content=?", (review[1], review[2]))
                    existing_data = cursor.fetchone()
                    if not existing_data and review[2] != '':  # 이미 데이터가 존재하지 않는 경우에만 삽입
                        cursor.execute(f"INSERT INTO {keyword} VALUES (?, ?, ?, ?)", (review[0], review[1], review[2], review[3]))

        # # 추가 키워드에 대한 처리
        # for additional_keyword, keywords_list in additional_keywords.items():
        #     for keyword in keywords_list:
        #         if keyword in review[2]:  # 리뷰에 추가 키워드가 포함된 경우
        #             # 해당 키워드 테이블에 이미 데이터가 있는지 확인
        #             cursor.execute(f"SELECT * FROM {additional_keyword} WHERE review_title=? OR review_content=?", (review[1], review[2]))
        #             existing_data = cursor.fetchone()
        #             if not existing_data and review[2] != '':  # 이미 데이터가 존재하지 않는 경우에만 삽입
        #                 cursor.execute(f"INSERT INTO {additional_keyword} VALUES (?, ?, ?, ?)", (review[0], review[1], review[2], review[3]))
                    
    # 변경사항 저장 및 연결 종료
    conn.commit()
    conn.close()