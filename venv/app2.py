from flask_cors import CORS
import json
from flask import Flask, request, jsonify, Response
import senti_module as st

# 감성 사전 주소
senti_dic = 'Univ_SentiWord.json'

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    data=request.json
    results= []

    for item in data:
        print("진행중...")
        senti = st.analyze_sentiments(item['review_content'], senti_dic)
        cum_polarity=0
        for score in senti[1].values():
            cum_polarity += score
        results.append({senti[0] : st.pn_classificate(cum_polarity)})
        
    return jsonify(results)

if __name__ == '__main__':
    app.run('127.0.0.1',port=5050,debug=True)