from flask import Flask, render_template, request
import joblib
import os
from konlpy.tag import Okt 
import re
app=Flask(__name__)
app.debug=True

tfidf_vector=None
model_lf=None

okt= Okt()

def tw_tokenzier(text):
    tokenzier_ko = okt.morphs(text)
    return tokenzier_ko

def load_lf():
    global tfidf_vector, model_lf 
    tfidf_vector=joblib.load(os.path.join(app.root_path, "model/tfidf_vect.pkl"))
    model_lf=joblib.load(os.path.join(app.root_path, "model/lf.pkl"))
    pass

def lt_transform(review):
    review=re.sub(r"\d+", " ", review)
    test_matrix=tfidf_vector.transform([review])
    return test_matrix

@app.route("/predict", methods=["GET","POST"])
def nlp_predict():
    if request.method== "GET":
       return render_template("predict.html")
    else :
        _review=request.form["review"]  
        _review_matrix=tfidf_vector.transform([ _review])
        _review_result=model_lf.predict(_review_matrix)[0]
        _review_result="긍정" if _review_result else "부정"
        result={
           "review": _review,
           "review_result":_review_result
        }
        return render_template("predict_result.html", result=result)  

@app.route("/")
def index():
    
    # 해당 테스트 코드는 잘 작동하지만
    # 별도의 함수로 빠져나가야 됨
   # test_str = "이 영화 재미있어요! 하하하"
   # test_matrix = lt_transform(test_str)
   # result = model_lr.predict(test_matrix)
   # print(result)
    return render_template("index.html")


if __name__ =="__main__" :
    load_lf()
    app.run()