# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 00:12:06 2024

@author: USER
"""

import load_reputation
import create_reputation
import insert_reputation

def main():
    # 대학교 이름과 대응되는 데이터베이스 파일 딕셔너리 생성
    university_databases = {
        "한국공대": "university_reviews_tukorea.db",
        "수원대": "university_reviews_suwon.db",
        "안양대": "university_reviews_anyang.db",
        "금오공대": "university_reviews_kumoh.db",
        "삼육대": "university_reviews_syu.db",
        # 필요한 대학교와 데이터베이스 파일 추가
    }

    # 사용자로부터 대학교 이름 입력 받기
    university_name = input("대학교 이름을 입력하세요: ")

    # 입력된 대학교 이름에 해당하는 데이터베이스 파일명 가져오기
    review_database = university_databases.get(university_name)

    # 해당 대학교 이름에 대한 데이터베이스 파일이 없는 경우 처리
    if not review_database:
        print("해당 대학교에 대한 리뷰 데이터베이스 파일이 없습니다.")
        return
    
    # 데이터베이스 파일명 설정
    combines_database = 'university_reviews_combines.db'
    
    # 데이터베이스에서 대학교 평판과 관련된 리뷰 불러오기
    reputation_reviews = load_reputation.load_reputation_related_reviews(review_database)
    
    # 대학교 평판과 관련된 키워드별로 테이블 생성
    create_reputation.create_tables_for_keywords(combines_database)
    
    # 리뷰를 키워드별로 분류하여 테이블에 삽입
    insert_reputation.insert_reviews_into_keyword_tables(reputation_reviews, review_database, combines_database)

if __name__ == "__main__":
    main()
