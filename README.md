pip install -r requirement.txt

<requirement.txt>
pandas(numpy 같이 깔림)
seaborn (matplotlib 같이 깔림)
scikit-learn
git+https://github.com/sigmadream/koreanize-matplotlib.git
joblib
konlpy
ipykernel
flask


참고자료 :Flask (https://easyitwanner.tistory.com/347)

1)Flask 객체
from flask import Flask
app=Flask(__name__)


2)파이썬에서 시작포인트
<app.py>
if __name__ =="__main__" :
    app.run()

<terminal>
python .역슬러시app.py

Running on http://127.0.0.1:5000
 
3) http는 URI, URL 입력을 받는다.
표준 :get, post, delete, put,PATCH ,HEAD ,OPTIONS,TRACE 

4-1) app.route
@app.route("/")
def index():
    return "Hello"

4-2)app.debug
app.debug=True

4-3)get
@app.route("/")
def index():
    return "Hello"
@app.route("/hello")
def hello():
    return "하하하"


5)index.html
부트스트랩-예시-Sticky footer navbar-오른쪽마우스-소스코드보기-복사해서 index.html붙여넣기

cdnjs bootstrap 5.3 ->version 5.3.3 ->

6)JS, SPRING FOOTER에 위치

==========
1)  순서 지키기
if __name__ =="__main__" :
    load_lf()
    app.run()

 load_lf()가 먼저이므로

tfidf_vector=None
model_lf=None

def load_lf():
    global tfidf_vector, model_lf 
    tfidf_vector=joblib.load(os.path.join(app.root_path, "model/tfidf_vect.pkl"))
    model_lf=joblib.load(os.path.join(app.root_path, "model/lf.pkl"))
    pass

2) 입력-임베딩/학습- 출력
AttributeError: Can't get attribute 'tw_tokenzier' on <module '__main__' from 'C:\\NLP_VER1\\app.py'>

okt= Okt()

def tw_tokenzier(text):
    tokenzier_ko = okt.morphs(text)
    return tokenzier_ko

3) 경로
tfidf_vector=joblib.load(os.path.join(app.root_path, "model/tfidf_vect.pkl"))
    model_lf=joblib.load(os.path.join(app.root_path, "model/lf.pkl"))

4)☆☆☆ 앞에서 했던 과정을 모두 넣어야 한다.
def lt_transform(review):
    review=re.sub(r"\d+", " ", review)
    test_matrix=tfidf_vector.transform([review])
    return test_matrix

==========

    매개변수 전달
take 2 폼설계 및 전송

1) context
리액트-useeffect
spring-securityConfig

요청될 때 method랑 URL이 뭔지 알려주는 역할이 필요
Flask의 context
