import sqlite3
import tukorea_scrapy
import suwon_scrapy
import syu_scrapy
import anyang_scrapy
import kumoh_scrapy
import load_reputation
import create_reputation
import insert_reputation
from flask_cors import CORS
import json
from flask import Flask, request, jsonify, Response

# 대학교 이름과 대응되는 데이터베이스 파일 딕셔너리 생성
university_databases = {
    "한국공대": "university_reviews_tukorea.db",
    "수원대": "university_reviews_suwon.db",
    "안양대": "university_reviews_anyang.db",
    "금오공대": "university_reviews_kumoh.db",
    "삼육대": "university_reviews_syu.db"
    # 필요한 대학교와 데이터베이스 파일 추가
}

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'This is Home!'

@app.route('/searchPost', methods=["POST"])
def search_post():
    print("test")
    # university_name = request.form['keyword']
    # university_name = request.json['keyword']
    print(request.data)
    university_name = json.loads(request.data)['keyword']
    review_database = university_databases.get(university_name)
    print("university_name ", university_name)
    print("review_database ", review_database)
    if not review_database:
        return jsonify({"message": "해당 대학교에 대한 리뷰 데이터베이스 파일이 없습니다."}), 404

    # 쿼리 실행하여 총 갯수 구하기
    conn = sqlite3.connect(review_database)
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(page_num) FROM university_reviews WHERE university_name = ?", (university_name,))
    result = cursor.fetchone()[0]
    conn.close()
    
    # start_page 계산
    start_page = int(result) + 1
    last_page = start_page + 10

    # 해당 대학의 리뷰 스크래핑
    if university_name == "한국공대":
        scrapy_university = tukorea_scrapy.scrape_university_reviews(university_name, start_page, last_page)
    elif university_name == "수원대":
        scrapy_university = suwon_scrapy.scrape_university_reviews(university_name, start_page, last_page)
    elif university_name == "안양대":
        scrapy_university = anyang_scrapy.scrape_university_reviews(university_name, start_page, last_page)
    elif university_name == "금오공대":
        scrapy_university = kumoh_scrapy.scrape_university_reviews(university_name, start_page, last_page)
    elif university_name == "삼육대":
        scrapy_university = syu_scrapy.scrape_university_reviews(university_name, start_page, last_page)
    else:
        return jsonify({"message": "해당 대학교에 대한 데이터는 존재하지 않습니다."}), 404

    # 대학 평판 관련 리뷰 로드
    combines_database = 'university_reviews_combines.db'
    reputation_reviews = load_reputation.load_reputation_related_reviews(review_database)

    # 대학 평판 관련 테이블 생성 및 리뷰 삽입
    create_reputation.create_tables_for_keywords(combines_database)
    insert_reputation.insert_reviews_into_keyword_tables(reputation_reviews, review_database, combines_database)

    # 응답
    response = jsonify({"message": "데이터 처리가 완료되었습니다."})
    # response.headers.add('Cache-Control', 'no-store')
    response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
    return response, 200

if __name__ == '__main__':
    app.run('127.0.0.1',port=5000,debug=True)