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
