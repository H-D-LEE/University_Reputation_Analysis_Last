import json 
class Senti():
    def __init__(self, dic_file):
        self.dic_file = dic_file

    def data_list(self, wordname):	
        with open(self.dic_file, encoding='utf-8-sig', mode='r') as f:
            data = json.load(f)
        result = ['None','None']	
        for entry in data:
            if entry['word'] == wordname:
                result = [entry['word'], entry['polarity']]
                break
                
        word = result[0]
        pol = result[1]	
            
        return word, pol
    